"""Check if userbot awake or not . 

"""
from userbot import ALIVE_NAME
from userbot.Config import Var
from userbot.utils import lightning_cmd
import os
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
if not ALIVE_PHOTTO:
    ALIVE_PHOTTO = "https://telegra.ph/file/17b2d55c3bb07b2d8f805.mp4"


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

ALIVE_MESSAGE = Var.ALIVE_MESSAGE
if not ALIVE_MESSAGE:
    ALIVE_MESSAGE = "**🔱Black Lightning IS Awake🔱 \n\n\n**"
    ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
    ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.0 \n\n`"
    ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
    ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
    ALIVE_MESSAGE += f"`Support Channel` : @blacklightningot \n\n"
    ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "
else:
    ALIVE_MESSAGE = ALIVE_MESSAGE

# @command(outgoing=True, pattern="^.awake$")
@borg.on(lightning_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete()
    await borg.send_file(awake.chat_id, ALIVE_PHOTTO, caption=ALIVE_MESSAGE)

from userbot import CMD_HELP

CMD_HELP.update( {
    ".awake": "**USAGE** Check If Userbot Alive ."
})
