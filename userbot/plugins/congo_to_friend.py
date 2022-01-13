import random

from userbot import CMD_HELP
from userbot.utils import lightning_cmd

RUNSREACTS = [
    "`Aur Bata Bsdk Kar Liya Tunee Party De Chal!`",
    "`Chal Gand Phad Dunga Udd Mat Abb`",
    "`Oo Wow Mere Beta Sikh Gaya!`",
    "`Chall Badhiya Congo`",
    "`Fuck You And Congo.`",
    "`Mere Ladke Lavde te lashan Akhir  Karliya Tune.`",
    "`Very Good.`",
    "`Veryy Good Nhi Bulanga Bass Tu Chutiya Hai!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]


@borg.on(lightning_cmd(pattern="chalbsdk"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


CMD_HELP.update(
    {
        "chalbsdk": "**congo_to_friend**\
\n\n**Syntax : **`.chalbsdk`\
\n**Usage :** This plugin is used to congratulate friend."
    }
)
