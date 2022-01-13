from userbot.utils import *
import cv2
import pytesseract

import urllib.request
import urllib

import webbrowser
import asyncio
import numpy as np
import os
import pandas as pd
from pathlib import Path

import requests


import re
from userbot import ALIVE_NAME
import pygments
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter




from math import ceil
from userbot import bot
from userbot.thunderconfig import Config

DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)
path = "./check/"
if not os.path.isdir(path):
    os.makedirs(path)
def url_to_image(url):
    resp = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(resp)
    image = np.asarray(bytearray(con.read()), dtype="uint8")
    image2 = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image2

def img2text(URL):
    if re.findall('^http', URL):
        im = url_to_image(URL)
    else:
        img = cv2.imread(URL)
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    config = ('-l eng --oem 1 --psm 6')
    text = pytesseract.image_to_string(im, config=config)
    text2 = text.rstrip('\n')
    return (text2)

def img2textdir(dirpath):
    files = []
    for file in os.listdir(dirpath):
        if file.endswith('.jpg') or file.endswith('.png'):
            files.append(os.path.join(dirpath, file))
    texts=[]
    names=[]
    for i in files:
        text=img2text(i)
        texts.append(text)
        names.append(i)
    translation={'Image':names, 'Text':texts}
    df=pd.DataFrame(data=translation)
    df.to_excel(dirpath+'/img2text.xlsx', sheet_name = 'ImagestoText')
    return df
    
    
    
@borg.on(lightning_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    try:
        downloaded_file_name = (
            await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/plugins/",  # pylint:disable=E0602
            )
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            krish_blac = path1.stem
            load_module(krish_blac.replace(".py", ""))
            await event.edit(f"Wait Installing.... ")
            await asyncio.sleep(2)
            await event.edit(
                "{}SucessFully Installed ....".format(
                    os.path.basename(downloaded_file_name)
                )
            )
        else:
            os.remove(downloaded_file_name)
            await event.edit("**Master You Already Have This Plugin .**")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
        os.remove(downloaded_file_name)
    await asyncio.sleep(4)

 
    await event.delete() 
    
