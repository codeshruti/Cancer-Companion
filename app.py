# The following is a simulation of a chatbot that can help cancer patients with their queries.
# Run the code with : streamlit run app.py

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_openai_response(prompt):
    """Get a response from OpenAI's API."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an Oncology specialist and should be empathetic with the user. Give suitable references and resources to support your answers when needed."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error querying LLM: {e}")
        return None
    
st.title("🩺 Cancer Companion")
st.write("### An empathetic Chatbot to support cancer patients")

user_input = st.text_area("Ask me all your cancer-related questions")

if st.button("Get Answer"):
    if user_input:
        with st.spinner("Thinking..."):
            ai_response = get_openai_response(f"{user_input}\n\nAnswer the user questions in a very easy-to-understand manner and be reassuring. Provide the user with the necessary information to help them clear their queries.")
            st.markdown(ai_response)
    else:
        st.warning("Please enter a question!")

