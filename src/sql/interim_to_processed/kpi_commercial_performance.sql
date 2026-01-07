/*
PROJETO: Análise de Indicadores Comerciais - Portfólio J. F. Ruffeil
OBJETIVO: Calcular MRR (Receita Mensal) e Churn Rate (Taxa de Evasão)
CAMADA: Interim -> Processed
GOVERNANÇA: Dados tratados conforme GOVERNANCE.md e LGPD
*/

WITH monthly_revenue AS (
    -- Etapa 1: Agrupar receita por cliente e por mês
    SELECT 
        customer_id,
        DATE_TRUNC('month', transaction_date) AS reference_month,
        SUM(net_value) AS mrr_value
    FROM interim_sales_data 
    GROUP BY 1, 2
),

customer_activity AS (
    -- Etapa 2: Identificar se o cliente retornou no mês seguinte (Lead Function)
    SELECT
        customer_id,
        reference_month,
        mrr_value,
        LEAD(reference_month) OVER (PARTITION BY customer_id ORDER BY reference_month) AS next_active_month
    FROM monthly_revenue
),

churn_flagging AS (
    -- Etapa 3: Marcar Churn se não houver registro no mês subsequente
    SELECT
        reference_month,
        mrr_value,
        CASE 
            WHEN next_active_month IS NULL OR next_active_month > reference_month + INTERVAL '1 month' 
            THEN 1 ELSE 0 
        END AS is_churn
    FROM customer_activity
)

-- Etapa Final: Consolidar Indicadores para o Dashboard
SELECT 
    reference_month,
    ROUND(SUM(mrr_value), 2) AS total_mrr,
    COUNT(DISTINCT is_churn) AS active_customers,
    ROUND(AVG(is_churn) * 100, 2) AS churn_rate_percentage
FROM churn_flagging
GROUP BY 1
ORDER BY 1 DESC;