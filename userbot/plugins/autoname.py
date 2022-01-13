"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from uniborg.util import lightning_cmd
from userbot import ALIVE_NAME, CMD_HELP

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lightning"


@borg.on(lightning_cmd(pattern="autoname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        name = f"⌚{HM} 🔥{DEFAULTUSER}🔥 📅{DMY}"
        logger.info(name)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Successfully Changed Profile Name"
        # )
        await asyncio.sleep(DEL_TIME_OUT)
        await event.edit(f"Auto Name has been started Master")


CMD_HELP.update( {".autoname": "Auto Profile Updation Commands"})