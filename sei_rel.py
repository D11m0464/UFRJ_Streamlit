import streamlit as st  

#st.set_page_config(layout="wide")

coluna_esquerda,coluna_meio,coluna_direita=st.columns([1,1,1])

relatorio=coluna_esquerda.selectbox('Relatórios', options=['Listagem_Protocolos_Abertos','Listagem_SEI_Assuntonaodisponibilizado','Listagem_SEI_EstatisticoUnidade','Listagem_SEI_ProcessosGerados'])


if relatorio == 'Listagem_Protocolos_Abertos':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    #container_dash.container().pa(src='https://ccbi.tic.ufrj.br/pentaho/api/repos/%3Ahome%3Acarloscarvalho%3ASEI%3ARelatorio%3AListagem_Protocolos_Abertos.prpt/viewer', width=1500,height=1200,scrolling=True)


if relatorio == 'Listagem_SEI_Assuntonaodisponibilizado':
    container_dash,container_lateral=st.columns([5,1],gap='small',vertical_alignment='top')

    #container_dash.container()._iframe(src='https://ccbi.tic.ufrj.br/pentaho/api/repos/%3Ahome%3Acarloscarvalho%3ASEI%3ARelatorio%3AListagem_SEI_Assuntonaodisponibilizado.prpt/viewer', width=1500,height=1200,scrolling=True)



#import streamlit.components as componente


#componente.
