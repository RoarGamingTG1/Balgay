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
        "Mining Shru Kren Aaj Se Hi",
           "Mining Shuru Kren Aaj Se Hi! ⛏️😄",
        "Mining mein zindagi banaayein! 💎🚀",
        "Gold digging ki tarah, bas ghar baithe! 🏡💰",
        "Mining karein, sapne sajayein! 🌟⛏️",
        "Bitcoin mine kar ke millionnaire banein! 🤑💸",
        "Chalo mining karne ka maza lo! 🎉⛏️",
        "Khudai karen, paisa banayein! 💵🔍",
        "Zameen ke neche chhupe khazaane dhoondein! 🗺️⛏️",
        "Digital sona dhoondhna shuru karein! 📲💎",
        "Aaj se mining, kal se Lamborghini! 🏎️💨",
        "Khazaana aapke computer mein chhupa hai! 💻💰",
        "Mining se ghar ka rent bharna ab aasaan! 🏠💸",
        "Mining karein, vacation pe jayein! 🌴⛏️",
        "Har clik pe sona! 🖱️💎",
        "Mining karein, stress door karein! 😌⛏️",
        "Crypto mine karein, future secure karein! 🚀🔒",
        "Paisa banane ka naya tareeqa! 💵⛏️",
        "Khudai karein, khushiyan le aayein! 🎉⛏️",
        "Bina mitti ke sona milega! 🏜️💎",
        "Har mining session mein naya adventure! 🗺️⛏️",
        "Mining karein aur naya phone khareedein! 📱💸",
        "Jitna chaho, utna kamao! 💰💯",
        "Kismat chamkao mining se! 🌟⛏️",
        "Mining karna, paisa kamaana! 💵⛏️",
        "Har coin mein nayi kahani! 📖💰",
        "Sona nikalo, bank balance badhao! 📈💎",
        "Mining karein aur dosto ko impress karein! 😎⛏️",
        "Mining karein, weekend enjoy karein! 🍹💰",
        "Crypto mining, aapka naya hobby! 🏆⛏️",
        "Khudai karo aur ghar ko sona banayein! 🏡💎",
        "Mining se jeetne ka naya tareeqa! 🥇⛏️",
        "Mining se ghar baithe kamaayein! 🛋️💸",
        "Crypto mining, future earning! 📉⛏️",
        "Bitcoin mining, future shining! ✨💎",
        "Mining karein, shandar zindagi jeeyein! 🎉💰",
        "Digital khazaane aapke intezaar mein! ⛏️💻",
        "Crypto mine karo aur shaandar bank balance paao! 💸💻",
        "Mining karein, life set karein! 📈💎",
        "Mining se har din naya! 🌞⛏️",
        "Khudai karein aur sapne sach karein! 🌟⛏️",
        "Mining karein aur apne fortune ko khud likhein! 🖋️💰",
        "Crypto mining, naya excitement! 🎢💎",
        "Mining karein aur doston ko sath le aayein! 👯‍♂️⛏️",
        "Mining se ghar ka kharcha! 🏠💵",
        "Mining kar ke apne sapne pure karein! 🌠⛏️",
        "Mining se fortune banayein! 🤑💎",
        "Crypto mining, nayi duniya! 🌐💰",
        "Zameen ke neche khazana hai! ⛏️💎",
        "Mining karein aur millionaire banein! 💰✨",
        "Mining se dosti badhao! 🤝⛏️",
        "Crypto mining se apna waqt sahi invest karo! ⏳💰",
        "Mining se naye projects start karo! 🚀⛏️",
        "Khudai se apna luck badhao! 🍀💎",
        "Mining karein aur lavish life jeeyein! 💎🏝️",
        "Crypto mining se car khareedein! 🚗💰",
        "Mining se dosti mazboot! 🤝⛏️",
        "Mining karein aur apna dream home banayein! 🏡💸",
        "Crypto mining karein aur duniya ghoomein! ✈️💰",
        "Mining karein aur apni duniya banaayein! 🌍⛏️",
        "Crypto mining, naye opportunities! 🚀💎",
        "Mining karein aur daily income paayein! 💵⛏️",
        "Mining se financial freedom! 🚀💰",
        "Crypto mining karein aur apna luck chamkaayein! 🌟💎",
        "Mining karein aur wealth badhayein! 💰📈",
        "Khudai karein aur apne sapne jeeyein! 🌠⛏️",
        "Mining karein aur financial stability paayein! 💰🔒",
        "Crypto mining, naye ideas! 💡💎",
        "Mining karein aur professional miner banein! ⛏️🏆",
        "Mining se ghar baithe kamaayein! 🏡💸",
        "Crypto mining se apna business start karein! 🚀💰",
        "Mining karein aur shaandar future banayein! 🌠💎",
        "Crypto mining karein aur life enjoy karein! 🍹💰",
        "Khudai karein aur apna luck banayein! 🍀⛏️",
        "Crypto mining se ghar baithe income! 🏠💸",
        "Mining karein aur apna fortune chamkaayein! 🌟💰",
        "Crypto mining, naye connections! 🌐💎",
        "Mining karein aur zindagi enjoy karein! 😄💰",
        "Mining karein aur aaj hi paisa kamaayein! 💵⛏️",
        "Crypto mining karein aur financial goals achieve karein! 🏆💎",
        "Mining se apne dosto ko inspire karein! 👯‍♂️💰",
        "Mining karein aur financial success paayein! 📈💎",
        "Khudai karein aur apne sapne jeeyein! 🌟⛏️",
        "Crypto mining se future secure karein! 🔒💰",
        "Mining karein aur apna luck chamkaayein! 🌠💎",
        "Crypto mining karein aur duniya ghoomein! ✈️💰",
        "Mining karein aur apne goals achieve karein! 🎯💎",
        "Crypto mining se financial independence! 🚀💰",
        "Mining karein aur lavish life jeeyein! 💎🏝️",
        "Crypto mining, naye opportunities! 🌟💎",
        "Mining karein aur daily income paayein! 💵⛏️",
        "Mining se apni duniya banayein! 🌍💰",
        "Crypto mining karein aur life enjoy karein! 🍹💎",
        "Khudai karein aur apna luck chamkaayein! 🍀⛏️",
        "Crypto mining se future banayein! 🔮💰",
        "Mining karein aur apne sapne sach karein! 🌠💎",
        "Crypto mining se zindagi enjoy karein! 😄💰",
        "Mining karein aur shaandar life paayein! 🎉💎",
        "Crypto mining karein aur apna future secure karein! 🔒💰",
        "Mining karein aur apna fortune chamkaayein! 🌟💎",
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
            "text": "MiningBot 1: Earn through Hamster Kombat Play",
            "url": "https://t.me/Hamster_kombat_bot/start?startapp=kentId6298865570",
            "image": "https://telegra.ph/file/1def17f220265924b3dc4.jpg"
        },
        {
            "text": "MiningBot 2: WCoin Play - Real Mining Earnings",
            "url": "https://t.me/wcoin_tapbot?start=NjI5ODg2NTU3MA==",
            "image": "https://telegra.ph/file/a8812258116b187b94eda.jpg"
        },
        {
            "text": "MiningBot 3: Earn with MemeFi Play",
            "url": "https://t.me/memefi_coin_bot?start=r_d9aa24376d",
            "image": "https://telegra.ph/file/d559e5d7915081ea2eb1c.jpg"
        },
        {
            "text": "MiningBot 4: YescCoin Play for Mining",
            "url": "https://t.me/yescoingame_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/4cab774299246ae48c43e.jpg"
        },
        {
            "text": "MiningBot 5: Play with Gamee for Real Earnings",
            "url": "https://t.me/gamee?start=ref_6298865570",
            "image": "https://telegra.ph/file/ca27a1c86360ab20b602a.jpg"
        },
        {
            "text": "MiningBot 6: Tapswap Play - Start Mining",
            "url": "https://t.me/tapswap_mirror_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/42c68116b51cd875b93a8.jpg"
        },
        {
            "text": "MiningBot 7: Earn with DotCoin Play",
            "url": "https://t.me/dotcoin_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/ed844f9c4243cf73b3940.jpg"
        }
                {
            "text": "MiningBot 8: Earn With OnChain Play",
            "url": "https://t.me/onchaincoin_bot?start=user_6298865570",
            "image": "https://telegra.ph/file/c1f935787e2955e53cb5d.jpg"
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
        "Friends! "
        "Yahan aapko mining se related sab kuch milega. Neeche diye gaye links ko follow karke mining start karein aur earning shuru kren in Apne mining krni hai or apny coins badhany hen jb inki listing Hogi to apko acha Profit Milega 😊 kuch bandy Bolty samjh nhi aati 🙆 mining Ki jab tak koi kaam start nhi kroge tab tak samjh nhi ayegi To apna time mat Barbad kren Kren Aaj se Hi start kren 🥰🥰"
    )
    sent_message = await message.reply_text(intro_message)

    # Wait for 10 seconds before deleting the intro message
    await asyncio.sleep(15)

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
            "hi", "hello", "bot", "how", "😒",
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
        
