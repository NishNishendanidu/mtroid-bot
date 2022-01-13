# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import os
import time
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, StartTime, topfunc
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, edit_or_reply, sudo_cmd

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
    PM_iMG = "https://telegra.ph/file/5db4087d9de9b738ad0fc.mp4"
else:
    PM_iMG = ALIVE_PIC


HELL_PIC = os.environ.get("HELL_PIC", None)
if HELL_PIC is None:
    HELL_IMG = "https://telegra.ph/file/d1400b2ae30b8e5e0d24e.mp4"
else:
    HELL_IMG = HELL_PIC

CAT_IMGE = os.environ.get("CAT_IMGE", None)
if CAT_IMGE is None:
    CAT_IMG = "https://telegra.ph/file/63abc60224dc567e3d441.jpg"
else:
    CAT_IMG = CAT_IMGE

version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "✮ MY BOT IS RUNNING SUCCESFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "
hellversion = "7.0"
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)


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

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

@borg.on(lightning_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(salive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**вℓα¢к ℓιgнтηιηg 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/lightning_support_channel)\n"
        )
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/lightning_support_group)\n"
        )
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ вℓα¢к ℓιgнтηιηg ](https://t.me/lightning_support_channel)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/blacklightningot)"
        await salive.get_chat()
        await salive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            salive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        await sallive.delete()
        return
    req = requests.get("https://telegra.ph/file/b01cd4ef19edc14195648.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(salive.chat_id, file=sticker)
        await borg.send_message(
            salive.chat_id,
            "**вℓα¢к ℓιgнтηιηg 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
            f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
            "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
            "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/lightning_support_channel)\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/lightning_support_group)\n"
            "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ вℓα¢к ℓιgнтηιηg ](https://t.me/blacklightningot)\n"
            "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/blacklightningot)",
            link_preview=False,
        )
        await salive.delete()


# Hellbot's Alive Message
# Credits to Hellboy Op


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid


pm_caption = "__**🔥🔥ɮʟǟƈӄ ʟɨɢɦȶռɨռɢ ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈ɮʟǟƈӄ ʟɨɢɦȶռɨռɢ😈       : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/lightning_support_group)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/krish1303y)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/KeinShin/Black-Lightningt) 🔹 [📜License📜](https://github.com/KeinShin/Black-Lightning/blob/master/LICENSE)"


@borg.on(lightning_cmd(outgoing=True, pattern="halive$"))
@borg.on(sudo_cmd(pattern="halive$", allow_sudo=True))
async def amireallyalive(halive):
    await halive.get_chat()
    await halive.delete()
    """ For .halive command, check if the bot is running.  """
    await borg.send_file(halive.chat_id, HELL_IMG, caption=pm_caption)
    await halive.delete()


# catuserbot's Alive
# Credits To catbot And Sandi


@borg.on(lightning_cmd(outgoing=True, pattern="calive$"))
@borg.on(sudo_cmd(pattern="calive$", allow_sudo=True))
async def amireallyalive(calive):
    if calive.fwd_from:
        return
    reply_to_id = await reply_id(calive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if PM_IMG:
        pm_caption = f"**{ALIVE_MSG}**\n\n"
        pm_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        pm_caption += f"**{EMOJI} Telethon version :** `{version}\n`"
        pm_caption += f"**{EMOJI} Lightning Userbot Version :** `{catversion}`\n"
        pm_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        pm_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        pm_caption += f"**{EMOJI} Master:** {DEFAULTUSER}\n"
        await calive.client.send_file(
            calive.chat_id, CAT_IMG, caption=pm_caption, reply_to=reply_to_id
        )
        await calive.delete()
    else:
        await edit_or_reply(
            calive,
            f"**{ALIVE_MSG}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version}\n`"
            f"**{EMOJI} Lightning Userbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {DEFAULTUSER}\n",
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


# Telebot's Alive
# Credits To Telebot And xditya
from userbot.Config import Var
from userbot.thunderconfig import Config

CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)


telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"


if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"


CMD_HELP.update(
    {
        "alive": "**alive**\
        \n\n**Syntax : **`.halive For Hellbot's Alive`\
        \n**Function : **__ Hellbot's Alive__\
        \nFor above two commands use `.bigspam` instead of spam for spamming more than 50 messages\
        \n\n**Syntax : **`.falive`\
        \n**Function : **__ Fridays's Alive.__\
        \n\n**Syntax : **`.halive `\
        \n**Function : **__ .hell Uerbot's Alive.__\
        \n\n**Syntax : **`.alive `\
        \n**Function : **__ .Lightning Uerbot's Alive.__\
        \n\n**Syntax : **`.awake `\
        \n**Function : **__ .Awake.__\
        \n\n\n**NOTE : All Credits To Thier Respective !!**"
    }
)
