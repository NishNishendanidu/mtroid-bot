import os

from glitch_this import ImageGlitcher
from telethon.tl.types import MessageMediaPhoto

from userbot.utils import lightning_cmd, sudo_cmd

glitcher = ImageGlitcher()
DURATION = 200  # Set this to however many centiseconds each frame should be visible for
LOOP = 0  # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop
sedpath = "./Anmol-dot283/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@borg.on(lightning_cmd(pattern=r"glitch"))
@borg.on(sudo_cmd(pattern=r"glitch", allow_sudo=True))
async def glitch(event):
    sed = await event.get_reply_message()
    okbruh = await event.edit("`Gli, Glitchiiingggg.....`")
    if isinstance(sed.media, MessageMediaPhoto):
        photolove = await borg.download_media(sed.media, sedpath)
    elif "image" in response.media.document.mime_type.split("/"):
        photolove = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("`Reply To Image`")
        return
    fmt = "gif"
    pathsn = f"./Anmol-dot283/@blacklightningot.{fmt}"
    glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
    glitch_imgs[0].save(
        pathsn,
        format="GIF",
        append_images=glitch_imgs[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    await borg.send_file(event.chat_id, pathsn)
    await okbruh.delete()
    for starky in (pathsn, photolove):
        if starky and os.path.exists(starky):
            os.remove(starky)
