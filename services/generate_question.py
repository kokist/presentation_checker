import openai
import base64
import time
import os
from pdf2image import convert_from_path
from io import BytesIO

# OpenAI APIキーの設定
# openai.api_key="OPENAI_API_KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Popplerのバイナリが配置されたディレクトリを環境変数に追加
poppler_path = os.path.join(os.path.dirname(__file__), '..', 'third_party', 'poppler', 'Library', 'bin')
os.environ['PATH'] += os.pathsep + poppler_path

# PDFをメモリ内で画像に変換し、Base64形式にエンコードする関数
def pdf_to_base64_images(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    base64_images = []
    for image in images:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        base64_images.append(base64_image)

    return base64_images

def generate_questions_from_pdf(pdf_path):
    base64_images = pdf_to_base64_images(pdf_path)
    questions = []
    for base64_image in base64_images:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professor in the field of artificial intelligence. You will ask a wide range of questions, from simple to highly difficult ones."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": 
                            """
                            Please generate only three questions from the image and output them as a numbered list. 
                            Output example
                            1. Why do you choose this model?
                            2. What is the main purpose of this model?
                            3. What is the pourpose of this experments?
                            """},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300,
            temperature=0.8,
            top_p=0.9
        )
        questions.append(response.choices[0].message.content + "\n")
        time.sleep(2)

    return questions

if __name__ == "__main__":
    # テスト用のPDFファイルのパスを指定
    pdf_path = "../samples/sample.pdf"
    questions = generate_questions_from_pdf(pdf_path)

    # 質問を箇条書きで表示
    for question in questions:
        print(f"{question}")