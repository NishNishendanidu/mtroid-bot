# keep credit if u gonna edit or kang it
# without creadit copy paster mc
# creadits to  sawan(@veryhelpful) learned from kraken


import asyncio

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern="mst ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("mst hu bbro ")
        await asyncio.sleep(1)
        await event.edit("╔═╦═╗╔══╗╔══╗\n║║║║║║══╣╚╗╔╝\n║║║║║╠══║─║║─\n╚╩═╩╝╚══╝─╚╝─")


@borg.on(lightning_cmd(pattern="gmg ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("good morning ")
        await asyncio.sleep(1)
        await event.edit("╔══╗╔═╦═╗\n║╔═╣║║║║║\n║╚╗║║║║║║\n╚══╝╚╩═╩╝")


@borg.on(lightning_cmd(pattern="good ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "╔══╗╔═╗╔═╗╔══╗\n║╔═╣║║║║║║╚╗╗║\n║╚╗║║║║║║║╔╩╝║\n╚══╝╚═╝╚═╝╚══╝"
        )


@borg.on(lightning_cmd(pattern="hhlo ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("hello,how r u")
        await asyncio.sleep(1)
        await event.edit("╔╗╔╗╔╗─╔═╗\n║╚╝║║║─║║║\n║╔╗║║╚╗║║║\n╚╝╚╝╚═╝╚═╝")


@borg.on(lightning_cmd(pattern="sry ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("i'm sorry")
        await asyncio.sleep(1)
        await event.edit("last time forgive me")
        await asyncio.sleep(1)
        await event.edit(
            "╔══╗╔═╗╔═╗╔═╗╔═╦╗\n║══╣║║║║╬║║╬║╚╗║║\n╠══║║║║║╗╣║╗╣╔╩╗║\n╚══╝╚═╝╚╩╝╚╩╝╚══╝"
        )


@borg.on(lightning_cmd(pattern="thnq ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("thanks for your help")
        await asyncio.sleep(1)
        await event.edit(
            "╔══╗╔╗╔╗╔══╗╔═╦╗╔╦╗╔══╗\n╚╗╔╝║╚╝║║╔╗║║║║║║╔╝║══╣\n─║║─║╔╗║║╠╣║║║║║║╚╗╠══║\n─╚╝─╚╝╚╝╚╝╚╝╚╩═╝╚╩╝╚══╝"
        )


@borg.on(lightning_cmd(pattern="ok ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("▒▐█▀▀█▌▒▐█▒▐▀\n▒▐█▄▒█▌▒▐██▌░\n▒▐██▄█▌▒▐█▒▐▄")


@borg.on(lightning_cmd(pattern="smile ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("how sad ")
        await asyncio.sleep(1)
        await event.edit(
            "╔══╗╔═╦═╗╔══╗╔╗─╔═╗\n║══╣║║║║║╚║║╝║║─║╦╝\n╠══║║║║║║╔║║╗║╚╗║╩╗\n╚══╝╚╩═╩╝╚══╝╚═╝╚═╝"
        )


@borg.on(lightning_cmd(pattern="lal ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("╔╗─╔═╗╔╗─\n║╚╗║╬║║╚╗\n╚═╝╚═╝╚═╝")
