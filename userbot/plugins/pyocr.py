try:
    from PIL import Image
except ImportError:
    import Image

import os

import pytesseract

from userbot.Config import Var
from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="read$"))
async def _(event):
    global images
    if event.fwd_from:
        return
    await event.edit("`Reading..`")
    if not os.path.isdir(Var.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        imagez = await borg.download_media(
            await event.get_reply_message(), Var.TMP_DOWNLOAD_DIRECTORY
        )
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
    results = pytesseract.image_to_string(Image.open(imagez))
    mk = f"<b><u> OCR </u></b> \n<b></u>Here is What I Can Read From This.</u></b> \n<code>{results}</code>"
    await event.edit(mk, parse_mode="HTML")
    if os.path.exists(results):
        os.remove(results)
