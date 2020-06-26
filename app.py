import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from blinker import Signal
import os
import xlrd


class FileReference:
    def __init__(self, filename):
        self.filename = filename

def hash_file_reference(file_reference):
    filename = file_reference.filename
    return (filename, os.path.getmtime(filename))


def main():

    html_title = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:40px;'>Data Science</p>
    </div>
    """
    st.markdown(html_title, unsafe_allow_html=True)
    html_subtitle = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:20px;'>Manipulação de dataframe com Pandas</p>
    </div>
    """
    st.markdown(html_subtitle, unsafe_allow_html=True)

    html_subtitle = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:15px;'>Selecione a caixa de marcação caso deseje visualizar o código</p>
    </div>
    """
    st.markdown(html_subtitle, unsafe_allow_html=True)

    file  = st.file_uploader('Selecione o arquivo .csv que deseja analisar', type = ["csv", "xls", "xlsx"])
    

    @st.cache(hash_funcs={FileReference: hash_file_reference})
    def try_read_df(data):
        try:
            return pd.read_csv(data)
        except:
            return pd.read_excel(data)
        if file:
            df = try_read_df(file)

    if file is not None:
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

if __name__ == "__main__":
    main()