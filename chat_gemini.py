import google.generativeai as genai
from flask import Flask, render_template, request

app = Flask(__name__)

GOOGLE_GEMINI_API_KEY = "CHAVE API"

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
