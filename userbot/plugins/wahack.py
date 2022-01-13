"""Emoji
Available Commands:
.wahack"""


import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern=r"wahack"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        replied_user.user.first_name
        replied_user.user.username
        useri_d = event.sender_id
        if useri_d == 1311769691:
            await event.edit(
                "This is My Master\nI can't hack my master's Account\n**How dare you trying to hack my master's account nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ @keinshin __to release your account__"
            )
        else:
            await event.edit("Hacking.. Your Whatsapp")
            animation_chars = [
                "Looking for WhatsApp databases in targeted person...",
                " User online: True\nTelegram access: True\nRead Storage: True ",
                "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
                "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
                "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
                "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
                "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",
                "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
                "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
                "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",
                "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",
                "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",
                "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
                "Hacking complete!\nUploading file...",
                "Targeted WhatsApp Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`",
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])
