from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CXmQRiwABA4pdYVwoPKfspYF4oV_-AkpNTom_wtAAAogDAAKtNIhWkzwOc8A6MJQhBA")
    await message.reply_text(
        f"""**Hey, I'm Shubhanshu MUSICπ΅

I can play music in your group's voice call. Developed by [Shubhanshu](https://t.me/Shubhanshutya).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  Source Code π ", url="https://t.me/greatpersonxd")
                  ],[
                    InlineKeyboardButton(
                        "π¬ Group", url="https://t.me/greatpersonxd"
                    ),
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/greatpersonxd"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "β Add To Your Group β", url="https://t.me/greatpersonxd"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Shubhanshu MUSIC PLAYER IS Online β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/greatpersonxd")
                ]
            ]
        )
   )


