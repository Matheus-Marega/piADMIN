import streamlit as st
from paginas.graficos import grafico1, grafico2, grafico3, grafico5,grafico4

def mostrar_relatorio_semanal():
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)


    with col1:
        grafico1()
    with col2:
        grafico2()


    with col3:
        grafico3()
    with col4:
        grafico4()
    with col5:
        grafico5()