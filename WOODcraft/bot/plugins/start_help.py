# WOODcraft goel
from WOODcraft.bot import AngelBot
from WOODcraft.vars import Var
import logging
logger = logging.getLogger(__name__)
from WOODcraft.bot.plugins.stream import MY_PASS
from WOODcraft.utils.human_readable import humanbytes
from WOODcraft.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from WOODcraft.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup


@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'سلام {m.from_user.mention(style="md")}, برای دریافت لینک دانلود مستقیم فایل مورد نظر خود را ارسال کنید.'
    )