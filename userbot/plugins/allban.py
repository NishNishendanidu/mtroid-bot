# originally created by @danish_00

# team cobra
from asyncio import sleep

from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from userbot import bot
from userbot.utils import lightning_cmd


@bot.on(lightning_cmd(pattern=r"allban", outgoing=True))
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit(
            " U Don't have sufficient permission 🧐 Alexa Iski Gand Maro 😑😑"
        )
        return
    await event.edit("Doing Nothing 🙃🙂")  # Kang with Credits
    # for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(
                EditBannedRequest(
                    event.chat_id,
                    int(user.id),
                    ChatBannedRights(until_date=None, view_messages=True),
                )
            )
        except Exception as e:
            await event.edit(str(e))
        await sleep(0.5)
    await event.edit("Nothing Happend here🙃🙂")
