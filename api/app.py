from flask import Flask, jsonify
import gdown
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    url = 'https://drive.google.com/u/0/uc?id=18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ&export=download'
    response = requests.get(url)
    with open('tradingBot.ipynb', 'wb') as f:
        f.write(response.content)
    return "HOLA"


