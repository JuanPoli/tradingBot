from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    file_id = '18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ'
    url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(url)

    if response.status_code == 200:
        with open('filename.csv', 'wb') as f:
            f.write(response.content)
        print('File downloaded successfully!')
    else:
        print('Error downloading file')
    return jsonify(message='colab notebook ran successfully')
