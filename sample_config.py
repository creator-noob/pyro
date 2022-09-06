import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5503878652:AAFPZWeZ0q_PAPub8JO3nOQxVCi5lmaGl3A")
    APP_ID = int(os.environ.get("APP_ID", 18028033))
    API_HASH = os.environ.get("API_HASH","0501ff3a1a276f92534e335f9a76b6e6")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
