# Inspired and Help Taken by Animesticker plugin("waifu" command)
# Plugin Made By @Anonymous_Machinee
# Kang With Credit
# (c) Phantom Userbot

## ALL IMPORTS ARE OF WAIFU PLUGIN (NO DELETION , ONLY ADDITION IN IMPORT)
import random

from telethon.errors import ChatSendStickersForbiddenError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.stic ?(.*)")
async def machine(stick):
    # """Creates random anime sticker!"""
    text = stick.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as .stic <emoji>")
    stickers = await bot.inline_query("sticker", f"{text}")
    hm = len(stickers)
    op = random.randrange(0, hm)
    try:
        await stickers[op].click(
            stick.chat_id,
            reply_to=stick.reply_to_msg_id,
            silent=True if stick.is_reply else False,
            hide_via=True,
        )
        await stick.delete()
    except ValueError:
        await stick.edit(
            "Use This Command as .stic <any emoji>\nor Stickers are Not Avaliable for Entered Emoji"
        )
    except ChatSendStickersForbiddenError:
        await stick.edit("Sorry boss Can't Send Sticker Here !!")

    CMD_HELP.update({"stic": ".stic : will send random sticker from emoji."})
