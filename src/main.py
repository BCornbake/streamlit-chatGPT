import os
import openai
import streamlit as st

API_KEY = os.getenv('OPENAI_API_KEY')
API_BASE = os.getenv('OPENAI_API_BASE')
openai.api_key = API_KEY
openai.api_base = API_BASE
openai.api_type = 'azure'
openai.api_version = '2023-07-01-preview'


st.title("ChatGPT 问答机器人")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-35-turbo-16k"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = openai.ChatCompletion.create(
            engine=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        full_response = response["choices"][0]["message"]["content"]
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
