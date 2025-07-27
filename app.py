import time
import requests
import streamlit as st

def buscar_id(url,id):
    endpoint = f"https://jsonplaceholder.typicode.com/{url}/{id}"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        type(response.json())
        dados = st.write(response.json())
        return dados


st.image("https://www3.ft.unicamp.br/sites/default/files/styles/large/public/si3.jpg?itok=iV7NWzMk", caption="SI3 - Sistema Integrado de Informações Institucionais da Unicamp")

url = st.text_input("Digite url desejado: ", key="dados")
id = st.text_input("Digite o id: ", key="id")
botao = st.button("Pesquisar", key="botao")

if botao:
    if url and id:
        with st.spinner("Buscando..."):
            time.sleep(4)
        buscar_id(url, id)
    else:
        st.error("Por favor, preencha todos os campos.")
    
    
    
        

        


        
    