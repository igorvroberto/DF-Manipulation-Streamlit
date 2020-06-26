import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from blinker import Signal
import os
import xlrd


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


    st.markdown('Selecione o arquivo **csv** que deseja analisar')
    file  = st.file_uploader('', type = ['csv', 'xls', 'xlsx'])
    st.markdown('Escolha o separador dos dados')
    separador = st.selectbox('',[';', ',', '.'])
    if file is None:
        st.error('Por favor, selecione um arquivo')
    else:
        df=pd.read_csv(file, sep=separador)
        st.success('Arquivo importado com sucesso')

    
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

        st.markdown("**Escolha abaixo o tipo do gráfico que deseja visualizar**")
        graphic_plot = st.selectbox('',['Gráfico de correlação','Gráfico de distribuição'])
        if graphic_plot == 'Gráfico de correlação':
            fig, ax = plt.subplots(figsize=(8, 8))
            sns.heatmap(df.corr(), annot=True)
            st.pyplot()
        elif graphic_plot == 'Gráfico de distribuição':
                option = st.selectbox('Selecione o atributo', df.columns)
                #Para dados categóricos é plotado um gráfico de barras
                if df[option].dtype == object:
                    sns.set_style('darkgrid')
                    fig, ax = plt.subplots(figsize=(8, 8))
                    sns.countplot(x=df[option], data=df)
                    plt.xticks(rotation=90)
                    st.pyplot()  
                #Para dados numéricos é plotado um histograma
                else:
                    sns.distplot(df[option], bins=10)
                    st.pyplot()


if __name__ == "__main__":
    main()