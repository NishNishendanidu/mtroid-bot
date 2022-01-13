from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
