import streamlit as st
from groq import Groq

st.title("⚡ ACTIVE ZERO CLOUD")
st.write("Conectado diretamente de Mesquita/RJ")

if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    prompt = st.text_input("Comando para o Zero:")
    if st.button("Executar"):
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        st.success(chat.choices[0].message.content)
else:
    st.error("Chave da Groq não configurada nos Secrets!")
