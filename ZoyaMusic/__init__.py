from aiohttp import ClientSession
from .console import LOGGER

from ZoyaMusic.modules.core.app import App
from ZoyaMusic.modules.core.bot import Bot
from ZoyaMusic.modules.core.dirs import dirr
from ZoyaMusic.modules.core.git import git
from ZoyaMusic.misc import dbb, heroku, sudo

dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = App()

bot = Bot()


from ZoyaMusic.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
