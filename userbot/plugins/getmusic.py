# plugin made by @hellboi_atul
# gaandu bina credits ka plugin liya toh tu maderchod...tera khandaan maderchod😂😂
# Thanks to @SongsForYouBot's owner..

import asyncio
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import bot
from userbot.events import register

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/Anitimeofficial"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await so.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(1)
        await so.edit("`Downloading...Please wait`")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await so.edit("```Please unblock @SongsForYouBot and try again```")
            return
        await so.edit("`Sending Your Music...weit!😎`")
        await asyncio.sleep(0.1)
        await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await so.delete()
