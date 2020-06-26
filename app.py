import streamlit as st

st.title('Título')
st.header('Isto é um cabeçalho')
st.subheader('Isto é um subcabeçalho')
st.text('Isto é um texto')
st.markdown('Isto é um markdown')

st.success('Sucesso')
st.info('Informação')
st.warning('Aviso')
st.error('Erro')

st.write('Texto')
st.write(range(10))



if st.checkbox('Exibir código'):
    st.text('Exibindo código 1')

if st.checkbox('Exibir código 2'):
    st.text('Exibindo código 2')

#Botões rádio
status = st.radio('Qual é o status?',('Ativo', 'Inativo'))

if status == 'Ativo':
    st.success('Você está ativo')
else:
    st.warning('Você está inativo')


#Caixa de seleção
ocupacao = st.selectbox('Qual é a sua ocupação?', ['Data Scientist', 'Programador', 'Engenheiro'])
st.write('Você selecionou a ocupação',ocupacao)


#Multiseleção
cidade = st.multiselect('Onde você mora?', ('São Paulo', 'Belo Horizonte', 'Rio de Janeiro'))
st.write('Você selecionou',len(cidade),'cidade(s)')


#Slider
escala = st.slider('Numa escala de 0 a 5, quanto você está satisfeito?',0,5)

#Botão
st.button('Exibir código')

if st.button('Exibir 2'):
    st.text('Ver diferença')


#Text input
nome = st.text_input('Digite seu nome')
if st.button('Submeter'):
    result = nome.title()
    st.success(result)


#Mostrar código
st.code('import numpy as np')

#Exibir código e comentário
with st.echo():
    #Isso também vai exibir o comentário
    import pandas as pd 
    df = pd.DataFrame()


#PANDAS
import pandas as pd 
file = st.file_uploader('Escolha um arquivo')
if file is not None:
    slider = st.slider('Quantas linhas você deseja visualizar?',1,100)
    df = pd.read_csv(file)
    st.dataframe(df.head(slider))
    st.markdown('TABLE')
    st.table(df.head(slider))
    st.markdown('Colunas')
    st.write(df.columns)
    st.table(df.groupby('Species')['PetalWidthCm'].mean())

import streamlit as st
import pandas as pd
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.title('AceleraDev Data Science')
    st.subheader('Semana 2 - Pré-processamento de Dados em Python')
    st.image('https://media.giphy.com/media/KyBX9ektgXWve/giphy.gif', width=200)
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        st.subheader('Analisando os dados')
        df = pd.read_csv(file)
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        st.markdown('**Visualizando o dataframe**')
        number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
        st.dataframe(df.head(number))
        st.markdown('**Nome das colunas:**')
        st.markdown(list(df.columns))
        exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
        st.markdown('**Contagem dos tipos de dados:**')
        st.write(exploracao.tipos.value_counts())
        st.markdown('**Nomes das colunas do tipo int64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))
        st.markdown('**Nomes das colunas do tipo float64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))
        st.markdown('**Nomes das colunas do tipo object:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))
        st.markdown('**Tabela com coluna e percentual de dados faltantes :**')
        st.table(exploracao[exploracao['NA #'] != 0][['tipos', 'NA %']])
        st.subheader('Inputaçao de dados númericos :')
        percentual = st.slider('Escolha o limite de percentual faltante limite para as colunas vocë deseja inputar os dados', min_value=0, max_value=100)
        lista_colunas = list(exploracao[exploracao['NA %']  < percentual]['nomes'])
        select_method = st.radio('Escolha um metodo abaixo :', ('Média', 'Mediana'))
        st.markdown('Você selecionou : ' +str(select_method))
        if select_method == 'Média':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)
        if select_method == 'Mediana':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)


if __name__ == '__main__':
	main()