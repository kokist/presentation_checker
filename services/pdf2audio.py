from services.generate_question import generate_questions_from_pdf
from services.text2speech import text_to_mp3_sync

def generate_questions_and_audio(pdf_path):
    questions = generate_questions_from_pdf(pdf_path)
    audio_files = []
    for question in questions:
        audio_file = text_to_mp3_sync(question)
        with open(audio_file, "rb") as file:
            audio_bytes = file.read()
        audio_files.append(audio_bytes)
    return questions, audio_files
