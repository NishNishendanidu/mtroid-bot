""" Sing a song... 
    Command .rattitude

    By @veryhelpful"""

import asyncio
import random

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"rflirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("here a fact about you......")
    await asyncio.sleep(1)
    s = random.randrange(1, 12)
    if s == 1:
        await event.edit("Your lips look lonely would they like to meet mine?")
    if s == 2:
        await event.edit(
            "There isn’t a word in the dictionary to describe how beautiful you are"
        )
    if s == 3:
        await event.edit(
            "I have had a really bad day and it always makes me feel better to see a pretty girl smile. So, would you smile for me?"
        )
    if s == 4:
        await event.edit("I lost my teddy bear can i sleep with you tonight?")
    if s == 5:
        await event.edit("I’m no organ donor but I’d be happy to give you my heart.")
    if s == 6:
        await event.edit(
            "If I had to rate you out of 10 I’d rate you a 9… because I am the one that you are missing"
        )
    if s == 7:
        await event.edit("Can I follow you? Cause my mom told me to follow my dreams")
    if s == 8:
        await event.edit("Your hand looks heavy can i hold it for you?")
    if s == 9:
        await event.edit(
            "You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me."
        )
    if s == 10:
        await event.edit(
            "Are you the sun? Because you’re so beautiful it’s blinding me"
        )
    if s == 11:
        await event.edit(
            "I should call you Google, because you have everything I’m looking for."
        )
    if s == 12:
        await event.edit(
            "Can you kiss me on the cheek so I can at least say a cute girl kissed me tonight?"
        )
