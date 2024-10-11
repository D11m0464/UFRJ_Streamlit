

import streamlit as st  

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('PR4', options=['CPST','Permuta','Pessoal em Números'])


if relatorio == 'CPST':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/0d206763-0646-46f6-a1a9-c886e676a842', width=1500,height=1200,scrolling=True)


if relatorio == 'Permuta':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/85bc949b-d76a-402a-b0c5-be3c6ec304ab', width=1500,height=1200,scrolling=True)


if relatorio == 'Pessoal em Números':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/27537151-f3f5-44d7-898c-045ea8d7e229', width=1500,height=1200,scrolling=True)

