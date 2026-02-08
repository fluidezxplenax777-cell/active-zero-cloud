import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Active Zero", page_icon="⚡", layout="centered")
st.title("⚡ ACTIVE ZERO CLOUD")
st.caption(f"Mesquita/RJ | Sistema Operacional | {datetime.now().strftime('%d/%m/%Y')}")

# --- MEMÓRIA BLINDADA (JSON) ---
MEMORIA_FILE = "memoria_zero.json"

def carregar():
    if os.path.exists(MEMORIA_FILE):
        try:
            with open(MEMORIA_FILE, "r") as f:
                return json.load(f)
        except: return []
    return []

def salvar():
    with open(MEMORIA_FILE, "w") as f:
        json.dump(st.session_state.messages, f)

if "messages" not in st.session_state:
    st.session_state.messages = carregar()

# --- MOTOR ---
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("⚠️ Chave de Segurança Ausente!")
    st.stop()

# --- INTERFACE ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Comando para o Zero..."):
    # Salva User
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta IA
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                model="llama-3.1-8b-instant",
                stream=True,
            )
            response = st.write_stream(stream)
            
            # Salva IA
            st.session_state.messages.append({"role": "assistant", "content": response})
            salvar()
        except Exception as e:
            st.error(f"Erro no Motor: {e}")

# Menu Lateral
with st.sidebar:
    if st.button("🗑️ Limpar Conversa"):
        if os.path.exists(MEMORIA_FILE): os.remove(MEMORIA_FILE)
        st.session_state.messages = []
        st.rerun()
