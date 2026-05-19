import pandas as pd

def transformar_dados(caminho_csv: str) -> pd.DataFrame:
    """
    Função responsável por carregar e transformar a base de vendas.
    """
    df = pd.read_csv(caminho_csv)

    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]
    df["mes"] = df["data_pedido"].dt.to_period("M").astype(str)

    return df