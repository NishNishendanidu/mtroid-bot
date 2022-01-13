# Plugin made by @hellboi_atul and bug fixes By Shivam Patel(Team Cobra)
# Give credits... Dont remove or edit these lines
# uses ytdl
# made for DARK COBRA userbot..

import asyncio
import json
import math
import os
import time

from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from uniborg.util import lightning_cmd
from userbot.utils import progress

try:
    from youtubesearchpython import SearchVideos
except:
    os.system("pip install pip install youtube-search-python")
    from youtubesearchpython import SearchVideos


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
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


@borg.on(lightning_cmd(pattern="vsong (.*)"))
async def download_video(v_url):
    pro = v_url
    sender = await pro.get_sender()
    me = await pro.client.get_me()
    pro1 = v_url.text
    if not sender.id == me.id:
        dc = await pro.reply("`processing, please weit...`")
    else:
        dc = await pro.edit("`processing, please weit...😍`")
    teamcobra = pro1[8:]
    if not teamcobra:
        return await dc.edit("`Error \nusage vsong <song name>`")
    search = SearchVideos(teamcobra, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        teamcobra = q[0]["link"]
    except:
        return await dc.edit("`failed to find your desired song`")
    type = "audio"
    await dc.edit("`Ok downloading your song🤓...`")
    if type == "audio":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        song = False
        video = True
    try:
        await dc.edit("`Fetching data, please wait..😋😍😎`")
        with YoutubeDL(opts) as darkcobra:
            darkcobra_data = darkcobra.extract_info(teamcobra)
    except DownloadError as error:
        await dc.edit(f"`{str(error)}`")
        return
    except ContentTooShortError:
        await dc.edit("`Oof the download content was too short😮🤐.`")
        return
    except GeoRestrictedError:
        await dc.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website🤔.`"
        )
        return
    except MaxDownloadsReached:
        await dc.edit("`Max-downloads limit has been reached😶.`")
        return
    except PostProcessingError:
        await dc.edit("`There was an error during post processing😐.`")
        return
    except UnavailableVideoError:
        await dc.edit("`sorry, media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await dc.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await dc.edit("`There was an error while fetching your query...`")
        return
    except Exception as e:
        await dc.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await dc.edit(
            f"`Preparing to upload your video song😎 `\
        \n**{darkcobra_data['title']}**\
        \nby *{darkcobra_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{darkcobra_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(darkcobra_data["duration"]),
                    title=str(darkcobra_data["title"]),
                    performer=str(darkcobra_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    v_url,
                    c_time,
                    "Uploading your video song😍..",
                    f"{darkcobra_data['title']}.mp3",
                )
            ),
        )
        os.remove(f"{darkcobra_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await dc.edit(
            f"`Preparing to upload your video song🤗❤ :`\
        \n**{darkcobra_data['title']}**\
        \nby *{darkcobra_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{darkcobra_data['id']}.mp4",
            supports_streaming=True,
            caption=darkcobra_data["title"],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{darkcobra_data['title']}.mp4"
                )
            ),
        )
        os.remove(f"{darkcobra_data['id']}.mp4")
        await dc.delete()
