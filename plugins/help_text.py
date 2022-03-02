import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from database.blacklist import check_blacklist
from database.userchats import add_chat

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


REPLY_MARKUP=InlineKeyboardMarkup([
                    [InlineKeyboardButton("𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url="https://t.me/+7ScFy39Vckk5MWQ1"),
                     InlineKeyboardButton("𝙐𝙥𝙙𝙖𝙩𝙚𝙨 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/pyrogrammers")],
                    [InlineKeyboardButton("𝙔𝙤𝙪𝙏𝙪𝙗𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")]
                ])
            )
@Client.on_message(filters.command("help"))
async def help_user(bot, update):
    fuser = update.from_user.id
    if check_blacklist(fuser):
        await update.reply_text("Sorry! You are Banned!")
        return
    add_chat(fuser)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        reply_markup=REPLY_MARKUP,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("start"))
async def start(bot, update):
    fuser = update.from_user.id
    if check_blacklist(fuser):
        await update.reply_text("Sorry! You are Banned!")
        return
    add_chat(fuser)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=REPLY_MARKUP,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
