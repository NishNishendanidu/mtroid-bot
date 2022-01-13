import os
import random
import re

import requests
from PIL import Image
from validators.url import url

from userbot import CMD_HELP, bot
from userbot.tweet import (
    bhautweet,
    johnnytweet,
    jtweet,
    miatweet,
    moditweet,
    sunnytweet,
)
from userbot.utils import lightning_cmd

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, "", inputString)


# for nekobot
async def trumptweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def purge():
    try:
        os.remove("gpx.png")
        os.remove("gpx.webp")
    except OSError:
        pass


# @register(outgoing=True, pattern=r"^\.trump(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="trump ?(.*)"))
async def trump(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to trump so he can tweet.`")
            return
    await event.edit("`Requesting trump to tweet...`")
    text = deEmojify(text)
    img = await trumptweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.johnny(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="johnny ?(.*)"))
async def johnny(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to Johnny so he can tweet.`")
            return
    await event.edit("`Requesting Johnny to tweet...`")
    text = deEmojify(text)
    img = await johnnytweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.bhau(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="bhau ?(.*)"))
async def bhau(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to Hindustani Bhau so he can tweet.`")
            return
    await event.edit("`Requesting Hindustani bhau to tweet...`")
    text = deEmojify(text)
    img = await bhautweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.sunny(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="sunny ?(.*)"))
async def sunny(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to Sunny so he can tweet.`")
            return
    await event.edit("`Requesting Sunny to tweet...`")
    text = deEmojify(text)
    img = await sunnytweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.joker(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="joker ?(.*)"))
async def j(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to 🃏 Joker so he can tweet.`")
            return
    await event.edit("`Requesting 🃏 Joker to tweet...`")
    text = deEmojify(text)
    img = await jtweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.modi(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="modi ?(.*)"))
async def modi(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to Modi so he can tweet.`")
            return
    await event.edit("`Requesting Modi to tweet...`")
    text = deEmojify(text)
    img = await moditweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.mia(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="mia ?(.*)"))
async def mia(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to Mia so he can tweet.`")
            return
    await event.edit("`Requesting Mia to tweet...`")
    text = deEmojify(text)
    img = await miatweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern=r"^\.cmm(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="cmm ?(.*)"))
async def cmm(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Give text for to write on banner!`")
            return
    await event.edit("`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    img = await changemymind(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


# @register(outgoing=True, pattern="^.type(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="type ?(.*)"))
async def type(animu):
    # """Generate random waifu sticker with the text!"""

    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("`No text given.`")
            return
    animus = [
        1,
        2,
        3,
        4,
        5,
        6,
        8,
        7,
        10,
        11,
        13,
        22,
        34,
        35,
        36,
        37,
        43,
        44,
        45,
        52,
        53,
    ]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}"
    )
    await sticcers[0].click(
        animu.chat_id,
        reply_to=animu.reply_to_msg_id,
        silent=True if animu.is_reply else False,
        hide_via=True,
    )
    await animu.delete()


# @register(outgoing=True, pattern="^.waifu(?: |$)(.*)")


@borg.on(lightning_cmd(outgoing=True, pattern="waifu ?(.*)"))
async def waifu(danish):
    # """Generate random waifu sticker with the text!"""

    text = danish.pattern_match.group(1)
    if not text:
        if danish.is_reply:
            text = (await danish.get_reply_message()).message
        else:
            await danish.answer("`No text given.`")
            return
    king = [32, 33, 37, 40, 41, 42, 58, 20]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(king)}{(deEmojify(text))}"
    )
    await sticcers[0].click(
        danish.chat_id,
        reply_to=danish.reply_to_msg_id,
        silent=True if danish.is_reply else False,
        hide_via=True,
    )
    await danish.delete()


# @register(outgoing=True, pattern=r"\.tweet(?: |$)(.*)")
@borg.on(lightning_cmd(outgoing=True, pattern="tweet ?(.*)"))
async def tweet(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await event.edit("`What should i tweet? Give your username and tweet!`")
                return
        else:
            await event.edit("What should i tweet? Give your username and tweet!`")
            return
    if "." in text:
        username, text = text.split(".")
    else:
        await event.edit("`What should i tweet? Give your username and tweet!`")
    await event.edit(f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    img = await tweets(text, username)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


@borg.on(lightning_cmd(pattern="tweetme(?: |$)(.*)"))
async def tweetme(okie):
    # """Creates random anime sticker!"""
    what = okie.pattern_match.group(1)
    if not what:
        if okie.is_reply:
            what = (await okie.get_reply_message()).message
        else:
            await okie.edit("`Tweets must contain some text, pero!`")
            return
    sticcers = await bot.inline_query("TwitterStatusBot", f"{(deEmojify(what))}")
    await sticcers[0].click(
        okie.chat_id,
        reply_to=okie.reply_to_msg_id,
        silent=True if okie.is_reply else False,
        hide_via=True,
    )
    await okie.delete()


CMD_HELP.update(
    {
        "tweet": ".tweet <username>.<tweet>"
        "\nUsage Create tweet with custom username.\n\n"
        ".trump <tweet>"
        "\nUsage Create tweet for Donald Trump.\n\n"
        ".sunny <tweet>"
        "\nUsage Create tweet for Sunny Leone.\n\n"
        ".johnny <tweet>"
        "\nUsage Create tweet for Johnny Sins.\n\n"
        ".bhau <tweet>"
        "\nUsage Create tweet for Hindustani bhau.\n\n"
        ".modi <tweet>"
        "\nUsage: Create tweet for Modi .\n\n"
        ".tweetme <tweet>"
        "\nUsage Create tweet from u in dark theme.\n\n"
        ".cmm <text>"
        "\nUsage Create banner for Change My Mind.\n\n"
        ".waifu <text>"
        "\nUsage Random anime girl stickers.\n\n"
        ".type <text>"
        "\nUsage random sticker is writing your text."
    }
)
