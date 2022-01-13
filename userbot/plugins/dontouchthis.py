"""
Files Batch Uploader Plugin for userbot.
usage:- .upb 
Note:- set TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870	
"""
import os

from uniborg.util import lightning_cmd
from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"upb"))
async def batch_upload(event):
    if event.fwd_from:
        return
    temp_dir = Config.TEMP_DIR
    if os.path.exists(temp_dir):
        files = os.listdir(temp_dir)
        files.sort()
        await event.edit("Uploading Files on Telegram...")
        for file in files:
            required_file_name = temp_dir + "/" + file
            print(required_file_name)
            await borg.send_file(event.chat_id, required_file_name, force_document=True)
    else:
        await event.edit("Directory Not Found.")
        return
    await event.edit("Successfull.")
