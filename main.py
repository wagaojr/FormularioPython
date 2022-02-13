import streamlit as st;
import pandas as pd 
import csv
from IPython.display import display

global dados
dados = pd.read_csv('tabela.csv')

st.title("ProMove")

with st.container():

   with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira seu nome", key=str)
    input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Qual o seu vínculo com a UFRJ?",["Estudante","Professor","Servidor","Pesquisador CLT","Funcionário","Ex Aluno"])
    input_local = st.selectbox("Onde trabalha/estuda na UFRJ?",["CCMN","CT","Letras","CCS"])
    input_pergunta1 = st.selectbox("Você sente dificuldade nos estudos?", ["Sim","Não"])
    input_pergunta2 = st.selectbox("Usaria um aplicativo específico da UFRJ para estudos?", ["Sim","Não"])
    input_button_submit = st.form_submit_button("Enviar")


st.sidebar.header('Escolha um gráfico')
input_grafico1 = st.sidebar.button('Gráfico 1')
input_grafico2 = st.sidebar.button('Gráfico 2')

if input_button_submit:
    with open('tabela.csv', 'w', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow([input_name , input_age , input_occupation , input_local , input_pergunta1 , input_pergunta2])
        dados = pd.read_csv('tabela.csv')
        st.write("Suas respostas foram salvas!")


if input_grafico1:
     pass

if input_grafico2:
     pass