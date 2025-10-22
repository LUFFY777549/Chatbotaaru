import google.generativeai as genai
from ChatBot.aaru_gemini import AaruGemini

chatbot_api = AaruGemini(api_key="AIzaSyCmZYuxe4JeEbGURuJa6jPoQNvt677tp0E")  # Replace with your real key
class AaruGemini:
    SYSTEM_PROMPT = (
        "You are Umaru, A smart AI girlfriend..."
    )

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def ask_question(self, message: str) -> str:
        try:
            prompt = f"{self.SYSTEM_PROMPT}\nUser: {message}"
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"❖ Umaru got an error: {str(e)}"
