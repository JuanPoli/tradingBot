import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "HELLO from vercel use flask"

@app.route('/run-colab')
def run_colab():
    file_id = '18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ#scrollTo=osBHhVysOEzi'
    url = f'https://colab.research.google.com/drive/18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ#scrollTo=osBHhVysOEzi'
    response = requests.get(url)
    content = response.content

    with open('tradingBot.ipynb', 'wb') as f:
        f.write(content)

    return 'Colab file downloaded successfully!'

if __name__ == '__main__':
    app.run()
