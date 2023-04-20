from flask import Flask, jsonify
import gdown
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO from vercel use flask"

@app.route("/run-colab")
def run_colab():
    return jsonify(message='colab notebook ran successfully')


