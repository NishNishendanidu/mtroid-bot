# made by @LEGENDX22
# kang with credits else gey

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP

from userbot.utils import lightning_cmd


bot = "@MadBoy_Rotomgram2_Bot"


@borg.on(lightning_cmd("weak ?(.*)"))
async def _(event):
  if event.fwd_from:
      return
  sysarg = event.pattern_match.group(1)
  if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await conv.get_response()
              await conv.send_message("/type")
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("Error: unblock @inhumanDexBot and retry!")
  elif "@" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await conv.get_response()
              await conv.send_message("/type " + sysarg)
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("Error: unblock @MadBoy_Rotomgram2_Bot and try again!")
  elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await conv.get_response()
              await conv.send_message("/type " + sysarg)
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("Error: unblock @MadBoy_Rotomgram2_Bot `and try again!")

CMD_HELP.update({
   "weak":"this plugin is info of pokemon weakness type .weak fire or .weak any types"})
