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


lista = ['Mais assentos nas áreas comuns: Seria ótimo ter mais bancos ou áreas de descanso em locais estratégicos.','Melhoria nos banheiros: "Os banheiros poderiam ser mais limpos e modernos, com espelhos e iluminação melhores."','Melhor climatização: "O ar-condicionado não é suficiente em dias muito quentes. Precisa ser mais eficiente."','Atendimento mais amigável: "O pessoal do balcão de informações poderia ser mais atencioso."']
def sug_melhoria():

    for sugestao in lista:
        st.text_area(f"{sugestao}")


def sug_melhoria2():
    col1, col2 = st.columns(2)
    


    with col1:
        grafico3()
    with col2:
        sug_melhoria()