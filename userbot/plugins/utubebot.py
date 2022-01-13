import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import lightning_cmd, edit_or_reply

SEARCH_STRING = "<code>Ok weit, searching....</code>"
NOT_FOUND_STRING = "<code>Sorry !I am unable to find any results to your query</code>"
SENDING_STRING = "<code>Ok I found something related to that.....</code>"
BOT_BLOCKED_STRING = "<code>Please unblock @utubebot and try again</code>"


@borg.on(lightning_cmd(pattern="yt (.*)"))
async def fetcher(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@utubebot"
    event = await edit_or_reply(event, SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            ok = await conv.get_response()
            while ok.edit_hide != True:
                await asyncio.sleep(0.1)
                ok = await event.client.get_messages(chat, ids=ok.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(("Sorry I found nothing..")):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    event, NOT_FOUND_STRING, parse_mode="html", time=5
                )
            await event.edit(SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(BOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>==> <code>{song}</code></b>",
            parse_mode="html",
        )
        await event.delete()
        await delete_messages(event, chat, purgeflag)
