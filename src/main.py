import streamlit as st
from decouple import config
import openai
import os

response = False
prompt_tokens = 0
completion_tokes = 0
total_tokens_used = 0
cost_of_response = 0

API_KEY = os.getenv('OPENAI_API_KEY')
API_BASE = os.getenv('OPENAI_API_BASE')
openai.api_key = API_KEY
openai.api_base = API_BASE
openai.api_type = 'azure'
openai.api_version = '2023-07-01-preview'


def make_request(question_input: str):
    response = openai.ChatCompletion.create(
        engine="gptdemo",
        messages=[
            {"role": "system", "content": f"{question_input}"},
        ]
    )
    return response


st.header("ChatGPT 问答机器人")

st.markdown("""---""")

question_input = st.text_input("输入问题")
rerun_button = st.button("提交")

st.markdown("""---""")

if question_input:
    response = make_request(question_input)
else:
    pass

if rerun_button:
    response = make_request(question_input)
else:
    pass

if response:
    st.write("Response:")
    st.write(response["choices"][0]["message"]["content"])
else:
    pass

