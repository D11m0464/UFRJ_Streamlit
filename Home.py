import streamlit as st



coluna_imagem,coluna_titulo=st.columns([1,1.5],vertical_alignment='top')
coluna_imagem.header(f'Bem vindo, {st.session_state.login}')
coluna_titulo.title(" :gray[Centro de Competencia de BI]")
coluna_titulo.title(" :gray[Divisão de Gestão de Dados]")
container = coluna_imagem.container(border=False)
container.image("imagem/sgtic.png")
 













