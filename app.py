import os
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2
import streamlit as st

load_dotenv()
api_key= os.getenv("OPENROUTER_API_KEY")

client= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
st.title("AI Resume Analyzer")
st.write("Paste your resume text to get its proper analysis!")

uploaded_file=st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

resume_text= st.text_area("Paste your resume text here: ",height=200)

if st.button("Analyze resume "):

    final_resume_text=""
    if uploaded_file is not None:
        pdf_reader= PyPDF2.PdfReader(uploaded_file)
        final_resume_text=""
        for page in pdf_reader.pages:
            final_resume_text+=page.extract_text()
        
    elif resume_text:
        final_resume_text=resume_text

    else:
        st.warning("Please upload a PDF or paste resume text.")
        st.stop()

    
    with st.spinner("Analyzing the resume..."):
        response= client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                    {"role":"user", "content":"Act like an HR reviewer and assess resume on the basis of stregths, weakness, missing skills and improvemnts. Be consice"},
                    {"role":"user","content":final_resume_text}
                ],
                max_tokens=300
        )
        st.subheader("AI Resume Analyzer Result:")
        st.write(response.choices[0].message.content)
