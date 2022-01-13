# Originally by @NOOB_GUY_OP
# I think its first for DARKCOBRA
"""Syntax: .afk REASON"""
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from userbot import CMD_HELP
from userbot.utils import lightning_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}

# Originally by @NOOB_GUY_OP
# I think its first for DARKCOBRA


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".mafk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        shite = await borg.send_message(
            event.chat_id,
            "__Back alive!__\n**No Longer afk.**\n `Was afk for:``"
            + total_afk_time
            + "`",
            file=pic,
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE \nSet AFK mode to False\n"
                + "__Back alive!__\n**No Longer afk.**\n `Was afk for:``"
                + total_afk_time
                + "`",
                file=pic,
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602 # Originally by @NOOB_GUY_OP
                # I think its first for DARKCOBRA
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of afk functionality "
                + "Sar please set it.\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "mafk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None  # Originally by @NOOB_GUY_OP
        # I think its first for DARKCOBRA
        message_to_reply = (
            f"__My Master Has Been In afk since__ `{total_afk_time}`\nWhere He Is: I don't know dear friend..he is a too busy person "
            + f"\n\n__I can't guarantee you that when he will come..__\n**REASON**: {reason}"
            if reason
            else f"**Heyy!**\n__I am currently unavailable. Since when, you ask? For {total_afk_time} I think.__\n\nWhen will I be back? Soon __Whenever I feel like coming back__**(o(^▽^)o)**  "
        )
        msg = await event.reply(message_to_reply, file=pic)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(lightning_cmd(pattern=r"mafk (.*) (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    global pic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()  # Originally by @NOOB_GUY_OP
    # I think its first for DARKCOBRA
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    pic = event.pattern_match.group(2)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )  # Originally by @NOOB_GUY_OP
        # I think its first for DARKCOBRA
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason} {pic}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id,
                f"**I shall be Going afk!** __because ~ {reason}__",
                file=pic,
            )
        else:
            await borg.send_message(event.chat_id, f"**I am Going afk!**", file=pic)
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#MAFKTRUE \nSet MAFK mode to True, and Reason is {reason}",
                file=pic,
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CMD_HELP.update(
    {
        "mafk": "__**PLUGIN NAME :** Afk__\
\n\n📌** CMD ➥** `.mafk` [Optional Reason]\
"
    }
)
