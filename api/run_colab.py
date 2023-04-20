import requests

def run_colab(request):
    url = 'https://drive.google.com/u/0/uc?id=18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ&export=download'
    file_name = 'tradingBot.ipynb'
    response = requests.get(url)
    open(file_name, 'wb').write(response.content)
    return {'message': 'colab notebook ran successfully'}
