import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from ZoyaMusic import LOGGER, app, bot
from ZoyaMusic.modules.core.call import Kaal
from ZoyaMusic.modules.main.database import get_banned_users, get_gbanned
from ZoyaMusic.utilities import config
from ZoyaMusic.utilities.config import BANNED_USERS
from ZoyaMusic.plugins import ALL_MODULES


loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("ZoyaMusic").error(
            "No Pyrogram String Defined !!..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("ZoyaMusic").warning(
            "Spotify Queries Not Working Without Spotify ID & Secret."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZoyaMusic.plugins" + all_module)
    LOGGER("ZoyaMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await app.start()
    await Kaal.start()
    try:
        await Kaal.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ZoyaMusic").error(
            "[ERROR] - \n\nHey, At first Please Turn On VC in Your Logger Group."
        )
        sys.exit()
    except:
        pass
    await Kaal.decorators()
    LOGGER("ZoyaMusic").info("Congratulations, Your ZoyaMusic Bot Now Deployed ...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("ZoyaMusic").info("Stopping Music Bot...")
