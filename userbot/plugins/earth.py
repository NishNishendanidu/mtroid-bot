# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

import asyncio
from collections import deque

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="earth"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
