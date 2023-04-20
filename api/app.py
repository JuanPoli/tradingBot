from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    url = 'https://colab.research.google.com/drive/18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ?usp=sharing'
    r = requests.get(url, allow_redirects=True)
    open('tradingBot.ipynb', 'wb').write(r.content)
    return jsonify(message='colab notebook ran successfully')
