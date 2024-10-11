import streamlit as st 
 

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('Relatórios', options=['Protocolos_Abertos','Assunto não disponibilizado','Estatistico da Unidade','Processos Gerados'])


if relatorio == 'Protocolos_Abertos':
       container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

       container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/question/c43cac71-fa21-4577-98c6-be88b8895c88', width=1500,height=1200,scrolling=True) 
 
 

