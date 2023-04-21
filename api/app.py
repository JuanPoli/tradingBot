from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO from vercel use flask"

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')

