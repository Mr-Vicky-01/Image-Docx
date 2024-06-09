import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class Model:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
    def get_response(self, image):
        prompt = """You are an intelligent document creator. Could you please extract the words from the given screenshot and provide me document text that matches exact screenshot font and look
        important note: if the screenshot not contain any text means you must say 'please upload a valid screenshot.'"""
        img = Image.open(image)
        response = self.model.generate_content([prompt, img]) 
        return response.text