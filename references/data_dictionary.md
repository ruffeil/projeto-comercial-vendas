# Dicionário de Dados e Metadados

Este documento detalha a estrutura das variáveis utilizadas nos projetos vinculados ao **TemplateBase**, garantindo a rastreabilidade e o entendimento técnico da origem ao output.

---

## 1. Camada Raw (Dados Brutos)
*Arquivos originais e imutáveis.*

| Variável | Tipo | Descrição | Regra de LGPD |
| :--- | :--- | :--- | :--- |
| `id_cliente` | Inteiro | Identificador único do cliente | Pseudonimização aplicada |
| `data_transacao` | Timestamp | Data e hora da operação | Dado operacional |
| `valor_bruto` | Decimal | Valor original da transação | Dado financeiro |

---

## 2. Camada Interim (Transformações)
*Dados em fase de limpeza e tipagem.*

| Variável | Origem | Transformação | Finalidade |
| :--- | :--- | :--- | :--- |
| `valor_net` | `valor_bruto` | Dedução de taxas e impostos | Cálculo de margem |
| `status_pagamento` | Vários | Padronização de strings (Categorização) | Filtros de dashboard |

---

## 3. Camada Processed (Feature Store / Final)
*Dados prontos para modelos de ML e Dashboards.*

| Variável | Tipo | Descrição | Relevância Científica |
| :--- | :--- | :--- | :--- |
| `churn_risk` | Float | Probabilidade de evasão (0 a 1) | Target do modelo preditivo |
| `score_fidelidade` | Inteiro | Pontuação baseada em histórico | Feature de segmentação |

---

## 5. Métricas de Performance Comercial (Output SQL)
| Variável | Descrição | Lógica Técnica |
| :--- | :--- | :--- |
| `total_mrr` | Receita Mensal Recorrente | Soma do `net_value` por mês de referência. |
| `churn_rate_percentage` | Taxa de Evasão Mensal | Média de clientes que não retornaram no mês seguinte. |
| `active_customers` | Base Ativa | Contagem distinta de IDs com transações no período. |

---

## 4. Histórico de Alterações
* **2026-01-07**: Criação da estrutura base de metadados (J. F. Ruffeil).