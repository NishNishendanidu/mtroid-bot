"""Emoji
Available Commands:
.bb
"""


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("ubb"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Thanks")
    animation_chars = [
        "Click here to Go to Telegraph",
        "[Click Here For Guide]https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
