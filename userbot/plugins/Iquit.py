"""
.iquit
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("iquit", outgoing=True))
async def leave(e):
    if e.fwd_from:
         return
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`Thats why i left earth, time to leave moon`"
        )
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit(
                "`Not a group`"
            )
