# Created By @keinshin For Black Lightning
# Makes Your Bot Super Bot Something Like Livegram but Better

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio 
from userbot.utils import lightning_cmd
from userbot import CMD_HELP

@borg.on(lightning_cmd(pattern="supbot?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@Manybot"
    await event.edit("```Wait...```")
    await asyncio.sleep(2)
    await event.edit("`Making Your Bot To Super Bot`")
    await asyncio.sleep(2)
    await event.edit("```Almost Done.........```")
    await asyncio.sleep(2)
    await event.edit("```Almost Done.......```")
    await asyncio.sleep(2)
    await event.edit("```Almost Done........```")
    await asyncio.sleep(2)
    await event.edit("```Almost Done.........```")
    await asyncio.sleep(2)
    await event.edit("```Almost Done......```")
    await asyncio.sleep(2)
    await event.edit("```Done```")
    await asyncio.sleep(2)
    await event.edit(f"**Done Bot Is Now A Superbot**   `{input_str}`")
    await asyncio.sleep(4)
    await event.edit(f"```Go To {input_str} To Manage Your Bot ``")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("Create a New Bot")
            await conv.get_response()
            await conv.send_message("I’ve copied the API token" )
            await conv.get_response()
            await conv.send_message(input_str)
            await conv.get_response()
            await conv.send_messafe("Skip")
            await conv.get_response()
            audio = await conv.get_response()
            await borg.send_message(event.chat_id, audio.text)
            await event.delete()
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @Manybot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("👀")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)   



@borg.on(lightning_cmd("command ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)    
    if "," in input_str:
        text, cmd = input_str.split(",")
    bot = "@Manybot"
    if input_str == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/commands ")
                await conv.get_response()
                await conv.send_message("Create Command")
                await conv.get_response()
                await conv.send_message(f"{input_str}")
                await conv.get_response()
                await conv.send_messafe(("Save"))
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Manybot `and retry!")
    elif "@" in input_str:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/commands ")
                await conv.get_response()
                await conv.send_message("Create Command")
                await conv.get_response()
                await conv.send_message(f"{input_str}")
                await conv.get_response()
                await conv.send_messafe(("Save"))
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Manybot `and try again!")
    elif "" in input_str:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/commands ")
                await conv.get_response()
                await conv.send_message("Create Command")
                await conv.get_response()
                await conv.send_message(f"{input_str}")
                await conv.get_response()
                await conv.send_messafe(("Save"))
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Manybot `and try again!")
                

        CMD_HELP.update(
    {
        "superbot": ".supbot ` <token>\nUse - Make Your Bot Super Bot Something Like Livegram But Better"
        
    }
)
