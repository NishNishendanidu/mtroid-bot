# By @keinshin for Black Lightning
# If you steal this without credits You will be the geyest gey ever in the world that you will suck my dick.
import asyncio

from .. import ALIVE_NAME
from ..utils import lightning_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@borg.on(lightning_cmd(pattern="chutiye$"))
async def _(event):
    if event.fwd_from:
        return
    lightning_anmation_interval = 4
    ttl = range(0, 100)
    await event.edit("Chutiye Saade Hue...")
    chars = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
            "Gadha, Bakland- Idiot",
            "Lauda, Lund- Penis, dick, cock",
            "Hijra- Gay, Transsexual",
            "Kuttiya- Bitch",
            "Paad- FART",
            "Randi- HOOKER",
            "Saala kutta- Bloody dog",
            "Saali kutti- Bloody bitch",
            "Tatti- Shit",
            "Kamina- bastard",
            "Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
            "Chut ke dhakkan- Pussy lid",
            "Chut ke gulam- Pussy whipped",
            "Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
            "Choot marani ka- Pussy whipped",
            "Choot ka baal- Hair of vagina",
            "Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
            "Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
            "Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
            "Chipkali ke chut ke pasine- Sweat of reptiles cunt",
            "Chipkali ki bhigi chut- Wet pussy of a wall lizard",
            "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
            "Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
            "Cuntmama- Vaginal uncle",
            "Chhed- Vagina,Hole",
            "Apni gaand mein muthi daal- Put your fist up your ass",
            "Apni lund choos- Go and suck your own dick",
            "Apni ma ko ja choos- Go suck your mom",
            "Bhen ke laude- Sister’s dick",
            "Bhen ke takke: Go and suck your sister’s balls",
            "Abla naari tera buble bhaari-  woman, your tits are huge",
            "Bhonsri-Waalaa- You fucker",
            "Bhadwe ka awlat- Son of a pimp",
            "Bhains ki aulad- Son of a buffalo",
            "Buddha Khoosat- Old fart",
            "Bol teri gand kaise maru- let me know how to fuck you in the ass",
            "Bur ki chatani- Ketchup of cunt",
            "Chunni- Clit",
            "Chinaal- Whore",
            "Chudai khana- Whore house",
            "Chudan chuda- Fucking games",
            "Chut ka pujari- pussy worshipper",
            "Chut ka bhoot- Vaginal Ghost",
            "Gaand ka makhan- Butter from the ass",
            "Gaand main lassan- Garlic in ass",
            "Gaand main danda- Stick in ass",
            "Gaand main keera- Bug up your ass",
            "Gaand mein bambu- A bambooup your ass",
            "Gaandfat- Busted ass",
            "Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
            "Hazaar lund teri gaand main-Thousand dicks in your ass",
            "Jhat ke baal- Pubic hair",
            "Jhaant ke pissu- Bug of pubic hair",
            "Kadak Mall- Sexy Girl",
            "Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
            "Khotey ki aulda- Son of donkey",
            "Kutte ka awlat- Son of a dog",
            "Kutte ki jat- Breed of dog",
            "Kutte ke tatte- Dog’s balls",
            "Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
            "Lavde ke bal- Hair on your penis",
            "muh mei lele: Suck my dick",
            "Lund Chus: Suck dick",
            "Lund Ke Pasine- Sweat of dick",
            "Meri Gand Ka Khatmal: Bug of my Ass",
            "Moot, Mootna- Piss off",
            "Najayaz paidaish- Illegitimately born",
            "Randi khana- whore house",
            "Sadi hui gaand- Stinking ass",
            "Teri gaand main kute ka lund- A dog’s dick in your ass",
            "Teri maa ka bhosda- Your mother’s breasts",
            "Teri maa ki chut- Your mother’s pussy",
            "Tere gaand mein keede paday- May worms infest your ass-hole",
            "Ullu ke pathe- Idiot",
        ]

    for i in ttl:  

        await asyncio.sleep(lightning_anmation_interval)
        await event.edit(
            chars[i % 100], link_preview=True
        )  
