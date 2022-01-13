# For The-TG-Bot-3.0
# By Priyam Kalra
# Parts of the code below is taken from other sources, the links to the
# sources is commented above the taken code

import asyncio
import os
import textwrap

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.utils import lightning_cmd

THUMB_IMAGE_PATH = "./thumb_image.jpg"


@borg.on(lightning_cmd(pattern="mmf ?(.*)"))
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Usage:- memify upper text ; lower text")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "Reply to a image/sticker.")
        return
    file = await borg.download_media(reply_message, Var.TEMP_DOWNLOAD_DIRECTORY)
    a = await event.reply("Memifying this image! (」ﾟﾛﾟ)｣ ")
    text = str(event.pattern_match.group(1)).strip()
    if len(text) < 1:
        return await a.edit("Usage:- memify upper text ; lower text")
    meme = await drawText(file, text)
    await event.client.send_file(event.chat_id, file=meme, force_document=False)
    os.remove(meme)
    await event.delete()
    await a.delete()


# Taken from https://github.com/UsergeTeam/Userge-Plugins/blob/master/plugins/memify.py#L64
# Maybe edited to suit the needs of this module


async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "resources/fonts/DejaVuSans.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, "webp")
    return webp_file


@bot.on(lightning_cmd(outgoing=True, pattern="mms ?(.*)"))
async def mim(event):
    if not event.reply_to_msg_id:
        await event.edit(
            "`Syntax: reply to an image with .mmf` 'text on top' ; 'text on bottom' "
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to a image/sticker/gif```")
        return
    await event.edit("`Downloading Media..`")
    if reply_message.photo:
        dls_loc = await bot.download_media(
            reply_message,
            "meme.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "meme.tgs",
        )
        os.system("lottie_convert.py --frame 0 -if lottie -of png meme.tgs meme.png")
        dls_loc = "meme.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "meme.mp4",
        )
        extractMetadata(createParser(video))
        os.system("ffmpeg -i meme.mp4 -vframes 1 -an -s 480x360 -ss 1 meme.png")
        dls_loc = "meme.png"
    else:
        dls_loc = await bot.download_media(
            reply_message,
            "meme.png",
        )
    await event.edit("```Memifying 🔸🔸🔸 ```")
    await asyncio.sleep(0.1)
    text = event.pattern_match.group(1)
    photo = await draw_meme(dls_loc, text)
    await event.client.send_file(event.chat_id, photo, reply_to=event.reply_to_msg_id)
    await event.delete()
    os.system("rm *.tgs *.mp4 *.png")
    os.remove(photo)


async def draw_meme(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(
        "userbot/helpers/styles/impact.ttf", int((70 / 640) * i_width)
    )
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad

    photu = "memify.png"
    photo = os.path.join(TEMP_DOWNLOAD_DIRECTORY, photu)
    img.save(photo, "png")
    return photo


CMD_HELP.update(
    {
        "memeify": ".mmf <text on top> ; <text on bottom> (reply to pic/sticker)\nUse - Memeify the pic/sticker."
    }
)
