import streamlit as st
import streamlit_authenticator as stauth



st.set_page_config(layout="wide", page_title="UFRJ-CCBI")



senhas_criptografadas = stauth.Hasher(["123456", "123123", "333333"]).generate()


#senhas_criptografadas = ["123456", "123123", "333333"]

credenciais = {"usernames": {
    "lira@gmail.com": {"name": "Lira", "password": senhas_criptografadas[0]},
    "alon@gmail.com": {"name": "Alon", "password": senhas_criptografadas[1]},
    "amanda@gmail.com": {"name": "Amanda", "password": senhas_criptografadas[2]}
}}

authenticator = stauth.Authenticate(credenciais, "credenciais_TIC", "fsyfus%$67fs76AH7", cookie_expiry_days=1)


def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao==True:
        return {"nome": nome, "username": username}
    elif status_autenticacao == False:
        st.error("Combinação de usuário e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")

def logout(authenticator):
      authenticator.logout('Logout', 'sidebar')


# autenticar o usuario
dados_usuario = autenticar_usuario(authenticator)



if dados_usuario:
    st.session_state.login = dados_usuario["nome"]
    #st.session_state.authenticator=authenticator
    pg=st.navigation(
            {
               " Home " :[st.Page("Home.py",title="Home")],
               " Dashboards " : [st.Page("sei.py",title=" SEI"),st.Page("pr4.py",title=" PR4"),st.Page("osticket.py",title=" Ticket")],
               " Relatórios " : [st.Page("sei_rel.py",title=" SEI")],
               "✖ Sair ": [st.Page(logout(authenticator),title=" Sair",default=False)] 
               



            })
    pg.run()


 

 

