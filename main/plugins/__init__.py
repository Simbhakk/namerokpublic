from pyrogram import filters
from pyrogram import Client as stark
from pyrogram.types import Message
from telethon import events

@Invix.on(events.NewMessage(incoming=True, pattern='/donate'))
async def Start_msg(bot: stark , m: Message):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/db68ef17d999fba44333e.jpg",
    caption = "**Hi , Donate some money to keep this service alive**.\n"
                            "**And motivate bot maker to repair bot regularly**..\n\n"
                            "**..**")
