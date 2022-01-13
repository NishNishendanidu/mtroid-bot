#Lifted from Dark Venom 
#Credits @Error-Shivansh

import asyncio

import time

from datetime import datetime

from platform import python_version as ver

from telethon import __version__, events

from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate

from userbot.utils import lightning_cmd

from . import *

#### Variables ####

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ʙʟᴀᴄᴋ-ʟɪɢʜᴛɴɪɴɢ ᴜꜱᴇʀ "
ALIVE_MSG = f"This is {DEFAULTUSER}'s 𝐁𝐥𝐚𝐜𝐤-𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐛𝐨𝐭"

ALIVE_PIC = Config.ALIVE_PHOTTO

if ALIVE_PIC is None :

    ALIVE_PIC = "https://telegra.ph/file/4f754de25cb890e3fb51e.mp4"

botversion = "1.2.0"

#### Functions ####

def get_readable_time(seconds: int) -> str:

    count = 0

    ping_time = ""

    time_list = []

    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:

        count += 1

        if count < 3:

            remainder, result = divmod(seconds, 60)

        else:

            remainder, result = divmod(seconds, 24)

        if seconds == 0 and remainder == 0:

            break

        time_list.append(int(result))

        seconds = int(remainder)

    for x in range(len(time_list)):

        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:

        ping_time += time_list.pop() + ", "

    time_list.reverse()

    ping_time += ":".join(time_list)

    return ping_time

@borg.on(lightning_cmd(pattern=r"valive"))
@borg.on(sudo_cmd(pattern=r"valive", allow_sudo=True))

async def alive(e):

    start = datetime.now()

    end = datetime.now()

    ping = (end - start).microseconds / 1000

    uptime = get_readable_time((time.time() - Lastupdate))

    cap = """
**𝐁𝐥𝐚𝐜𝐤-𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐛𝐨𝐭**
**{}**
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ **Ⲟⲱⲛⲉʀ** - `{}` 
║┣⪼ **Ⲋⲧⲁⲧυⲋ** - `Ⲟⲛⳑⲓⲛⲉ`
║┣⪼ **Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ** - `{}`
║┣⪼ **Ⳙⲣⲧⲓⲙⲉ** - `{}` 
║┣⪼ **Ⲃⲟⲧ Ⲣⲓⲛⳋ** - `{}`
║┣⪼ **Ⲣⲩⲧⲏⲟⲛ** - `{}` 
║┣⪼ **Ⲧⲉⳑⲉⲧⲏⲟⲛ** - `{}` 
║┣⪼ [✨𝐁𝐥𝐚𝐜𝐤-𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨](https://github.com/KeinShin/Black-Lightning/)
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪
""".format(

        ALIVE_MSG,

        DEFAULTUSER,

        botversion,

        uptime,

        ping,

        ver(),

        __version__,

    )

    try:

        await e.get_chat() 

        await borg.send_file(e.chat_id, file=ALIVE_PIC,caption=cap)

        await e.delete()

    except ChatSendMediaForbiddenError:

        await e.edit(cap, link_preview=False)

       

CMD_HELP.update(

    {

        "valive": "**VALive**\
\n\n**Syntax : **`.valive`\
\n**Usage :** Check if 𐌵sᥱrδ᧐ᴛ is alive"

    }

)
