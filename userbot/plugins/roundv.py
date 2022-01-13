# COPYRIGHT © DARK COBRA
# Plugin made by @hellboi_atul ...
# You may use this with permission..and
# Please don't remove the credits..
# else gay...
# Plugin which can convert any 1:1 video(square video) to round video...


from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import lightning_cmd

# ===================================================================================


@borg.on(lightning_cmd(r"roundv$"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any users message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to media message```")
        return
    chat = "@TelescopyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("**Reply to actual users message.**")
        return
    okay = await event.edit("**Processing weit..**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            response = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await okay.edit("__Please unblock @TelescopyBot and try again__")
            return
            await okay.delete()
        if not response.media:
            await event.client.send_message(event.chat_id, response.message)
        if response.media:
            await event.client.send_file(event.chat_id, response)
