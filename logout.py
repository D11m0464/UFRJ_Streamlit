
from main import logout
import streamlit as st  





input = st.text_input("Deseja realmente Sair (S/N)", value=None, max_chars=1)


input =input.lower(input)

if(input == 'S'): 
    logout(st.session_state.authenticator)


