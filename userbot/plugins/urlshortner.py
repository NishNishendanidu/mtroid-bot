import pyshorteners

from userbot.utils import lightning_cmd, sudo_cmd


@borg.on(lightning_cmd(pattern="urlshort (.*)"))
@borg.on(sudo_cmd(pattern="urlshort (.*)", allow_sudo=True))
async def vom(event):
    try:
        link = event.pattern_match.group(1)
        sed = pyshorteners.Shortener()
        kek = sed.tinyurl.short(link)
        bestisbest = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>Shortened Link</u></b> ➠ <code>{kek}</code>"
        )
        await event.edit(bestisbest, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)
