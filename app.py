import streamlit as st
import google.generativeai as genai
import base64
import os
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

st.set_page_config(
    page_title="Data Science Tutor",
    page_icon="images/tutorss.png",
    layout='centered',
    initial_sidebar_state="expanded")
#st.image("images/tutor.jpg")
 
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=""" You are helpful AI, and expert in data science field
and Knows each and every topic regarding machine learning,
deep learning, natural language processing, generative ai, bert, encoder-decoder architecture, statistics, probability,
and every machine learning and deep learning algorithms with examples.
You are a data science tutor who answers the question asked related to data science field
""")

st.header("Data Science - AI Tutor")

if 'memory' not in st.session_state:
    st.session_state['memory'] = []

# Initializing the chat object
chat = model.start_chat(history=st.session_state['memory'])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message('user').write(user_prompt)
    response = chat.send_message(user_prompt, stream=True)
    response.resolve()
    st.chat_message('ai').write(response.text, end='')
    st.session_state['memory'] = chat.history
## Footer Follow code

st.sidebar.image("images/tutor.jpg")
st.sidebar.markdown("<h3>If you like this app. You can follow me on</h3>", unsafe_allow_html=True)

linkedin, github,discord,m,n = st.sidebar.columns(5)
with linkedin:
    st.markdown(
        """<a href="https://www.linkedin.com/in/sanchit-singla/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with github:
    st.markdown(
        """<a href="https://github.com/sa-1-2/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/github.PNG", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with discord:
    st.markdown(
        """<a href="https://discordapp.com/users/753842907966079046">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/discord.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)
   
st.sidebar.write("")
st.sidebar.write("BY: Sanchit Singla")

st.sidebar.write("")
st.sidebar.write()
email_address = "sanchitsingla1403@gmail.com"
st.sidebar.markdown("""<p>You can report Bug at Email</p><a href="mailto:{}"><img src="data:image/png;base64,{}" width="40"><p>sanchitsingla1403@gmail.com</p>
        </a>""".format(email_address, base64.b64encode(open("images/gmail.png", "rb").read()).decode()), unsafe_allow_html=True)
