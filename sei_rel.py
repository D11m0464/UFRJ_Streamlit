import streamlit as st 
 

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('Relatórios', options=['Protocolos_Abertos','Assunto não disponibilizado','Estatistico da Unidade','Processos Gerados'])


if relatorio == 'Protocolos_Abertos':
       container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

       container_dash.container()._iframe(src='https://dashboard.ccbi.tic.ufrj.br/public/dashboard/2c051ef0-22b4-489d-a7c0-ca1b94df7811', width=1500,height=1200,scrolling=True) 
 


