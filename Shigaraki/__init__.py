from Shigaraki.core.bot import Shigaraki as Shigaraki
from Shigaraki.core.dir import dirr
from Shigaraki.core.git import git
from Shigaraki.core.userbot import Userbot
from Shigaraki.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Shigaraki()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
