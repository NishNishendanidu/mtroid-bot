"""Fun pligon...for HardcoreUserbot
\nCode by @veryhelpful
type `.sadsawan2` and to see the fun.
"""
import asyncio

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern="sad1 ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("एक धोखा खाकर रुक गए.. ")
        await asyncio.sleep(2)
        await event.edit("बंद कर दिए सारे रास्ते हो सकता है")
        await asyncio.sleep(2)
        await event.edit("बना हो कोई और तेरे वास्ते हर कोई एक जैसा थोड़ी ना होता")
        await asyncio.sleep(2)
        await event.edit("तू देख तो सही बदलकर पुराने रास्ते..")
        await asyncio.sleep(2)
        await event.edit(
            "**एक धोखा खाकर रुक गए..,बंद कर दिए सारे रास्ते हो सकता है बना हो कोई और तेरे वास्ते हर कोई एक जैसा थोड़ी ना होता तू देख तो सही बदलकर पुराने रास्ते..**"
        )
