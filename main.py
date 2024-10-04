import streamlit as st

 





#st.markdown(
#    """
#    <style>
#    .reportview-container {
#        background: url('C:\Users\carlos santos\Desktop\UFRJ-DEMO-Streamlit\imagem\sgtic.png');
#    }
#   </style>
#    """,
#    unsafe_allow_html=True
#)

st.set_page_config(layout="wide")


pg=st.navigation(
{
   " Home " :[st.Page("Home.py",title="Home")],
   " Dashboards " : [st.Page("sei.py",title=" SEI"),st.Page("pr4.py",title=" PR4"),st.Page("osticket.py",title=" Ticket")],
   " Relatórios " : [st.Page("sei_rel.py",title=" SEI")],
   "✖ Sair ": [] 
   



})
pg.run()