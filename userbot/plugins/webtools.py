#Made by @Midhun_xD real owner @Midhun_xD 
#ported To javes 3.0 @ShivaM_PateL
#nothing BY Me @CRiMiNaL786

import requests
import os 
from re import match
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY","./downloads")
import aiofiles
import asyncio
from iplookup import iplookup
from selenium import webdriver
from youtube_search import YoutubeSearch
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from userbot import CMD_HELP
from userbot.utils import lightning_cmd, edit_or_reply, sudo_cmd
from userbot.Config import Var
from userbot.thunderconfig import Config
from var import Var
from userbot.utils import lightning_cmd





@borg.on(lightning_cmd(pattern="wshot ?(.*)"))
@borg.on(sudo_cmd(pattern="wshot ?(.*)", allow_sudo=True))
async def wshot(message):
    king= message.text
    amaan=king[7:]

    link_match = match(r"\bhttps?://.*\.\S+", amaan)
    if not link_match:
        await message.edit("`I need a valid link to take screenshots from.`")
        return
    link = link_match.group()
    await message.edit("`Processing ...`")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome((ChromeDriverManager().install()),chrome_options=chrome_options)
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await message.edit(
        f"`Generating screenshot of the page...`"
        f"\n`Height of page = {height}px`"
        f"\n`Width of page = {width}px`"
        f"\n`Waiting ({int(wait_for)}s) for the page to load.`"
    )
    await asyncio.sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    driver.close()
    message_id = message.message.id
    reply = await message.get_reply_message()
    if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
    file_path = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "wshot.png")
    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(im_png)
    await asyncio.gather(
        message.delete(),
        message.client.send_file(
            message.chat_id,
            file_path,
            caption=link,
            force_document=False,
            reply_to=message_id,
        ),
    )
    os.remove(file_path)
    driver.quit()


@borg.on(lightning_cmd(pattern="lp ?(.*)"))
@borg.on(sudo_cmd(pattern="lp ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfbro = await edit_or_reply(event, "Wait Fetching Website Info")
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain=" + gone
        await event.edit(
            "Fecthing Website Info ! Stay Tuned. This may take some time ;)"
        )
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (
            f'Domain Name => {sed["domain"]} \nCreated On => {sed["create_date"]} \nDomain ID => {sed["domain_id"]} \nHosted ON => {kek["url"]}'
            f'\nLast updated => {sed["update_date"]} \nExpiry Date => {sed["expire_date"]} \nDomain Age => {sed["domain_age"]}'
            f'\nOwner => {km["name"]} \nCountry => {km["country"]} \nState => {km["region"]}'
            f'\nPhone Number => {km["phone"]} \nDomain Ip => {okthen}'
        )
        await tfbro.edit(sedlyf)
    except Exception:
        await tfbro.edit(f"Something Went Wrong. MayBe Website Wrong.")


@borg.on(lightning_cmd(pattern="bin ?(.*)"))
@borg.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfsir = await edit_or_reply(event, "Wait Fetching Bin Info")
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (
            f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
            f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
            f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
            f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
            f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n"
        )
        await tfsir.edit(data_is, parse_mode="HTML")
    except:
        await tfsir.edit("Not a Valid Bin Or Don't Have Enough Info.")


@borg.on(lightning_cmd(pattern="iban ?(.*)"))
@borg.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        tfhm = await edit_or_reply(event, "Wait Fetching IBAN Info")
        banks = lol["bankData"]
        kek = (
            f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
            f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
            f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
            f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
            f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
            f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
            f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n"
        )
        await tfhm.edit(kek, parse_mode="HTML")
    except:
        await tfhm.edit(f"Invalid IBAN Or Doesn't Have Enough Info")


@borg.on(lightning_cmd(pattern="gitdl ?(.*)"))
@borg.on(sudo_cmd(pattern="gitdl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        kekman = await edit_or_reply(event, "Fetching Repo")
        inputs = event.pattern_match.group(1)
        sed = event.pattern_match.group(1)
        if sed:
            if " " in sed:
                stark = inputs.split(" ", 2)
        gitusername = stark[0]
        gitrepo = stark[1]
        gitbranch = stark[2]
        link = f"https://github.com/{gitusername}/{gitrepo}/archive/{gitbranch}.zip"
        await kekman.edit("Uploading... Stark Tuned.")
        await event.delete()
        await borg.send_file(event.chat_id, file=link, caption="You Repo Achieve File.")
    except:
        await borg.send_message(
            event.chat_id, "**Usage** : `.gitdl <gitusername> <gitrepo> <gitbranch>`"
        )


@borg.on(lightning_cmd(pattern="yts ?(.*)"))
@borg.on(sudo_cmd(pattern="yts ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        fin = event.pattern_match.group(1)
        stark_result = await edit_or_reply(event, "Fectching Result this May Take Time")
        results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
        noob = "<b>YOUTUBE SEARCH</b> \n\n"
        for moon in results:
            hmm = moon["id"]
            kek = f"https://www.youtube.com/watch?v={hmm}"
            stark_name = moon["title"]
            stark_chnnl = moon["channel"]
            total_stark = moon["duration"]
            stark_views = moon["views"]
            noob += (
                f"<b><u>VIDEO-TITLE</u></b> ➠ <code>{stark_name}</code> \n"
                f"<b><u>LINK</u></b> ➠ <code>{kek}</code> \n"
                f"<b><u>CHANNEL</u></b> ➠ <code>{stark_chnnl}</code> \n"
                f"<b><u>DURATION</u></b> ➠ <code>{total_stark}</code> \n"
                f"<b><u>TOTAL-VIEWS</u></b> ➠ <code>{stark_views}</code> \n\n"
            )
        await stark_result.edit(noob, parse_mode="HTML")
    except:
        await event.edit("Some Thing Went Wrong.")

CMD_HELP.update({"wshot":"\n\n.wshot link "})
