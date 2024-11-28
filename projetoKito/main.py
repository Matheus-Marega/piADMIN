import streamlit as st
from paginas.auth_adm import auth_admin
from paginas.dashboard_principal import mostrar_relatorio_semanal
from paginas.sugestao_melhoria import sug_melhoria2


def main():

    st.set_page_config(
    page_title="Pagina de Login",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )

    authenticator =  auth_admin()
    authenticator.login()

    if st.session_state["authentication_status"] is False:
        st.error("Usuario/Senha invalido")

    elif st.session_state["authentication_status"] is None:
        st.warning("Por favor, Utilize se usuario e senha")

    elif st.session_state["authentication_status"] is True:
        opcao = st.sidebar.selectbox(
            "O que você deseja Visualizar?",
            ("Pagina Incial", "Sugestoes de Melhoria/Feedback", "Relatorio Semanal")
        )

        if opcao == "Pagina Incial":
            mostrar_relatorio_semanal()
        elif opcao == "Sugestoes de Melhoria/Feedback":
            sug_melhoria2()

        elif opcao == "Relatorio Semanal":
            st.title("Teste3")


if __name__ == "__main__":
    main()