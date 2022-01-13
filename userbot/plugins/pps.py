# You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""it's to generate the replied user's, channel's or chat's all profile pics that are not deleted
cmd is .PPS ,
ALL credits to the owner of FTG BOT and the dev of this Plugin Emily Bennett."""


import logging
from html import *

from telethon import *
from telethon.tl.functions.account import *
from telethon.tl.functions.channels import *
from telethon.tl.functions.photos import *
from telethon.tl.types import *

from uniborg.util import lightning_cmd

logger = logging.getLogger(__name__)


if 1 == 1:
    name = "Profile Photos"
    client = borg

    @borg.on(lightning_cmd(pattern="PPS(.*)"))
    async def PPScmd(event):
        #        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("<code>ID number you entered is invalid</code>")
                    return
            except:
                await event.edit("<code>ID number you entered is invalid</code>")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await event.edit("<code>No photo found with that id</code>")
                return
