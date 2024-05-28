import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        "Mining Shru Kren Aaj Se Hi",
     
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(45)

    # Delete the sent message
    await sent_message.delete()

# Function to send a series of 8 messages
async def send_series_of_messages(message):
    messages = [
        {
            "text": "Message 1: ʜᴀᴍsᴛᴇʀ ᴋᴏᴍʙᴀᴛ ᴘʟᴀʏ",
            "url": "https://t.me/Hamster_kombat_bot/start?startapp=kentId6298865570",
            "image": "https://telegra.ph/file/1def17f220265924b3dc4.jpg"
        },
        {
            "text": "Message 2: ᴡᴄᴏɪɴ ᴘʟᴀʏ",
            "url": "https://t.me/wcoin_tapbot?start=NjI5ODg2NTU3MA==",
            "image": "https://t.me/wcoin_tapbot?start=NjI5ODg2NTU3MA=="
        },
        {
            "text": "Message 3: ᴍᴇᴍᴇ ғɪ ᴘʟᴀʏ",
            "url": "https://t.me/memefi_coin_bot?start=r_d9aa24376d",
            "image": "https://telegra.ph/file/d559e5d7915081ea2eb1c.jpg"
        },
        {
            "text": "Message 4: ʏᴇsᴄᴏɪɴ ᴘʟᴀʏ ",
            "url": "https://t.me/yescoingame_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/image4.jpg"
        },
        {
            "text": "Message 5: ɢᴀᴍᴇᴇ ᴘʟᴀʏ",
            "url": "https://t.me/gamee?start=ref_6298865570",
            "image": "https://telegra.ph/file/ca27a1c86360ab20b602a.jpg"
        },
        {
            "text": "Message 6: Tapswab Play",
            "url": "https://t.me/tapswap_mirror_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/42c68116b51cd875b93a8.jpg"
        },
        {
            "text": "Message 7: ᴅᴏᴛ ᴄᴏɪɴ ᴘʟᴀʏ",
            "url": "https://t.me/dotcoin_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/ed844f9c4243cf73b3940.jpg"
        },
        {
            "text": "Message 8: ᴊᴏɪɴ ɢʀᴏᴜᴘ ғᴏʀ ᴜᴘᴅᴀᴛᴇs",
            "url": "https://t.me/zarwish1",
            "image": "https://telegra.ph/file/adb8795cd553aaace3c9d.jpg"
        }
    ]

    for msg in messages:
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Open Link", url=msg["url"])]]
        )
        sent_message = await message.reply_photo(
            photo=msg["image"],
            caption=msg["text"],
            reply_markup=reply_markup
        )

        # Wait for a short period before sending the next message
        await asyncio.sleep(5)

# Function to send intro message and then a series of messages
async def send_intro_message(message):
    intro_message = (
        "In Sab Projects P work kren all Real Mining Platforms Hen Join @zarwish1 🙆"
    )
    sent_message = await message.reply_text(intro_message)

    # Wait for 10 seconds before deleting the intro message
    await asyncio.sleep(10)

    # Delete the sent message
    await sent_message.delete()

    # Send the series of messages
    await send_series_of_messages(message)

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
    
