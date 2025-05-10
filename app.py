import streamlit as st
from ollama_utils import generate_reply

st.set_page_config(page_title="Local Chatbot", page_icon="🤖")

st.title("🧠 Chat with Your Local LLM")
st.caption("Running locally via Ollama")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask something...")

if user_input:
    reply = generate_reply(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", reply))

for sender, msg in st.session_state.history:
    with st.chat_message(sender):
        st.markdown(msg)
