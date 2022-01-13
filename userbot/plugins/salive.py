import time

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.Config import Var
from userbot.plugins import telever
from userbot.utils import lightning_cmd, sudo_cmd


# Functions
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


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Var.ALIVE_IMAGE
pm_caption = "➥ **𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += f"➥ **Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{telever}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](https://github.com/Anmol-dot283/Black-Lightning)\n"
pm_caption += "➥ **Copyright** : By [KeinShin@Github](GitHub.com/StarkGang)\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[🇮🇳 Deploy 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤Userbot 🇮🇳](https://telegra.ph/FRIDAY-06-15)"


@borg.on(lightning_cmd(pattern=r"fralive"))
@borg.on(sudo_cmd(pattern=r"fralive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .salive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "salive": "**sLive**\
\n\n**Syntax : **`.salive`\
\n**Usage :** Check if UserBot is salive"
    }
)
