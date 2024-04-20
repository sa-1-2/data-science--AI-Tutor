import streamlit as st
import google.generativeai as genai
import base64

st.set_page_config(
    page_title="Data Science Tutor",
    page_icon="images/tutorss.png",
    layout='centered',
    initial_sidebar_state="expanded")
#st.image("images/tutor.jpg")
 

API_KEY = "AIzaSyAD1ROM_WZ688-WIJ0Y7VNn4x6mWUZWqY0"
genai.configure(api_key = API_KEY)
generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192
        }

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)  

def get_gemini_response(question, prompt, model):
    response = model.generate_content([prompt, question])
    return response.text

prompt = """ You are helpful AI, and expert in data science field
and Knows each and every topic regarding machine learning,
deep learning, natural language processing, generative ai, bert, encoder-decoder architecture, statistics, probability,
and every machine learning and deep learning algorithms with examples.
You are a data science tutor who answers the question asked related to data science field
"""




st.header("Data Science - AI Tutor")
question = st.text_input("Ask your question:", key='input')

submit = st.button("Get Solution")
if submit:
    response = get_gemini_response(question, prompt, model)
    st.write(response)

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
