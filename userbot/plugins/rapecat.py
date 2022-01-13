"""Emoji

Available Commands:

.rapecat

build by legend @r4v4n4 , if u edit it then u r gay...
edited by @TECHOPS_recompiled"""
import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 27)

    input_str = event.pattern_match.group(1)

    if input_str == "rapecat":

        await event.edit(input_str)

        animation_chars = [
            "**r**",
            "**ra**",
            "**rap**",
            "**rape**",
            "**rape_**",
            "**rape_c*",
            "**rape_ca**",
            "**rape_cat**",
            "**ape_cat🐅**",
            "**pe_cat🐅🐈**",
            "**e_cat🐅🐈🐈**",
            "**_cat🐅🐈🐈🐈**",
            "**cat🐅🐈🐈🐈🐈**",
            "**at🐅🐈🐈🐈🐈🐈**",
            "**t🐅🐈🐈🐈🐈🐈🐈**",
            "🐅🐈🐈🐈🐈🐈🐈🐈",
            "🐅🐈🐈🐈🐈🐈🐈🐈🐈",
            "🐅🐈🐈🐈🐈🐈🐈🐈🐈🐈",
            "🐈🐈🐈🐈🐈🐈🐈🐈",
            "🐈🐈🐈🐈🐈🐈🐈",
            "🐈🐈🐈🐈🐈🐈",
            "🐈🐈🐈🐈🐈",
            "🐈🐈🐈🐈",
            "🐈🐈🐈",
            "🐈🐈",
            "🐈",
            "🐅",
            "**rApEd**",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
