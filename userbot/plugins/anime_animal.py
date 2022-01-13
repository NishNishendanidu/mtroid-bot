"""
MADE BY @Stark_TVL 
bug fixed by @Melloxd
"""

from userbot.utils import lightning_cmd

M = (
    "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈▏\n"
)


@borg.on(lightning_cmd(pattern=r"spong"))
async def kek(admin):
    await borg.edit(M)

    D = (
        "╭━┳━╭━╭━╮╮\n"
        "┃┈┈┈┣▅╋▅┫┃\n"
        "┃┈┃┈╰━╰━━━━━━╮\n"
        "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
        "╲┃┈┈┈┈╭━┳━━━━╯\n"
        "╲┣━━━━━━┫\n"
    )


@borg.on(lightning_cmd(pattern=r"dog"))
async def dog(dog):
    await dog.edit(D)
    P = (
        "┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
        "┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
    )


F = (
    " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈\n"
)

E = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈\n"
)

H = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈HOMER\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n"
)


@borg.on(lightning_cmd(pattern=r"fox"))
async def fox(fox):
    await fox.edit(F)


@borg.on(lightning_cmd(pattern=r"elephant"))
async def elephant(elephant):
    await elephant.edit(E)


@borg.on(lightning_cmd(pattern=r"homer"))
async def homer(homer):
    await homer.edit(H)


@borg.on(lightning_cmd(pattern=r"pig"))
async def pig(pig):
    await pig.edit(P)



from userbot import CMD_HELP
CMD_HELP.update(
    {
     "| | animals | |": "`.pig`\
     \n**USAGE**: ` Pig Face.`\
     \n\n| animals |: `.homer`\
     \n**USAGE**: ` Animation plugin.`\
     \n\n| animals |: `.spong`\
     \n**USAGE**: `Spongebob face creator.`\
     \n\n| animals |: `.elephant`\
     \n**USAGE**: `Elephant Art  plugin.`\
     \n\n| animals |: `.fox` / `text`\
     \n**USAGE**:  `Fox Ascii Maker Plugin`"
    }
)