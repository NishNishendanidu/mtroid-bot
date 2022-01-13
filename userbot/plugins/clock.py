# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

import asyncio
from collections import deque

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"clock"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"))
    for _ in range(60):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
