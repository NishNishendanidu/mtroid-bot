"""Emoji

Available Commands:

.wtf"""


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The F",
        "What The Fa",
        "What The Fak Brah",
        "[What The Fakk Brah](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
