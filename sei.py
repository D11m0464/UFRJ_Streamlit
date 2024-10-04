import streamlit as st  

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('SEI EM  NÚMEROS', options=['Dados Gerais','Tempo Médio Permanência'])


if relatorio == 'Dados Gerais':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/2e2825a4-0f47-46a7-9cfd-84b2da1c2929', width=1500,height=1200,scrolling=True)


if relatorio == 'Tempo Médio Permanência':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/a3901571-3b68-4a02-9989-7f84d55c3580', width=1500,height=1200,scrolling=True)



#import streamlit.components as componente


#componente.
