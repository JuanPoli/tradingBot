import google.auth
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

# authenticate and create Drive API client
auth.authenticate_user()
creds = Credentials.from_authorized_user_info(google.auth.default()[0])
drive_service = build('drive', 'v3', credentials=creds)

# download the Colab file
file_id = '18jK7gSM1Lv-AVYEoHmeDesaRO0eJhZkJ'
file_name = 'tradingBot.ipynb'
request = drive_service.files().get_media(fileId=file_id)
content = request.execute()
with open(file_name, 'wb') as f:
    f.write(content)

