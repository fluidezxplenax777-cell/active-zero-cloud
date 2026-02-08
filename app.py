import streamlit as st
from groq import Groq

# Configuração da Página
st.set_page_config(page_title="Active Zero", page_icon="⚡")
st.title("⚡ ACTIVE ZERO CLOUD")
st.write("Conectado diretamente de Mesquita/RJ")

# Inicializa o cliente
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Chave API não encontrada nos Secrets!")
    st.stop()

# Campo de entrada
prompt = st.text_input("Comando para o Zero:", placeholder="Digite sua ordem aqui...")

# Trava de segurança: Usando o modelo atualizado de 2026
if prompt:
    try:
        with st.spinner("Processando com Llama 3.1..."):
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant", # MOTOR ATUALIZADO
            )
            st.markdown("### Resposta:")
            st.write(chat.choices[0].message.content)
    except Exception as e:
        st.error(f"Erro na ignição: {e}")
else:
    st.info("Aguardando coordenadas para execução...")
