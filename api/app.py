from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO from vercel use flask"

@app.route("/api/run-colab")
def run_colab():
    response = requests.get("https://your-vercel-app-url/api/run-colab")
    return response.json()

if __name__ == '__main__':
    app.run()

