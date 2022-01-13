# Plugin made by @hellboi_atul for DARK COBRA..
# You can use this..but don't edit/remove these comment lines..
# This module fetches the audio from YouTube for the given query..
# So wahi...Enjoy
""" This plugin is the V2 of utube.py in DARK COBRA userbot..which directly fetches the audio..
 it's not necessary for this plugin to always work.. 
 Audios are auto queued for downloads..
 This too made by @hellboi_atul .. """

import re

from userbot import bot
from userbot.utils import lightning_cmd

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


@borg.on(lightning_cmd(pattern="uta(?: |$)(.*)"))
async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            (await doit.get_reply_message()).message
        else:
            await doit.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return
    sticcers = await bot.inline_query("Lybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(
        doit.chat_id,
        reply_to=doit.reply_to_msg_id,
        silent=True if doit.is_reply else False,
        hide_via=True,
    )
    await doit.delete()
