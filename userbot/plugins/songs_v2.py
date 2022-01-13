# plugin made by @hellboi_atul bug fixes by @Mrconfused

# Copyright (C) DARK COBRA 2020.

# if you change these lines you are gay...bc fuck off!

# leechers stay away😑...if you use this code without credit...u gay bitch fuck off...!

import asyncio
import os
import re

from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterMusic

from userbot import CMD_HELP, bot
from userbot.utils import lightning_cmd

try:

    pass

except:

    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


# @register(outgoing=True, pattern="^.netase(?: |$)(.*)")


@borg.on(lightning_cmd("song2 ?(.*)"))
async def WooMai(netase):

    if netase.fwd_from:

        return

    song = netase.pattern_match.group(1)

    chat = "@WooMaiBot"

    link = f"/netease {song}"

    await netase.edit("```Getting Your Music```")

    async with bot.conversation(chat) as conv:

        await asyncio.sleep(2)

        await netase.edit("`Downloading...Please wait`")

        try:

            msg = await conv.send_message(link)

            response = await conv.get_response()

            respond = await conv.get_response()

            """ - don't spam notif - """

            await bot.send_read_acknowledge(conv.chat_id)

        except YouBlockedUserError:

            await netase.edit("```Please unblock @WooMaiBot and try again```")

            return

        await netase.edit("`Sending Your Music...weit!😎`")

        await asyncio.sleep(3)

        await bot.send_file(netase.chat_id, respond)

    await netase.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])

    await netase.delete()


@borg.on(lightning_cmd("songs ?(.*)"))
async def _(event):

    try:

        await event.client(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))

    except UserAlreadyParticipantError:

        pass

    except:

        await event.reply(
            "You need to join [this](https://t.me/joinchat/DdR2SUvJPBouSW4QlbJU4g) group for this module to work.",
            link_preview=False,
        )

        return

    args = event.pattern_match.group(1)

    if not args:

        await event.edit("`Enter song name`")

        return

    chat = -1001271479322

    current_chat = event.chat_id

    current_msg = event.id

    try:

        async for event in event.client.iter_messages(
            chat, search=args, limit=1, filter=InputMessagesFilterMusic
        ):

            await event.client.send_file(current_chat, event, caption=event.message)

    except:

        await event.reply("`Song not found.`")

        return

    await event.client.delete_messages(current_chat, current_msg)


IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:

    """Remove emojis and other non-safe characters from string"""

    return re.sub(IF_EMOJI, "", inputString)


CMD_HELP.update(
    {
        "song2": ".song2\nUse - download song \
        \n\n.songs\nUse - songs"
    }
)
