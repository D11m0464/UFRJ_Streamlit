import streamlit as st  

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('OSTicket', options=['Gerencial','Análise Histórico'])


if relatorio == 'Gerencial':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/6dc30224-ffd8-428a-b1d8-d6dfcb5d6c8f', width=1500,height=1200,scrolling=True)


if relatorio == 'Análise Histórico':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/4066169d-5335-41c3-a420-7ff2da59d8d7', width=1500,height=1200,scrolling=True)

