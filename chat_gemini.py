import google.generativeai as genai
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = Flask(__name__)

GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY") # Criar um arquivo .env dentro do diretório raiz e configurar com esse codigo "GOOGLE_GEMINI_API_KEY= CHAVE DA API AQUI"


genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        return render_template("index.html", prompt=prompt, response=response.text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
