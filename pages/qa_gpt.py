import streamlit as st
from utils.sidebar_setup import setup_sidebar
import tempfile
from services.pdf2audio import generate_questions_and_audio
import hashlib

def display():
    setup_sidebar()
    st.title("AI-Powered Question Generator from PDF")
    st.write("This app generates questions from the uploaded presentation PDF.")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_bytes = uploaded_file.getvalue()
        pdf_hash = hashlib.md5(pdf_bytes).hexdigest()

        if 'pdf_hash' not in st.session_state or st.session_state['pdf_hash'] != pdf_hash:
            st.session_state['pdf_hash'] = pdf_hash
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(pdf_bytes)
                tmp_file_path = tmp_file.name

            with st.spinner('Generating questions... This may take a few moments.'):
                questions, audio_files = generate_questions_and_audio(tmp_file_path)
                st.session_state['questions'] = questions
                st.session_state['audio_files'] = audio_files

        questions = st.session_state.get('questions', [])
        audio_files = st.session_state.get('audio_files', [])

        st.write("### Generated Questions")
        for i, (question, audio_bytes) in enumerate(zip(questions, audio_files), 1):
            st.audio(audio_bytes, format="audio/mp3")
            checkbox_key = f"question_{i}_visible"
            
            if st.checkbox(f"Show Question {i}", key=checkbox_key):
                st.write(f"#### Question {i}")
                st.write(question)

if __name__ == "__main__":
    display()
