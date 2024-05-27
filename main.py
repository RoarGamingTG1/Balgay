import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
        "Chengez Khan ki rohen kehti hain, tumhari har jeet ab sirf ek sapna hai! 💀",
        "Chengez Khan ki rohen kehti hain, tumhara ant ab nischit hai! 😈",
        "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
        "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
        "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
        "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka paigaam hoga! 💀",
        "Chengez Khan ki rohen kehti hain, tumhe ab se sirf dard milega! 😈"
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(45)

    # Delete the sent message
    await sent_message.delete()

# Function to send intro message
async def send_intro_message(message):
    intro_message = (
        "Khushamdeed! Aap Chengez Khan ke rohen ki duniya mein hain! 😈\n"
        "Yahan par aapko khatarnaak dhamkian milengi aur maut ka har pal mehsoos hoga. ⚔️"
    )
    sent_message = await message.reply_text(intro_message)

    # Wait for 60 seconds before deleting the message
    await asyncio.sleep(60)

    # Delete the sent message
    await sent_message.delete()

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if "start" in message.text.lower():
        await send_intro_message(message)
    else:
        trigger_words = [
            "hi", "hello", "kia", "how", "price",
            "inbox", "dm", "ban", "😁", "banggfcxxx",
            "halgggccl", "hoggfffw", "mevgvvffcccc", "togvcccccxxxx"
        ]
        question = message.text.lower()
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                break

# Run the bot
app.run()
