import streamlit as st
st.title("AI Resume Analyzer")
st.write("Paste your resume text to get its proper analysis!")
resume_text= st.text_area("Paste your resume text here: ",height=250)
if st.button("Analyze Resume"):
    st.write("Button Clicked")
