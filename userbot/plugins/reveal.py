#ported from ultroid by @Hackintush 

import asyncio
import os
import time

from uniborg.util import edit_or_reply, sudo_cmd

from userbot import bot as cipherx 
from userbot.utils import lightning_cmd
from userbot import CMD_HELP

opn = []

@cipherx.on(lightning_cmd(pattern="reveal"))
@cipherx.on(sudo_cmd(pattern="reveal", allow_sudo=True))
async def _(event):
    xx = await edit_or_reply(event, "`...`")
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if a.media:
            b = await a.download_media()
            c = open(b, "r")
            d = c.read()
            c.close()
            n = 4096
            for bkl in range(0, len(d), n):
                opn.append(d[bkl : bkl + n])
            for bc in opn:
                await event.client.send_message(
                    event.chat_id,
                    f"```{bc}```",
                    reply_to=event.reply_to_msg_id,
                )
            await event.delete()
            opn.clear()
            os.remove(b)
            await xx.delete()
        else:
            return await edit_or_reply(xx, "`Reply to a readable file`", time=10)
    else:
        return await edit_or_reply(xx, "`Reply to a readable file`", time=10)

CMD_HELP.update(
    {
        "reveal": ".reveal <reply to a file>\nUse - Read contents of file and send as a telegram message."
    }
)
