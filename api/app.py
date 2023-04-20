from flask import Flask, jsonify
import nbconvert
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO from vercel use flask"

@app.route('/run-colab')
def run_colab():
    notebook_file = "tradingBot.ipynb"
    python_file = "tradingBot.py"
    nbconvert.export_python(notebook_file, python_file)
    os.system(f"python {python_file}")

