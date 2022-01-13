# Rewritten by @keinshin
import io
from  userbot import CMD_LIST, ALIVE_NAME, bot as light
from userbot import CMD_HELP
from userbot.utils import lightning_cmd
import asyncio
from var import Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Your Desired Name` "
    
            



@light.on(lightning_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if lightningusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "`Lol Try .help`")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "\n    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit("`Wait Checking..`")
                await asyncio.sleep(2)
                await event.edit(input_str + "  ☹️ is not a valid plugin😞😞!")
        else:
            light_help_strin = """**Black Lightning Heres With The Detailed Help For CMDs** 😉😉 !\n If Faced Any Bug Please Give The Feed Back at [Lightning Support](https://t.me/lightning_support_group):"""
            results = await bot.inline_query(  # pylint:disable=E0602
            lightningusername, light_help_strin
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
