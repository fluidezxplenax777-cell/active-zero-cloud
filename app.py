import streamlit as st
from groq import Groq

# Configuração da Página
st.set_page_config(page_title="Active Zero", page_icon="⚡")
st.title("⚡ ACTIVE ZERO CLOUD")
st.write("Conectado diretamente de Mesquita/RJ")

# Inicializa o cliente com a chave dos Secrets
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Chave API não encontrada nos Secrets!")
    st.stop()

# Campo de entrada
prompt = st.text_input("Comando para o Zero:", placeholder="Digite sua ordem aqui...")

# Trava de segurança: só executa se houver texto
if prompt:
    try:
        with st.spinner("Processando em Mesquita..."):
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )
            st.markdown("### Resposta:")
            st.write(chat.choices[0].message.content)
    except Exception as e:
        st.error(f"Erro na ignição: {e}")
else:
    st.info("Aguardando coordenadas para execução...")
