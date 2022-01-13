# credit to kraken. madharchod plz dont copy
# Made By @veryhelful.
# thanks to kraken to give his plugin to edit and giving me idea
# all punjabi sahyri here are given by @Arwinder10


import asyncio
import random

from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@lightning_support_group"

sawan = bot.uid


@bot.on(lightning_cmd(pattern=r"plove$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Black-Lightning Making A Shayri.......")
    await asyncio.sleep(1.3)
    h = random.randrange(1, 9)
    if h == 1:
        await event.edit(
            f" Meri Kisi Gal Te Naraj Na Hovi,\nAkhian Nu Hanjua Nal Na Dhovi,\nMildi Ae Khushi Tenu Hasde Dekh Ke.\nSanu Maut Vi Aa Jave Ta Vi Na Rovi.\n\n\n✍️ {DEFAULTUSER}"
        )
    if h == 2:
        await event.edit(
            f"Dil Karda Ae Tere Kol Aa Ke Ruk Jaava,\nTeri Bukkal Wich Rakh Ke Sir Muk Jaava.\nHanju Ban Ke Digga Teriya Aakhaa Da,\nTere Bulla De Kol Aa Ke Sukk Jaava.\n\n\n✍️ {DEFAULTUSER}"
        )
    if h == 3:
        await event.edit(
            f"Tussi Hasde o sanu hasaan vaaste Tussi rone yo saanu rovaan vaaste Ek vaar rus ke ta vekho sohneyo Marr javange tuhanu manaan vaaste.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 4:
        await event.edit(
            f"Jo pani wang paviter, pyar tan unu kehnde ne.\n\njo ikk di ho ke reh je, naar tan unu kehnde ne.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 5:
        await event.edit(
            f"Khushboo teri yaari di saanu mehka jaandi hai,\n Teri har ik kitti hoyi gal saanu behka jaandi hai,\n Saah taan bahut der lagaande ne aun -jaan vich, \nHar saah ton pehle teri yaad aa jaandi hai.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 6:
        await event.edit(
            f"Yaadan tereiya nu bhullna hun okha ho gaya...... \nJo detey ne tu Gum ohna nu sehna okha ho geya..... \nTu jaan lagey keh deta bhull ja mainu....... \nHun unna gallan nu bhullana okha ho gaya......\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 7:
        await event.edit(
            f"Ae chand chamkna chad vii de \nTeri chandni saanu staandi ae \nTera varga hai usda chehra \nTenu vekh ke usdi yaad aandi ae.\n\n\n✍️{DEFAULTUSER}  "
        )
    if h == 8:
        await event.edit(
            f"Tutte hoye Pemane ch jaam nahi aunda, \nIshq de mariz nu araam nahi aunda, \nO Dil todan walya tu e te sochya hunda,\n Tutya hoya Dil kisi de kamm nahi aunda.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 9:
        await event.edit(
            f"Meri kisi gal te naraj na hovi, \nAkhian nu hanjua nal na dhovi, \nMildi a khushi tenu hasde dekh ke\n Sanu maut v aa jave ta v na rovi…\n\n\n✍️{DEFAULTUSER}"
        )


@bot.on(lightning_cmd(pattern=r"psad$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("@veryhelpful Making A Shayri.......")
    await asyncio.sleep(1.3)
    h = random.randrange(1, 22)
    if h == 1:
        await event.edit(
            f"Kithe miladi hai uhana akhan 👀 nu ninda,\njihana nu bevaphavam ne ruvaia 😭 hove..\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 2:
        await event.edit(
            f"Muhabata de anadaja vakhare-vakhare hude ne..\nKise ne ṭuṭa ke cahia te koi caha ke ṭuṭa gia..!!.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 3:
        await event.edit(
            f"Teri 👉narajagi 😔ika pala di vi dila❤️ sahida nai\nlaphaja ca nai dasa sakade kina tainu piara❤️ karade an\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 4:
        await event.edit(
            f"Mohabbat dila vica kujha isa tarha di hoṇo cahidi hai,\nKi uha hasila bhavem kise duje nu hove..\nPara kami usanu zidagi bhara meri hoṇi cahidi hai..!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 5:
        await event.edit(
            f"Tre kanan de vica gala kara pyra diam kara pyara dia,\nChaḍa sagana ni aja gala mana lai yara dia mana lai yara dia..😘😍\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 6:
        await event.edit(
            f"Aja kala di Love Story da ihi asul ai,\ntusi jisanu yada karake ro rahe ho uha kise hora nu Khush rakhaṇa ca Busy ai..\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 7:
        await event.edit(
            f"Phark ta bas soch da hai,\nnahi ta dosati vi pyar to ghaṭa nahin hund...\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 8:
        await event.edit(
            f"Jado tainu pahili vara vekhia ruhh ne avaza diti chala koi gunaha kar,\ntainu pata Mai muhabata kara lai..\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 9:
        await event.edit(
            f"Yaar badal ke vekho, tuhaade nawe yaara ch v ohna diyaa rooha jhalkdiyaa haungiyaa\npurane yaar bhulne v nahi te ohna di yaad v nahi auni\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 10:
        await event.edit(
            f"Tere pyaar waang saadhe iraade v kache nikale\nnaa chhadeyaa gya, ni dilo kadheyaa gyaa\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 11:
        await event.edit(
            f"Pyar v bahut azeeb aa\njis insaan nu paayea v na howe\nus nu v khohan da darr lageyaa rehnda\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 12:
        await event.edit(
            f"Tera door Jana seh na howe😒\nIshq enna naal tere ve🙈\nSathon hun reh na howe❤️..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 13:
        await event.edit(
            f"Saah lain naam tera sajjna🙈\nBina pal vi kithe sarda😕..!!\nRabb vang tenu poojan akhiyan😇\nTe dil ibadat karda😍..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 14:
        await event.edit(
            f"Tenu ki dassiye hun sajjna ve\nGhutt sabran vala kinjh pita e😣..!!\nAsa ikalleyan beh beh raatan nu\nTera naam har saah naal lita e❤️..!\nTenu khabran na khaure dil chandre diyan\nIshq tere de dhageyan naal sita e🙈..!!\nIkk jaan diwani hoyi teri e\nduja dil tere naawe kita e😍..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 15:
        await event.edit(
            f"Ki kehne haal dilan de ve\nKoi puche na koi dasse na🙌..!!\nSathon rabb vi mukh fereya\nTe jagg ton pal vi russe na💔..!!\nAsi sab nu muskaunde firde haan\nTe sanu dekh koi hasse na☹️..!!\nSade hassde mukh dekh sawal karan\nTe udaas hoyia nu koi puche na😟..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 16:
        await event.edit(
            f"Oh gaira de sang khul gaye hone aa\nnaweyaa de naal ghul gaye hone aa\ntu jinaa da khyaal dil cho ni kadhda\nArwinder O kadon de tainu bhulge hone a\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 17:
        await event.edit(
            f"Zaroori nahi ke jajhbaat kalam naal hi likhe jaan\nkhali panne v bahut byaan kar jande ne\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 18:
        await event.edit(
            f"Zindagi aini dukhi nahi aa ke marn nu jee kare\npar kujh lok dukh hi eaina dinde ne ke jeon da dil nahi karda\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 19:
        await event.edit(
            f"Saadhe ute aapna hak jataun wala koi nahi\ntu ruse taa tainu mna la ge\npar asi rusiye kive sanu manaun wal koi nahi\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 20:
        await event.edit(
            f"Bhull gaya jiona loka layi\nHun aapde khayal vas lainda e..!!\nShad k mehfilan duniya diyan\nIkalleyan ja kite behnda e..!!\nKhaure vigad gaya ja sudhar gaya\nPar nakhre na hun kise de sehnda e..!!\nHun nhi krda dil kise naal mohobbat nu\nBs time pass de zariye labbda rehnda e..!!✍️{DEFAULTUSER}"
        )
    if h == 21:
        await event.edit(
            f"Bekadri kar rukhe ho tur Jana\nEda nahio chahan hundiya..!!\nBefikre ho nhi saunde sajjna\nJinna nu parwahan hundiya..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 22:
        await event.edit(
            f"Ajh v ohi chehra e\npar tera dil na mera e\npata ni kadon tak rehna\nmere dil vich naam jo tera e\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 22:
        await event.edit(
            f"Change hon ja maade sanu fark nhi painda\nO asi taan izzat rakhde aan dil ch\nSanu chahun valeyan layi vi te bhulaun valeyan layi vi..!!\nJee sadke aawe jihne auna\nTe jaan vala ja sakde\nKyunki aawdi zindagi de boohe khulle rakhne ne asi\nAun valeyan layi vi te jaan valeyan layi vi🙏😎..!!\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 22:
        await event.edit(
            f"Sabh da dilo hi karida ae,\nkoi varte ja parkhe oh gal wakhri\n\n\n✍️{DEFAULTUSER}"
        )
