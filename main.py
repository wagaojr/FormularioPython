import streamlit as st;
from serviços.dados import Dados
import serviços.database

st.title("ProMove")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira seu nome")
    input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Qual o seu vínculo com a UFRJ?",["Estudante","Professor","Servidor","Pesquisador CLT","Funcionário","Ex Aluno"])
    input_local = st.selectbox("Onde trabalha/estuda na UFRJ?",["CCMN","CT","Letras","CCS"])
    input_pergunta1 = st.selectbox("Você sente dificuldade nos estudos?", ["Sim","Não"])
    input_pergunta2 = st.selectbox("Usaria um aplicativo específico da UFRJ para estudos?", ["Sim","Não"])
    input_button_submit = st.form_submit_button("Enviar")


if input_button_submit:
    Dados.insertDado(input_name,input_age, input_occupation, input_local, input_pergunta1, input_pergunta2)