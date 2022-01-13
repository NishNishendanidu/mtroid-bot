#plugin by @Rishisuperyo @Parmatin
#Some constant credits go to Varun and Ricksuperbro
#kanger = kang wity credits else bhenchod macchar ki jaat teri chut gand ek kardunga saale
#ha benjo tu teko hi bol rah 🤣🤣
#usage .hpind
#OP BOLTE
import asyncio
import random
from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd
#Constant
yo = "https://telegra.ph/file/11198632a306a03723d9d.mp4"
yo2 = "https://telegra.ph/file/72d3a8c9d53b5c2ca927c.mp4"
yo3 = "https://telegra.ph/file/4470a8593dbd2d181beca.mp4"
#SED I HAVE NO MORE IF U HAVE I WILL UPDATE IT :)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"
remd = bot.me.id
cap =f"YEAH BRO 𝙷𝙰𝙿𝙿𝚈 𝙸𝙽𝙳𝙴𝙿𝙴𝙽𝙳𝙴𝙽𝙲𝙴 𝙳𝙰𝚈🇮🇳 TO [{DEFAULTUSER}](tg://user?id={remd})\n DONT FORGET TO CLICK 👉[dis](http://wish-style.com/?n=Rishisuperyo)👈\n ~ @Rishisuperyo"
#bruh

@borg.on(lightning_cmd(pattern=r"hpind", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("STARTING CELEBRATION OF 𝙷𝙰𝙿𝙿𝚈 𝙸𝙽𝙳𝙴𝙿𝙴𝙽𝙳𝙴𝙽𝙲𝙴 𝙳𝙰𝚈🇮🇳 ")
    await asyncio.sleep(3)
    s = random.randrange(1, 3)
    if s == 1:
        await event.edit("THANKS TO OUR SOLDIERS WHO ARE PROTECTING US IN BORDER , JAI HIND🇮🇳")
    if s == 2:
        await event.edit(
        	     "BEFORE 74 YEARS WE GOT FREEDOM BY OUR FREEDOM FIGHTER, JAI HIND🇮🇳 "
        )
    if s == 3:
        await event.edit(
        	     "WE SHOULD TAKE CARE OF OUR COUNTRY AND THANKS TO OUR SOLDIERS, JAI HIND🇮🇳"
        )
    await bot.send_message(event.chat_id, "Please don't blink ur eyes a surprise iz coming")
    await asyncio.sleep(4)            
    f = random.randrange(1,3)
#try
    if f == 1:
       await bot.send_file(
        event.chat_id, file=yo ,caption=cap, link_preview=False
        )   
    if f == 2:
       await bot.send_file(
        event.chat_id, file=yo2 ,caption=cap, link_preview=False
       )
    if f == 3:
       await bot.send_file(
        event.chat_id, file=yo3 ,caption=cap, link_preview=False
       )
