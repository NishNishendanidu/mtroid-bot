# Created  By @keinshin

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "
bot = "@gif"


@borg.on(lightning_cmd("gif ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    lightn_gif = event.pattern_match.group(1)
    if lightn_gif == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("@gif")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(f"**Bruh:** `unblock` @gif `and Then try {DEFAULTUSER} retry!")
    elif "@" in lightn_gif:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("@gif " + lightn_gif)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(f"**Bruh:** `unblock` @gif `and Then try {DEFAULTUSER} retry")
    elif "" in lightn_gif:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("@gif " + lightn_gif)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(f"**Bruh:** `unblock` @gif `and Then try {DEFAULTUSER} retry")
