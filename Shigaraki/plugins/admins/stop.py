from pyrogram import filters
from pyrogram.types import Message

from Shigaraki import app
from Shigaraki.core.call import Shigaraki
from Shigaraki.utils.database import set_loop
from Shigaraki.utils.decorators import AdminRightsCheck
from Shigaraki.utils.inline import close_markup
from config import filter


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~filter
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Shigaraki.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
