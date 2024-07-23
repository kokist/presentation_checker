import streamlit as st

def home():
    # 言語選択ドロップダウンをページの最上部に配置
    language = st.selectbox('Choose your language:', ['English', '日本語'])

    if language == 'English':
        st.warning('This deploy version does not have the querying feature powered by GPT. If you want to try the querying feature, please do a local build.')
        st.title("Presentation Checker")
        st.header("Welcome to the Presentation Checker")
        st.write("""
            This application helps you to extract speeches from PowerPoint files and check them. 
            Please navigate to the 'PPT to sound' page from the sidebar to start using the application.
        """)
        
        col1, col2 = st.columns(2)

        with col1:
            st.header("PPT to Sound")
            st.image("images/ppt2speech.webp")

        with col2:
            st.header("Q&A with GPT")
            st.image("images/qa_gpt.webp")

    elif language == '日本語':
        st.warning('このデプロイのバージョンにはGPTによる質疑対策の機能がありません。質疑対策の機能を試したい場合は、localでのbuildを行ってください。')
        st.title("プレゼンチェッカー")
        st.header("プレゼンチェッカーへようこそ")
        st.write("""
            このアプリケーションは、PowerPointファイルからスピーチを抽出し、音声化することにより，発音やアクセントをチェックするアプリです。
            アプリを使用するには、「PPT to sound」ページに進んでください。
        """)
        
        col1, col2 = st.columns(2)

        with col1:
            st.header("PPT to Speech")
            st.image("images/ppt2speech.webp")

        with col2:
            st.header("Q&A with GPT")
            st.image("images/qa_gpt.webp")
