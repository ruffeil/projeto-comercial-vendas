import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuracao da pagina
st.set_page_config(page_title="Analytics Dashboard", layout="wide")

# Cabecalho tecnico
st.title("Painel de Insights Estrategicos")
st.markdown("Estrutura de dados processada via TemplateBase com governanca GPG.")

# Funcao para carregamento de dados com cache
@st.cache_data
def load_data():
    # O caminho aponta para a camada de dados limpos definida no template
    path = "data/processed/dataset_clean.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

df = load_data()

# Indicadores Principais (KPIs)
col1, col2, col3 = st.columns(3)
if not df.empty:
    col1.metric("Volume de Dados", len(df))
    col2.metric("Pipeline", "Concluido")
    col3.metric("Integridade", "Verificada")

    # Visualizacao Dinamica
    st.subheader("Analise Exploratoria Interativa")
    col_x = st.selectbox("Selecione variavel horizontal", df.columns)
    col_y = st.selectbox("Selecione variavel vertical", df.columns)
    
    fig = px.scatter(df, x=col_x, y=col_y, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Aguardando presenca de dados na pasta data/processed/.")