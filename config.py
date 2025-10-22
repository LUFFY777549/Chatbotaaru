from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 21218274))
API_HASH = getenv("API_HASH", "3474a18b61897c672d315fb330edb213")
BOT_TOKEN = getenv("BOT_TOKEN", "8378514673:AAGD4gfcOP6evzXsU0DQmrIqjR1N9gy_TiU")
OWNER_ID = int(getenv("OWNER_ID", 7576729648))
LOGGER_ID = int(getenv("LOGGER_ID", -1002345678901))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://narutouzumaki568876:narutouzumaki568876@cluster0.kn2tmlk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(getenv("AUTH_CHANNEL", -1002955024896))
FSUB = int(getenv("FSUB", -1002955024896))
WEB_APP = getenv("WEB_APP", "False").lower() == "true"

STICKER = [
    "CAACAgUAAxkBAAECbiFo-Sx9AZTY73zVuAx_vwNhZ3zPwQACvwcAAo5lMFVAgMnnDM43WR4E",
]

IMG = [
    "https://files.catbox.moe/8eobds.jpg",
]