# Plugin made by @okay_retard && @hellboi_atul...
# If Gonna kang then keep credits..don't edit/remove these lines...
# else gay
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterMusic

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("sptfy ?(.*)"))
async def _(event):
    try:
        await event.client(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply(
            "You need to join [this](https://t.me/joinchat/DdR2SUvJPBouSW4QlbJU4g) group for this module to work.",
            link_preview=False,
        )
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter song name`")
        return
    chat = -1001271479322
    current_chat = event.chat_id
    current_msg = event.id
    try:
        async for event in event.client.iter_messages(
            chat, search=args, limit=1, filter=InputMessagesFilterMusic
        ):
            await event.client.send_file(current_chat, event, caption=event.message)
    except:
        await event.reply("`Song not found.`")
        return
    await event.client.delete_messages(current_chat, current_msg)
