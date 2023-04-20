from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/uc?id=1eBM0SUzwM2n18iS_J7Q8wTI89dTPYC6k', 'tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')

