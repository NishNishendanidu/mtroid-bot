# Got it from @userbotjunks
# All in one code.

"""
Available Commands:
.tlol
.lol
.heart
.candy
.nothappy"""

import asyncio
from collections import deque

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern=r"candy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(lightning_cmd(pattern=r"nothappy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(lightning_cmd(pattern=r"heart"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(lightning_cmd(pattern=r"tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤨🤔🧐🤨"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(lightning_cmd(pattern=r"lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
