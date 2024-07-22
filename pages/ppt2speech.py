import streamlit as st
import io
import asyncio
from services.extract_ppt import extract_ppt
from services.text2speech import text_to_mp3
from utils.sidebar_setup import setup_sidebar

def display():
    setup_sidebar()

    st.title('PPT to Speech Extractor')
    st.write("""
    This app converts speaker notes from PowerPoint files into speech. 
    """)
    uploaded_file = st.file_uploader("Upload your PowerPoint file here", type=["pptx"])
    
    if uploaded_file is not None:
        speeches = extract_ppt(io.BytesIO(uploaded_file.getvalue()))
        if speeches:
            all_speeches = '\n'.join(speeches)  # すべてのスピーチを1つのテキストに結合

            # Convert to Speech ボタンをここに配置
            convert_clicked = st.button('Convert to Speech')
            # ボタンがクリックされた後の処理
            if convert_clicked:
                try:
                    filename = asyncio.run(text_to_mp3(all_speeches))
                    # st.success('Audio file created successfully: {}'.format(filename))
                    st.success('Audio file created successfully')
                    st.audio(filename)
                except RuntimeError as e:
                    st.error(f"Error converting text to speech: {e}")

            st.write("Extracted Speeches:")
            for i, speech in enumerate(speeches, 1):
                st.markdown(f"**Slide {i}:**\n\n{speech}")
                
        else:
            st.warning("No speeches found in the uploaded PowerPoint.")

if __name__ == "__main__":
    display()
