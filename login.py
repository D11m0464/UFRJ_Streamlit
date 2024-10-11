import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import bcrypt

senhas_criptografadas = [bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() for password in ['123456', '234567', '345678']]

credenciais = {"usernames": {
    "lira@gmail.com": {"name": "Lira", "password": senhas_criptografadas[0]},
    "alon@gmail.com": {"name": "Alon", "password": senhas_criptografadas[1]},
    "amanda@gmail.com": {"name": "Amanda", "password": senhas_criptografadas[2]},
}}

authenticator = stauth.Authenticate(credenciais, "credenciais_hashco", "fsyfus%$67fs76AH7", cookie_expiry_days=30)

def autenticar_usuario(authenticator):
    resultado_login = authenticator.login()


    # Verificar se o resultado não é None e contém três elementos
  # Verificar se o resultado não é None e contém três elementos
    if resultado_login is not None:
        nome, status_autenticacao, username = resultado_login


        if status_autenticacao:
            return {'nome': nome, 'username': username}
        elif status_autenticacao == False:
            st.error('Combinação de usuário e senha inválido')
        else:
            st.error('Preencha o formulário para fazer o login')
    else:
        st.error('Erro no processo de login, tente novamente.')
        return None

def logout(authenticator):
    authenticator.logout()


# autenticar o usuario
dados_usuario = autenticar_usuario(authenticator)

if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela

    base = carregar_dados()

    st.title("Hash&Co")
    st.write("Bem vindo, Fulano")
    st.table(base.head(10))