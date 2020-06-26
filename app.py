import streamlit as st
import pandas as pd
import numpy as np
import base64


st.title("Data Science")
st.subheader("Manipulação de dataframes utilizando a biblioteca Pandas")
st.text("Selecione a caixa de marcação caso deseje ver o código de execução de cada função")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png", width=200)
file  = st.file_uploader("Escolha o arquivo .csv que deseja analisar", type = "csv")
if file is not None:
    st.success("Arquivo importado com êxito")
    df = pd.read_csv(file)

    if st.checkbox("Número de linhas"):
        st.code("df.shape[0]")
    st.markdown(df.shape[0])

    if st.checkbox("Número de colunas"):
        st.code("df.shape[1]")
    st.markdown(df.shape[1])

    if st.checkbox("Nomes das colunas"):
            st.code("df.columns.to_list()")
    st.markdown(df.columns.to_list())

    if st.checkbox("Informações estatísticas das colunas numéricas"):
        st.code("df.describe()")
    st.dataframe(df.describe())

    st.markdown("**Visualizando o dataframe**")
    rows_number = st.slider("Escolha o número de linhas que deseja visualizar", min_value=1, max_value=100)
    st.dataframe(df.head(rows_number))
   
    if st.checkbox("Contagem dos tipos de dados"):
        st.code("df.dtypes")
        st.code("df.dtypes.value_counts()")
    st.write(df.dtypes.value_counts())

    df_numerico = df.select_dtypes(include=['int64', 'float64'])
    if st.checkbox("Nomes das colunas numéricas"):
        st.code("df_numerico = df.select_dtypes(include=['int64', 'float64'])")
        st.code("df_numerico.columns.unique()")
    st.write(df_numerico.columns.unique())

    df_categorico = df.select_dtypes(include=["object"])
    if st.checkbox("Nomes das colunas categóricas"):
        st.code("df_categorico = df.select_dtypes(include=['object'])")
        st.code("df_categorico.columns.unique()")
    st.write(df_categorico.columns.unique()) 
    