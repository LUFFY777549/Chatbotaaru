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
    "CAACAgUAAx0CeVrr4AABA2WaaCQoVC8FjSD8VuVTOemf8iMsuB4AAsUXAALfySFVZ8WvmJF9y7QeBA",
    "CAACAgUAAx0CeVrr4AABA2WbaCQoVFGQ8bMbYbjdAa_hwMX5Ey0AArQVAALa2yBVNyiv0PjLavkeBA",
    "CAACAgUAAx0CeVrr4AABA2WZaCQoTzXsmocAAV4ei8U4CHEaiCOkAAJtFQACDZkgVdlv6ZpBRa5OHgQ",
    "CAACAgUAAx0CeVrr4AABA2WYaCQoTLix5yKaiPC6VIAUGSQ50_0AAoIWAAL_vCFV9UCakfSiUnQeBA",
    "CAACAgUAAx0CeVrr4AABA2WXaCQoSN2AR6W-2usiKLpMy2WSdk0AAqcaAAKXHiFVeW8TyEoCbEMeBA",
    "CAACAgUAAx0CeVrr4AABA2WVaCQoOY7lsoxoeywegfiOQxVc74MAAs0TAALlgyFVlZxoUNHWXFAeBA",
    "CAACAgUAAx0CeVrr4AABA2WUaCQoNE9U5q9W1pgSXj9bpRTnoXgAAkYXAAI68ylV_qo6hecGh40eBA",
    "CAACAgUAAx0CeVrr4AABA2WDaCQnvUjQgOKVm5deqrv4_Jmkd14AAgoUAAJ3uCBVq_-M6rUuoi8eBA",
    "CAACAgUAAx0CeVrr4AABA2WEaCQnwECiKsxllioAAXTiYi5RPD_OAAKbFwACXCMpVcc_pIRGEhGNHgQ",
    "CAACAgUAAx0CeVrr4AABA2WFaCQnx1KB260wSbHWf4iOv9X3aVIAAm8VAAK0CyFV9AlM_s8podUeBA",
    "CAACAgUAAx0CeVrr4AABA2WHaCQn2-MhtiM4QpdcLNjOQ0imRkQAAukUAAIgkCFV5eb3HtvsISUeBA",
    "CAACAgUAAx0CeVrr4AABA2WIaCQn5GYTy5yUj-1fyHsYqI9bccQAAgMaAAI13CFVbtM4jrz2LkoeBA",
]

IMG = [
    "https://files.catbox.moe/rz42be.jpg",
    "https://files.catbox.moe/41e7z2.jpg",
    "https://files.catbox.moe/q4o6l9.jpg",
    "https://files.catbox.moe/q4o6l9.jpg",
    "https://files.catbox.moe/0mpi0w.jpg",
    "https://files.catbox.moe/jnmurs.jpg",
]