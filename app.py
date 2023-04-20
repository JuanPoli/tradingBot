from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    return gdown.download('https://drive.google.com/uc?id=18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ', 'tradingBot.ipynb', quiet=False)
    