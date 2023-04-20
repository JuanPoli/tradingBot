from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    try:
        gdown.download('https://drive.google.com/uc?id=18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ', 'tradingBot.ipynb', quiet=False)
        return jsonify({'message': 'colab notebook ran successfully'})
    except Exception as e:
        return jsonify({'message': f'error running colab notebook: {str(e)}'}), 500
