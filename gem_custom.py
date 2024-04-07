import os
import google.generativeai as genai
#from dotenv import load_dotenv   #for python-dotenv method
#load_dotenv()                    #for python-dotenv method


# AI APIKey: Google Gemini
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API'))

api_key=os.getenv('GOOGLE_GEMINI_API')
model = genai.GenerativeModel('gemini-pro')

def ai(prompt, message):
  response = model.generate_content(message)
  print(response.text)
  return (response.text)