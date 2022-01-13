from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import lightning_cmd

telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


@borg.on(lightning_cmd(pattern="recognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    cat = await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("unblock @Rekognition_Bot and try again")
            await cat.delete()
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            cat = response.message.message
            await event.edit(cat)

        else:
            await event.edit("sorry, I couldnt find it")


@borg.on(lightning_cmd(pattern="purl ?(.*)"))
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
            await event.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(lightning_cmd(pattern="limits ?(.*)"))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                danish = await conv.get_response()
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @spambot `and retry!")


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


CMD_HELP.update(
    {
        "bots": ".purl (reply to file)\nUse - Get a direct download link of that file/doc/pic/vid\
        \n\n.reader (reply to url)\nUse - Open that url in telegraph .\
        \n\n.sgm (reply to any user or tag)\nUse - send details of that user.\
        \n\n.recognize (reply to any media)\nUse - send details about it.\
        \n\n.wspr (message) (target username/id)\nUse - Send a whisper message to that person.\
        \n\n.limits\nUse - Check if you are limited by telegram."
    }
)
