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

url = st.text_input("Digite o id da pessoa: ", key="dados")
id = st.text_input("Digite o id: ", key="id")
botao = st.button("Pesquisar", key="botao")

if botao:
    buscar = buscar_id(url,id)
    
else:
    st.error("Por favor, digite um id válido.")

# try:
#     if botao:
#         buscar_id(dados)
        
# except requests.exceptions.RequestException as e:
#     st.error(f"Erro ao buscar dados: {e}")
        
    