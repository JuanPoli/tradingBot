from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    url = 'https://drive.google.com/file/d/18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ/view?usp=sharing'
    output = 'tradingBot.ipynb'
    gdown.download(url, output, quiet=False)
    return jsonify(message='colab notebook ran successfully')