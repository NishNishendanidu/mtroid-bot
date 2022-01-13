# (c) @UniBorg

import asyncio
from collections import deque

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"moon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
