#plugin by @Rishisuperyo
#animation by @Rishisuperyo
#Thanks to @huehuehuehuehuehuehuehuehu for idea
#usage ==> .tornado
from telethon import events
from userbot.utils import lightning_cmd
@borg.on(lightning_cmd(pattern=r"tornado"))
async def hapy (event):
     a=".                .....................\n                 ....................\n                 .................\n                 .................\n                 ...............\n                 .............\n                 ...........\n                 ..........\n                 .........\n                 .......\n                 ......\n                 .....\n                 ....\n                 ...\n                 ..\n                 ."
     await event.edit(a)
