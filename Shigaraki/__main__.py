import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Shigaraki import LOGGER, app, userbot
from Shigaraki.core.call import Shigaraki
from Shigaraki.misc import sudo
from Shigaraki.plugins import ALL_MODULES
from Shigaraki.utils.database import get_banned_users, get_gbanned
from config import filter


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("assistant variables is empty")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            filter.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            filter.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Shigaraki.plugins" + all_module)
    LOGGER("Shigaraki.plugins").info("plugins loaded.")
    await userbot.start()
    await Shigaraki.start()
    try:
        await Shigaraki.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Shigaraki").error(
            "trun on vc of log channel"
        )
        exit()
    except:
        pass
    await Shigaraki.decorators()
    LOGGER("Shigaraki").info(
        "Powered by @hxh_network"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Shigaraki").info("stopping bot....")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
