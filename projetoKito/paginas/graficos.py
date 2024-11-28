import streamlit as st
import pandas as pd
import plotly.express as px

# Dados simulados para os gráficos
genero_infra_data = pd.DataFrame({
    'Gênero': ['Masculino', 'Feminino'],
    'Infraestrutura Média': [3.8, 4.2],
    'Limpeza Média': [4.0, 4.3]
})

frequencia_seg_limpeza_data = pd.DataFrame({
    'Frequência': ['Diariamente', 'Semanalmente', 'Quinzenalmente', 'Mensalmente', 'Raramente'],
    'Segurança Média': [4.3, 4.0, 3.7, 3.5, 3.2],
    'Limpeza Média': [4.1, 4.0, 3.6, 3.4, 3.3]
})

sugestoes_produtos_data = pd.DataFrame({
    'Sugestões de Melhoria': ['Mais segurança', 'Mais opções de lojas', 'Mais vagas no estacionamento', 'Melhor sinalização'],
    'Frequência': [15, 25, 10, 8],
    'Produtos/Serviços Faltando': [20, 30, 5, 7]
})

variedade_satisfacao_data = pd.DataFrame({
    'Variedade de Lojas': [3, 4, 5, 2, 4.5],
    'Satisfação Geral': [3.8, 4.2, 4.5, 3.0, 4.3]
})

segmento_sugestoes_data = pd.DataFrame({
    'Data de Visita': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04'],
    'Roupas': [5, 7, 6, 4],
    'Eletrônicos': [3, 5, 4, 2],
    'Alimentação': [8, 9, 6, 7],
    'Livraria': [2, 3, 3, 2]
}).set_index('Data de Visita')


# Gráfico 1 - Gênero x Avaliação de Infraestrutura e Limpeza (Matplotlib)
def grafico1():
    st.subheader("Avaliação de Infraestrutura e Limpeza por Gênero")
    fig1 = px.bar(
        genero_infra_data.melt(id_vars='Gênero', var_name='Categoria', value_name='Média'),
        x='Gênero', y='Média', color='Categoria',
        barmode='group', color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig1.update_layout(xaxis_title=None, yaxis_title="Média de Avaliação")
    st.plotly_chart(fig1)

def grafico2():
    st.subheader("Frequência de Visitas x Nota Média de Segurança e Limpeza")
    fig2 = px.line(
        frequencia_seg_limpeza_data.melt(id_vars='Frequência', var_name='Categoria', value_name='Nota Média'),
        x='Frequência', y='Nota Média', color='Categoria', markers=True,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig2.update_layout(xaxis_title="Frequência de Visitas", yaxis_title="Nota Média")
    st.plotly_chart(fig2)

def grafico3():
    st.subheader("Sugestões de Melhoria x Produtos/Serviços em Falta")
    fig3 = px.bar(
        sugestoes_produtos_data,
        x='Sugestões de Melhoria', y=['Frequência', 'Produtos/Serviços Faltando'],
        title="Distribuição de Sugestões e Produtos/Serviços em Falta",
        labels={'value': 'Número de Menções', 'variable': 'Categoria'},
        barmode='stack', text_auto=True, color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig3)

def grafico4():
    st.subheader("Variedade de Lojas x Satisfação Geral")
    fig4 = px.scatter(
        variedade_satisfacao_data,
        x='Variedade de Lojas', y='Satisfação Geral',
        trendline='ols', color_discrete_sequence=['teal'],
        labels={'Variedade de Lojas': "Nota - Variedade de Lojas", 'Satisfação Geral': "Nota - Satisfação Geral"}
    )
    fig4.update_traces(marker=dict(size=12))
    st.plotly_chart(fig4)

def grafico5():
    st.subheader("Segmentos Mais Frequentados por Data de Visita")
    fig5 = px.imshow(
        segmento_sugestoes_data,
        labels={'x': "Segmentos", 'y': "Data de Visita", 'color': "Frequência"},
        title="Frequência de Visitas por Segmento"
    )
    st.plotly_chart(fig5)