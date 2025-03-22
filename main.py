import streamlit as st
from serach import run_crew


st.title("Web RAG")

url = st.text_input("Digite a url que deseja extrair informações?", "https://www.uol.com.br/")
question = st.text_input("Faça uma pergunta sobre o site.", "Quis as princiapis notícias")



if st.button("Responder"):
    if url and question:

        with st.spinner("Processando..."):
            result = run_crew(url, question)
    
        st.success("Feito!")
        st.markdown(result.raw)
    else:
        st.error("Por favor, digite alguma url.")
