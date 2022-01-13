import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern="purl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @FiletolinkTGbot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(lightning_cmd(pattern="sgm ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to an user message.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a message.**")
        return
    chat = "@sangmatainfo_bot"
    reply_message.sender
    await event.edit("**Getting user's name history..**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @SangMataInfo_bot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(lightning_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a url message.**")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @chotamreaderbot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(lightning_cmd(pattern="connecter ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return
    chat_id = event.chat_id
    await event.client.send_message("missrose_bot", "/connect {}".format(chat_id))
    await event.edit("[Connected](https://t.me/missrose_bot)")
    await asyncio.sleep(3)
    await event.delete()
