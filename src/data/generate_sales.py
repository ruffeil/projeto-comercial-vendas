#este é um arquivo gerado para testes de performance.

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Garante que a pasta de dados brutos exista
os.makedirs('data/raw', exist_ok=True)

# Semente para dados iguais sempre
np.random.seed(42)

# Gera 1000 linhas de transações
n_rows = 1000
df = pd.DataFrame({
    'transaction_id': range(1001, 1001 + n_rows),
    'customer_id': np.random.randint(1, 200, n_rows),
    'transaction_date': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)],
    'net_value': np.random.uniform(50.0, 500.0, n_rows).round(2),
    'status': np.random.choice(['paid', 'refunded'], n_rows, p=[0.9, 0.1])
})

# Salva o arquivo na pasta correta
df.to_csv('data/raw/sales_raw_2025.csv', index=False)
print("Dataset gerado com sucesso em data/raw/sales_raw_2025.csv!")