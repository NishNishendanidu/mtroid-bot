from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd

naam = str(ALIVE_NAME)

bot = "@Missrose_bot"


@borg.on(lightning_cmd("fedban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and retry!"
                )
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and try again!"
                )
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and try again!"
                )


@borg.on(lightning_cmd("unfedban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and retry!"
                )
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and try again!"
                )
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit(
                    "**Error:** `unblock` @Missrose_bot `and try again!"
                )
