#Github.com/im-Rudraa332

import os
from .. import Bot
from telethon import events, Button
from pyrogram import filters,Client
#async def start_srb(event, st):
from .. import AUTH
#S = '/' + 's' + 't' + 'a' + 'r' + 't'
# ----------------> Something try new

from pyrogram import filters

Rudraa="""Hi, sir batch or bulk is not free. you can see this smalll plan\nhttps://t.me/Bypass_Restricted/19"""

@Bot.on_message((filters.command("bulk") & filters.private & ~filters.user(AUTH)) | filters.command("batch") & ~filters.user(AUTH))

async def start(bot, cmd):

    await cmd.reply_text(

        Rudraa.format(cmd.from_user.first_name, cmd.from_user.id)

    )

    return
#------------------------------------------------------>
from pyrogram import Client
from pyrogram.types import Message

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
# ------------------------------------> Added log channel
from .configs import Config
from .database import Database
import datetime

BOT_USERNAME = Config.BOT_USERNAME
BOT_TOKEN = Config.BOT_TOKEN
API_ID = Config.API_ID
API_HASH = Config.API_HASH
LOG_CHANNEL = Config.LOG_CHANNEL
#AUTH = Config.AUTH
db= Database(Config.DATABASE_URL, BOT_USERNAME)

async def foo(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            Config.LOG_CHANNEL,
            f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) And His/her username is \n **@{cmd.from_user.username}**\n And Userid is `{cmd.from_user.id}` !!"
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("You are Banned.", quote=True)
            return
    await cmd.continue_propagation()


@Bot.on_message(filters.private)
async def _(bot, cmd):
    await foo(bot, cmd)

# ----------------------------------------------------------->brodcast message Added

broadcast_ids = {}
import random
import time
import aiofiles
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import asyncio
import traceback
import string
async def send_msg(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"

@Bot.on_message(filters.private & filters.command("broadcastpelo") & filters.reply)
async def broadcast_(c, m):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"Broadcast Started! You will be notified with log file when all the users are notified."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    os.remove('broadcast.txt')

 

# ------------------------------------------------------->

from .. import bot
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@bot.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Hi👋 I am Save Restricted Content Bot\n\n**Send me any video or message link Only \nfrom PUBLIC RESTRICTED CHANNELS** to clone it here.\n\nMust join:- @Bypass_Restricted"
    #await start_srb(event, text)
    await event.reply(text, 

                      buttons=[

                              [Button.url("REPO LINK", url="https://t.me/Bypass_Restricted/68"),
                               Button.url("PREMIUM", url="https://t.me/Bypass_Restricted/66")],        
                              [Button.url("JOIN CHANNEL TO USE ME", url="t.me/Raj02_bots")]])                             

@bot.on(events.NewMessage(incoming=True, pattern='/qr_code'))                       
async def donate(event):
    photo = "https://telegra.ph/file/db68ef17d999fba44333e.jpg"
    await event.(photo)

@bot.on(events.NewMessage(incoming=True, pattern='/donate'))                       
async def donate(event):
    text = "Please donate to keep this service alive. you can send any amount\n10₹, 20₹, 50₹, 100₹\n\n🔘 Payment Methods : 'aman-9298@paytm' \n For QR CODE PRESS /qr_code " 
    await event.(text)
    
    '''

    await event.reply(text, 

                      buttons=[

                              [Button.inline("SET THUMB.", data="set"),

                               Button.inline("REM THUMB.", data="rem")],

                              [Button.url("Join to use me", url="t.me/Raj02_bots")]])

    '''

    

