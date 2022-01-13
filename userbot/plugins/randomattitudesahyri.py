""" Sing a song... 
    Command .attituder

    By @veryhelpful"""

import asyncio
import random

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"attituder$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("@veryhelpful Making A Shayri for u.......")
    await asyncio.sleep(2)
    s = random.randrange(1, 8)
    if s == 1:
        await event.edit(
            "Dil nhi karta ab\n kisi se dil lagane ko \n bohot aati hai tere jaise \n keh deta hu hoon laut jane ko."
        )
    if s == 2:
        await event.edit(
            "humari hesiyat ka andaza tum ye\n jaan ke laga lo hum kabhi unke \n nahi hote jo har kisi ke ho jate hai "
        )
    if s == 3:
        await event.edit(
            "Attitude तो अपना भी खानदानी है,\nऔर तू मेरे दिल की रानी है, \nइसलिये कह रहा हूँ मान जा, \nक्योंकि अपनी तो करोड़ो दीवानी हैं।"
        )
    if s == 4:
        await event.edit(
            "मेरा वाला थोड़ा लेट आयेगा,\n लेकिन जब आयेगा तो लाखो में एक आयेगा।"
        )
    if s == 5:
        await event.edit(
            "इतना Attitude न दिखा जिंदगी में तकदीर बदलती रहती है,\n शीशा वहीं रहता है,\n पर तस्वीर बदलती रहती है।"
        )
    if s == 6:
        await event.edit(
            "हम से है ज़माना, ज़माने से हम नही,\nकोई हम से नज़रे मिलाये, \nकिसी मे इतना दम नही।"
        )
    if s == 7:
        await event.edit(
            "हम तो शौक तलवारों के पाला करते हैं,\nबन्दूकों की ज़िद तो बच्चे किया करते हैं।\nशेर अपना शिकार करते हैं और हम अपने Attitude से वार करते हैं।"
        )
    if s == 8:
        await event.edit(
            "शेर अपना शिकार करते हैं\n और हम अपने Attitude से वार करते हैं।"
        )
