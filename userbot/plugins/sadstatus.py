""" Sing a song... 
    Command .sadsatutsr

    By @veryhelpful"""

import asyncio
import random

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"shayri$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Black-Lightning Making A Shayri for u.......")
    await asyncio.sleep(2)
    s = random.randrange(1, 15)
    if s == 1:
        await event.edit(
            "HAMNE TOH BSS DOST KO HI BEWAFA SAMJHA THHA...\nYAHAAN SACCHA PYAAR V SAATH NHI DIYA🥱🥱"
        )
    if s == 2:
        await event.edit("Love leads to death 🥱🥱\nOr to a living dead 🥱🥱")
    if s == 3:
        await event.edit(
            "BAATEN TU KABHI YE NA BHULNA.....\nKOI TERE KAARANN HAI..MRR RHA 🥱🥱🥱🥱"
        )
    if s == 4:
        await event.edit(
            "Ae dost Tere jaise log ko kaat k fekk dange hm\nMeri taraf aae her toofan ko Teri taraff bhej dange hm...\nLekhin tune Jo saath chorrda hamara ......\nKsm SE badnaam krke tujhe nya dost....\n dhoondh lange hum🥱🥱🥱🥱"
        )
    if s == 5:
        await event.edit(
            "Bde ajeeb Hain ye Zindagi k raaste.........\nAnjaane modd pe log Mill jaate Hain...khhud ko apna BTA k.....chorrrd jaate Hain...\n. KRTE hai. H baat (Zindagi bhar saath rahenge) interest khtm hone prr......zinda LAASH BNA jaate h🥱🥱🥱"
        )
    if s == 6:
        await event.edit(
            "Dill jaisa thha waisa hi reh jaata......\nJitne dard thhey UTNE kaafi thhey.......\nZindagi aap me aake aur tadpaa diya.........\nMillla kya u badnaam krke ....zinda LAASh...... DIYA🙃🙃"
        )
    if s == 7:
        await event.edit(
            "DARD SE IS KADAR DOSTI HO GYI.......\nZINDAGI BEDARD SI HO GYI.......\nJALL  GAY WO ASHIYANA.......JO KABHI BNA HI NHI THHA......\nROSHNI TOH CHORRDO..........\nGHAR MEIN JO MOMABATTIE  THHI WO V KHTM HO GYI.........🥱🥱"
        )
    if s == 8:
        await event.edit(
            "Zindagi barbaad hai...... Zindagi SE pyaar na Karo.......\nHo raat toh Dinn ka intezaar na Karo.......\nWo Pall v aaega....jiss pal ka INTEZAAR na  ho aako.....\nPRRR uspe kabhi aitbaar na Karo........🥱🥱"
        )
    if s == 9:
        await event.edit(
            "Dard k saath rhte hue v dosti nhi Hui\nZindagi bedard si hote hue v nhi Hui\nAashiyana toh jall gya\nPrr  Roshni nhi Hui ..........❤️"
        )
    if s == 10:
        await event.edit(
            "ME: DUNIYA ME AISI KYA CHEEZ HAI JO FREE MEI MILTI HAI............\nMAH HEART : DHOKHA "
        )
    if s == 11:
        await event.edit(
            "JO INSAAN AAPKO TADAPTA HUA ....ROTA CHORRD DE NA.......... TOH SAMAJH LENA WO KABHI AAPSE \nPYAAR NHI KRR SKTA.....AGAR KOI PYAAR KAREGA NA......\nTOH WO KABHI AAPKO AISEY NHI CHORRDEGA.......🥱🥱"
        )
    if s == 12:
        await event.edit(
            "TOOTE HAIN.....ES TARAH DILL ......\nAWAAZ TKK NA AAI....\nHUM JAISEY JEE RHE H.....\nKOI JEE K TOH BTAAE....🙃🙃"
        )
    if s == 13:
        await event.edit(
            "AANKHON ME AANSU LEKE........\nHOTHON SE MUSKURAAE................\nHUM JAISEY JEE RHE HAIN.......\nKLI JEE K TOH BTAAE...🙃🙃"
        )
    if s == 14:
        await event.edit(
            "TUJHE KAISEY PTA NA CHALAA.................\nK MAIN TENU PYAAR KRR Di AAN...........\nTUJHE KAISEY PTA NA CHALAA......\nK TERA INTEZAAR KRR DI AAN........🙃"
        )
    if s == 15:
        await event.edit(
            "MTT CHORRDNA KISIKO USKE HAAL PE.......\nHO SKTA H.......\nAAPKE ALAWA  USKE PAAS AUR KOI NA HO.......🙃🙃"
        )
