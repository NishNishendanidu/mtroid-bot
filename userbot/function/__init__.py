#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import json
import math
import os
import re
import shlex
import subprocess
import time
from os.path import basename
from typing import List, Optional, Tuple

import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont
import requests
from bs4 import BeautifulSoup as bs
from pymediainfo import MediaInfo
from telethon.tl.types import MessageMediaPhoto
from validators.url import url

BASE_URL = "https://isubtitles.org"
from userbot.thunderconfig import Config

sedpath = Config.TMP_DOWNLOAD_DIRECTORY
from userbot import logging

logger = logging.getLogger("[--WARNING--]")
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


# Thanks To Userge-X
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current != total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]

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
# LOL
def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


# Thanks To Userge-X
# Ported By @STARKXD
async def convert_to_image(event, borg):
    lmao = await event.get_reply_message()
    if not (
        lmao.gif
        or lmao.audio
        or lmao.voice
        or lmao.video
        or lmao.video_note
        or lmao.photo
        or lmao.sticker
    ):
        await event.edit("`Format Not Supported.`")
        return
    else:
        try:
            c_time = time.time()
            downloaded_file_name = await borg.download_media(
                lmao.media,
                sedpath,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "`Downloading...`")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(
                "Downloaded to `{}` successfully.".format(downloaded_file_name)
            )
    if not os.path.exists(downloaded_file_name):
        await event.edit("Download Unsucessfull :(")
        return
    if lmao and lmao.photo:
        lmao_final = downloaded_file_name
    elif lmao.sticker and lmao.sticker.mime_type == "application/x-tgsticker":
        rpath = downloaded_file_name
        image_name20 = os.path.join(sedpath, "SED.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {downloaded_file_name} {image_name20}"
        stdout, stderr = (await runcmd(cmd))[:2]
        os.remove(rpath)
        lmao_final = image_name20
    elif lmao.sticker and lmao.sticker.mime_type == "image/webp":
        pathofsticker2 = downloaded_file_name
        image_new_path = sedpath + "image.png"
        os.rename(pathofsticker2, image_new_path)
        if not os.path.exists(image_new_path):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        lmao_final = image_new_path
    elif lmao.audio:
        sed_p = downloaded_file_name
        hmmyes = sedpath + "stark.mp3"
        imgpath = sedpath + "starky.jpg"
        os.rename(sed_p, hmmyes)
        await runcmd(f"ffmpeg -i {hmmyes} -filter:v scale=500:500 -an {imgpath}")
        os.remove(sed_p)
        if not os.path.exists(imgpath):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        lmao_final = imgpath
    elif lmao.gif or lmao.video or lmao.video_note:
        sed_p2 = downloaded_file_name
        jpg_file = os.path.join(sedpath, "image.jpg")
        await take_screen_shot(sed_p2, 0, jpg_file)
        os.remove(sed_p2)
        if not os.path.exists(jpg_file):
            await event.edit("`Couldn't Fetch. SS`")
            return
        lmao_final = jpg_file
    await event.edit("`Almost Completed.`")
    return lmao_final

def lightning_convert_to_img(image, filename=None):
    filename = filename or os.path.join("./temp/", "temp.jpg")
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(filename, "jpeg")
    os.remove(image)
    return filename

# Thanks To Userge-X
async def crop_vid(input_vid: str, final_path: str):
    media_info = MediaInfo.parse(input_vid)
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    if aspect_ratio != 1:
        crop_by = width if (height > width) else height
        os.system(f'ffmpeg -i {input_vid} -vf "crop={crop_by}:{crop_by}" {final_path}')
        os.remove(input_vid)
    else:
        os.rename(input_vid, final_path)


# Thanks To Userge-X
async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    """ take a screenshot """
    logger.info(
        "[[[Extracting a frame from %s ||| Video duration => %s]]]",
        video_file,
        duration,
    )
    ttl = duration // 2
    thumb_image_path = path or os.path.join(sedpath, f"{basename(video_file)}.jpg")
    command = f'''ffmpeg -ss {ttl} -i "{video_file}" -vframes 1 "{thumb_image_path}"'''
    err = (await runcmd(command))[1]
    if err:
        logger.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


# Thanks To @HeisenbergTheDanger, @xditya
async def fetch_feds(event, borg):
    fedList = []
    await event.edit("`Fetching Your FeD List`, This May Take A While.")
    async with borg.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await bot_conv.send_message("/myfeds")
        await asyncio.sleep(3)
        response = await bot_conv.get_response(timeout=300)
        await asyncio.sleep(3)
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("`Try again after 5 mins.`")
            return
        elif "make a file" in response.text:
            await event.edit(
                "`Boss, You Real Peru. You Are Admin in So Many Feds. WoW!`"
            )
            await asyncio.sleep(6)
            await response.click(0)
            await asyncio.sleep(6)
            fedfile = await bot_conv.get_response()
            await asyncio.sleep(3)
            if fedfile.media:
                downloaded_file_name = await borg.download_media(fedfile, "fedlist")
                await asyncio.sleep(6)
                file = open(downloaded_file_name, "r")
                lines = file.readlines()
                for line in lines:
                    try:
                        fedList.append(line[:36])
                    except BaseException:
                        pass
                # CleanUp
                os.remove(downloaded_file_name)
        else:
            In = False
            tempFedId = ""
            for x in response.text:
                if x == "`":
                    if In:
                        In = False
                        fedList.append(tempFedId)
                        tempFedId = ""
                    else:
                        In = True

                elif In:
                    tempFedId += x
    await event.edit("`FeD List Fetched SucessFully.`")
    return fedList


# Thanks To https://github.com/CW4RR10R/yify-grabber/blob/master/yify/__init__.py
async def get_yiffy(imdb_id, event, borg):
    url = f"https://yts-subs.com/movie-imdb{imdb_id}"
    page = BeautifulSoup(requests.get(url).content, "html.parser")
    content = page.find("div", {"class": "table-responsive"})
    if content:
        await event.edit("Fetching all languages and its ratings...")
        lang = "English"
        movies = [
            [
                movie.find("span", {"class": "label"}).get_text(),
                "https://yts-subs.com" + movie.find("a")["href"],
            ]
            for movie in content.find_all("tr", {"class": "high-rating"})
            if movie.find("span", {"class": "sub-lang"}).get_text() == lang
            and movie.find("span", {"class": "label"})
        ]
        list_eng = {movie[1]: int(movie[0]) for movie in movies}
        await event.edit(f"Selecting top rated {lang} subtitle")
        top_rated = max(list_eng, key=list_eng.get)
        html = BeautifulSoup(requests.get(top_rated).content, "html.parser")
        file_name = (
            html.find("div", {"class": "col-xs-12", "style": "margin-bottom:15px;"})
            .get_text()
            .strip()
        )
        dwn_url = html.find("a", {"class": "btn-icon download-subtitle"})["href"]
        dwn_dir = sedpath + file_name.replace("/", " ") + ".zip"
        await event.edit(f"Found {file_name}")
        await event.edit(f"Downloading to my local. Please Wait")
        with open(dwn_dir, "wb") as f:
            f.write(requests.get(dwn_url).content)
    else:
        dwn_dir = None
        file_name = None
        dwn_url = None
        await event.edit("`No Movies Found.`")
    return dwn_dir, file_name, dwn_url
