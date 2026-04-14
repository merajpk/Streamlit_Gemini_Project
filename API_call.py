from google import genai
import os
from dotenv import load_dotenv
from PIL import Image
from gtts import gTTS
import io
import streamlit as st

# Loading the envirment variable

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#client
client = genai.Client(api_key=my_api_key)


#Note Generator function
def note_generator(images):
    prompt = "100 word markdown summary of all images. Format: #title, -points, **bold**, >quote. Extract only notes content."
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images , prompt]
    )

    return response.text

def audio_transcription(text):
    spech = gTTS(text , lang='en' , slow=False)

    audio_buffer = io.BytesIO()
    spech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(img , difficulty):
    prompt = f"Generate 5 Quizzes based on {difficulty} difficulty and make a correct ans part in below of all"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img, prompt]
    )

    return response.text

# def correct_ans(quiz_text):
#     prompt = f"Extract only the correct answers from this quiz. Return as a numbered list:\n\n{quiz_text}"
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=[prompt]
#     )
#     return response.text