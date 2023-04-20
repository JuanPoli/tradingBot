from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    gdown.download('https://colab.research.google.com/drive/18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ?usp=sharing', 'tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
