import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Dashboard - E-commerce",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def carregar_dados():
    caminho = Path("data/vendas_ecommerce.csv")
    df = pd.read_csv(caminho)
    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]
    df["mes"] = df["data_pedido"].dt.to_period("M").astype(str)
    return df

df = carregar_dados()

st.title("📊 Análise de Vendas em E-commerce")
st.write("Dashboard desenvolvido para a 2ª entrega do Projeto Integrador.")

# Filtros
st.sidebar.header("Filtros")
categorias = st.sidebar.multiselect(
    "Categoria",
    sorted(df["categoria"].dropna().unique()),
    default=sorted(df["categoria"].dropna().unique())
)
status = st.sidebar.multiselect(
    "Status do pedido",
    sorted(df["status"].dropna().unique()),
    default=sorted(df["status"].dropna().unique())
)
estados = st.sidebar.multiselect(
    "Estado",
    sorted(df["estado"].dropna().unique()),
    default=sorted(df["estado"].dropna().unique())
)

df_filtrado = df[
    (df["categoria"].isin(categorias)) &
    (df["status"].isin(status)) &
    (df["estado"].isin(estados))
]

# Métricas
pedidos = df_filtrado["id_pedido"].nunique()
faturamento = df_filtrado.loc[df_filtrado["status"] != "Cancelado", "valor_total"].sum()
ticket_medio = faturamento / pedidos if pedidos else 0
qtd_itens = df_filtrado["quantidade"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de pedidos", f"{pedidos}")
col2.metric("Faturamento", f"R$ {faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col3.metric("Ticket médio", f"R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col4.metric("Itens vendidos", f"{qtd_itens}")

st.divider()

# Gráficos
vendas_mes = df_filtrado[df_filtrado["status"] != "Cancelado"].groupby("mes", as_index=False)["valor_total"].sum()
vendas_categoria = df_filtrado[df_filtrado["status"] != "Cancelado"].groupby("categoria", as_index=False)["valor_total"].sum()
vendas_estado = df_filtrado[df_filtrado["status"] != "Cancelado"].groupby("estado", as_index=False)["valor_total"].sum()
status_pedidos = df_filtrado.groupby("status", as_index=False)["id_pedido"].count()

col5, col6 = st.columns(2)
with col5:
    st.subheader("Faturamento por mês")
    fig = px.line(vendas_mes, x="mes", y="valor_total", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("Faturamento por categoria")
    fig = px.bar(vendas_categoria, x="categoria", y="valor_total", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

col7, col8 = st.columns(2)
with col7:
    st.subheader("Faturamento por estado")
    fig = px.bar(vendas_estado, x="estado", y="valor_total", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

with col8:
    st.subheader("Status dos pedidos")
    fig = px.pie(status_pedidos, names="status", values="id_pedido")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Base tratada")
st.dataframe(df_filtrado, use_container_width=True)

st.subheader("Conclusão da análise")
st.write("""
Com base nos dados analisados, é possível identificar o faturamento por período, as categorias de maior desempenho,
os estados com maior volume de vendas e a proporção de pedidos entregues ou cancelados. Essas informações auxiliam
na tomada de decisão, permitindo que a empresa acompanhe seus principais indicadores e identifique oportunidades
de melhoria nas vendas e no atendimento ao cliente.
""")