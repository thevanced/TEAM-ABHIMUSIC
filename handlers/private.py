from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CXmQRiwABA4pdYVwoPKfspYF4oV_-AkpNTom_wtAAAogDAAKtNIhWkzwOc8A6MJQhBA")
    await message.reply_text(
        f"""**Hey, I'm Shubhanshu MUSIC🎵

I can play music in your group's voice call. Developed by [Shubhanshu](https://t.me/Shubhanshutya).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/greatpersonxd")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/greatpersonxd"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/greatpersonxd"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/greatpersonxd"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Shubhanshu MUSIC PLAYER IS Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/greatpersonxd")
                ]
            ]
        )
   )


