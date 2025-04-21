import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 25955854

API_HASH = "2ede59823a90cb31442a74f5ae01f675"

BOT_TOKEN = "7979900579:AAHY6sPeK6jmmvwi7fePwxCm11dmCAOYUN4"

BOT_ID = 7979900579

BOT_USERNAME = "shigaraki_probot"

OWNER_USERNAME = "SLAYER1237"

BOT_NAME = "Shigaraki"

ASSUSERNAME = "DEATH_WISH"


MONGO_DB_URI = "mongodb+srv://shigarakisan:demnkin@cluster0.cxt4iov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = 500000

LOGGER_ID = -1002392274240

DISASTER_LOG = -1002392274240

OWNER_ID = 6018803920

SPECIAL_USER = 7933208850

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = ""

UPSTREAM_BRANCH = "master"

GIT_TOKEN = ""


SUPPORT_CHANNEL = "https://t.me/MBT_UPDATES"

SUPPORT_CHAT = "https://t.me/+ytk9hkZfGjY3MDRl"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000


SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = "BQFTgqgAPNqbr8KqG8r3VNw0h5J9VsqK-lcmadfaF-DTlt7htcuulAufS3K8vGmP-o7x6x6JrrZVvy_FIw2w6fUKas0YbPY2r48RM9vU2eoAImPvmPigbQ6zxTqeyukN8o7119bH6-jW-6bIE74pet6p4nZnjwQTYHIHGvtnh4MTitCpvx5RNBG1hcjZ3TLD0Zgjgj0_bUW5g-DSrIoWJkjNJae9usGYwLHSAwmQtAglmPxeRKoWXRB6LlnRDGUWHlBnWBin3bymfAn0LAsuedAwLFguYzxIKo6idgYYWGldRQMtkXV50BPzX2nJW0_erwfkmDTXHENgop9kTTrPHJHJ8X37sgAAAAHUsVFIAA"
STRING2 = None 
STRING3 = None 
STRING4 = None
STRING5 = None
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://files.catbox.moe/iffmnv.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/f3yuiy.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/urv7wi.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2tcim5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/jkqyg2.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
