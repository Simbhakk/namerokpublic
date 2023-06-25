import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ''))
	API_HASH = os.environ.get("API_HASH",'')
	BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
	BOT_USERNAME = os.environ.get("BOT_USERNAME", 'Publicsavei')
	
	DATABASE_URL = os.environ.get("DATABASE_URL",'mongodb+srv://devilbot:Rajbot@cluster0.ldrbggy.mongodb.net/?retryWrites=true&w=majority')
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1001661389574'))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	
