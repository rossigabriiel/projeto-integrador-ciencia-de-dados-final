# Análise de Vendas em E-commerce - Projeto Integrador

## 1. Descrição do projeto

Este projeto tem como objetivo analisar dados de vendas de um e-commerce, identificando padrões, tendências e indicadores importantes para apoiar a tomada de decisão.

A solução foi desenvolvida em Python, com tratamento de dados utilizando Pandas e visualização por meio de um dashboard interativo no Streamlit.

## 2. Integrantes do grupo

- Gabriel: coordenação geral, validação da entrega e apoio no dashboard.
- Matheus: organização da base de dados.
- Giovanna: análise exploratória dos dados.
- Anderson: tratamento e transformação dos dados.
- Mateus: validação dos indicadores.
- José Eduardo: documentação do projeto.
- Fabio: apoio técnico.
- Nicholas: revisão final.

> Ajustar os nomes conforme os integrantes reais do grupo.

## 3. Tecnologias utilizadas

- Python
- Pandas
- Plotly
- Streamlit
- GitHub
- Streamlit Cloud

## 4. Estrutura do projeto

```text
projeto_integrador_2_fase/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── vendas_ecommerce.csv
└── src/
    └── transformacoes.py
```

## 5. Transformações realizadas nos dados

Foram realizadas as seguintes transformações:

1. Leitura da base de vendas em formato CSV.
2. Conversão da coluna de data para formato de data.
3. Criação da coluna `valor_total`, calculada por quantidade x preço unitário.
4. Criação da coluna `mes`, utilizada para análise temporal.
5. Filtro de pedidos por categoria, estado e status.
6. Separação de pedidos cancelados para cálculo correto do faturamento.

## 6. Indicadores apresentados no dashboard

O dashboard apresenta os seguintes indicadores:

- Total de pedidos.
- Faturamento total.
- Ticket médio.
- Quantidade de itens vendidos.
- Faturamento por mês.
- Faturamento por categoria.
- Faturamento por estado.
- Distribuição dos pedidos por status.
- Tabela com a base tratada.

## 7. Como executar o projeto localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o dashboard:

```bash
streamlit run app.py
```

## 8. Como publicar no Streamlit Cloud

1. Criar um repositório público no GitHub.
2. Enviar todos os arquivos deste projeto para o repositório.
3. Acessar o Streamlit Cloud.
4. Clicar em **New app**.
5. Selecionar o repositório do projeto.
6. Em **Main file path**, informar:

```text
app.py
```

7. Clicar em **Deploy**.

## 9. Link da aplicação publicada

Inserir aqui o link do Streamlit Cloud:

```text
https://seu-link-do-streamlit.streamlit.app
```

## 10. Conclusão

A segunda etapa do projeto foi desenvolvida com foco na execução prática da solução planejada na primeira fase.  
Foram realizadas as transformações dos dados, construção de indicadores, elaboração de visualizações e organização do projeto em repositório GitHub.

O dashboard permite visualizar de forma clara os principais resultados de vendas do e-commerce, facilitando a análise de desempenho por período, categoria, estado e status dos pedidos.