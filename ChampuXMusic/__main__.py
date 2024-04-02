import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ChampuXMusic import LOGGER, app, userbot
from ChampuXMusic.core.call import Champu
from ChampuXMusic.misc import sudo
from ChampuXMusic.plugins import ALL_MODULES
from ChampuXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ChampuXMusic.plugins" + all_module)
    LOGGER("ChampuXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Champu.start()
    try:
        await Champu.stream_call("https://graph.org/file/e254ad05e8f46bd819478.mp4")
    except NoActiveGroupCall:
        LOGGER("ChampuXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Champu.decorators()
    LOGGER("ChampuXMusic").info(
        "\x43\x68\x61\x6D\x70\x75\x20\x42\x6F\x74\x20\x68\x61\x73\x20\x62\x65\x65\x6E\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x20\x73\x74\x61\x72\x74\x65\x64\x2E\x0A\x0A\x40\x54\x68\x65\x43\x68\x61\x6D\x70\x75\x20"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ChampuXMusic").info("Stopping Champu Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
