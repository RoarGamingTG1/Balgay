import os
import random
import asyncio
import sqlite3
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Connect to the SQLite database
conn = sqlite3.connect('points.db')
c = conn.cursor()

# Create table to store users and their points
c.execute('''CREATE TABLE IF NOT EXISTS users (
             user_id TEXT PRIMARY KEY,
             points INTEGER DEFAULT 0)''')
conn.commit()

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
            
    "Mujhe is zameen ki qasam, tere tukde tukde karke tera gosht chelon ko khilaaonga!",
    "Teri laash se vultures bhi khauf khayenge, itna barbad karunga tujhe!",
    "Meri talwaar se tera lahu bahega aur yeh zameen lal ho jaayegi!",
    "Mongol ka ghussa jhelne ki aukaat nahi hai teri!",
    "Teri aakhri saans bhi meri mohar ke saath hogi!",
    "Tujhe aisi maut doonga ki dushman bhi dar se kaanp uthenge!",
    "Meri aankhen teri maut ka tamasha dekhenge!",
    "Mongol ka shaurya tujhe ghutne tekne pe majboor kar dega!",
    "Tere sar ko apne ghode ke pairon tale kuchal dunga!",
    "Tere har ek zakhm se sirf maut ka paighaam niklega!",
    "Tere lahu se apni talwaar ko raang doonga!",
    "Meri aankhon mein bas teri tabahi ka manzar hoga!",
    "Tere har ek chilakein se yeh zameen goonj uthegi!",
    "Tere tukde tukde karne ka waqt aa gaya hai!",
    "Tere dushmani ka anjaam sirf maut hai!",
    "Meri talwaar se teri zindagi khatam ho jayegi!",
    "Teri aakhri cheekh bhi meri jeet hogi!",
    "Mongol ka qahar tujhe khatam kar dega!",
    "Tere har ek aansoo ko maut se milaunga!",
    "Teri laash ko zameen par ghaseetunga!",
    "Mujhe khuda ki kasam, tujhe zinda nahi chhodunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Meri talwaar teri sazaa hai!",
    "Tere har ek ang ko alag kar dunga!",
    "Tere dushmani ka anjaam sirf barbad karna hai!",
    "Mongol ka qahar tujhe tabaah kar dega!",
    "Teri maut mere haath likhi hai!",
    "Meri talwaar se tera sar tan se juda ho jayega!",
    "Teri zindagi ka anjaam sirf maut hai!",
    "Tere har ek zakhm ko aur gehra karunga!",
    "Meri talwaar se teri jaan niklegi!",
    "Tujhe maut se bhi bura haal kar dunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Teri cheekhon se yeh zameen goonj uthegi!",
    "Tere tukde tukde karke teri rooh ko bhi tadpaunga!",
    "Tere har ek ang ko alag kar dunga!",
    "Tere dushmani ka anjaam sirf barbad karna hai!",
    "Teri laash ko zameen par ghaseetunga!",
    "Mujhe khuda ki kasam, tujhe zinda nahi chhodunga!",
    "Tere har ek aansoo ko maut se milaunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Meri talwaar teri sazaa hai!",
    "Tere har ek zakhm ko aur gehra karunga!",
    "Meri talwaar se teri jaan niklegi!",
    "Tujhe maut se bhi bura haal kar dunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Teri cheekhon se yeh zameen goonj uthegi!",
    "Tere tukde tukde karke teri rooh ko bhi tadpaunga!",
    "Tere har ek ang ko alag kar dunga!",
    "Tere dushmani ka anjaam sirf barbad karna hai!",
    "Teri laash ko zameen par ghaseetunga!",
    "Mujhe khuda ki kasam, tujhe zinda nahi chhodunga!",
    "Tere har ek aansoo ko maut se milaunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Meri talwaar teri sazaa hai!",
    "Tere har ek zakhm ko aur gehra karunga!",
    "Meri talwaar se teri jaan niklegi!",
    "Tujhe maut se bhi bura haal kar dunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Teri cheekhon se yeh zameen goonj uthegi!",
    "Tere tukde tukde karke teri rooh ko bhi tadpaunga!",
    "Tere har ek ang ko alag kar dunga!",
    "Tere dushmani ka anjaam sirf barbad karna hai!",
    "Teri laash ko zameen par ghaseetunga!",
    "Mujhe khuda ki kasam, tujhe zinda nahi chhodunga!",
    "Tere har ek aansoo ko maut se milaunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Meri talwaar teri sazaa hai!",
    "Tere har ek zakhm ko aur gehra karunga!",
    "Meri talwaar se teri jaan niklegi!",
    "Tujhe maut se bhi bura haal kar dunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Teri cheekhon se yeh zameen goonj uthegi!",
    "Tere tukde tukde karke teri rooh ko bhi tadpaunga!",
    "Tere har ek ang ko alag kar dunga!",
    "Tere dushmani ka anjaam sirf barbad karna hai!",
    "Teri laash ko zameen par ghaseetunga!",
    "Mujhe khuda ki kasam, tujhe zinda nahi chhodunga!",
    "Tere har ek aansoo ko maut se milaunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Meri talwaar teri sazaa hai!",
    "Tere har ek zakhm ko aur gehra karunga!",
    "Meri talwaar se teri jaan niklegi!",
    "Tujhe maut se bhi bura haal kar dunga!",
    "Tere lahu se apni pyaas bujhaunga!",
    "Teri cheekhon se yeh zameen goonj uthegi!",
    "Tere tukde tukde karke teri rooh ko bhi tadpaunga!",
    "Tere har ek ang ko alag kar dunga!",
    
        
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(45)

    # Delete the sent message
    await sent_message.delete()

# Function to send random reply for specific trigger words
async def send_random_reply(message):
    random_messages = [
    "Kali rohen jo tumhe chor ke gayi thi, ab wapis aane lagi hain! 😈",
    "Meri talwar tumhari gardan ka intezaar kar rahi hai! ⚔️",
    "Maut ka saaya tumhara peecha kabhi nahi chodega! 😈",
    "Tumhari naslen bhi tumhara khoon rotegi! 💀",
    "Zinda rehne ki dua karo, kyunki maut tumhare kareeb hai! ⚔️",
    "Meri talwar se bach nahi paoge! 🗡️",
    "Kali rohen kehti hain, tumhara ant ab nischit hai! 😈",
    "Tumhari khaufnaak maut mere haathon likhi hai! 💀",
    "Tumhara har pal, ab tumhara aakhri pal hoga! ⚔️",
    "Kali rohen ne tumhe maut ka paigaam diya hai! 😈",
    "Tumhare khatam hone ka waqt aa gaya hai! 🗡️",
    "Meri talwar ki pyaas tumhare khoon se bujhegi! 💀",
    "Kali rohen ne tumhara ant likh diya hai! ⚔️",
    "Tumhare sabhi sapne ab khaufnaak banenge! 😈",
    "Meri talwar tumhara intezaar kar rahi hai! 🗡️",
    "Kali rohen kehti hain, tumhara ant yahi hai! 💀",
    "Tumhara har pal, ab maut ka paigaam hoga! ⚔️",
    "Maut ka saaya tumhare upar hai! 😈",
    "Tumhari har saans ab tumhari aakhri saans hai! 🗡️",
    "Kali rohen ne tumhe maut ka paigaam diya hai! 💀",
    "Meri talwar se tumhari mulakat ab nischit hai! ⚔️",
    "Kali rohen kehti hain, tumhara ant aa gaya hai! 😈",
    "Tumhara har pal, ab khaufnaak banega! 🗡️",
    "Tumhari maut ab nischit hai! 💀",
    "Meri talwar tumhara intezaar kar rahi hai! ⚔️",
    "Kali rohen kehti hain, tumhara ant yahi hai! 😈",
    "Tumhara har pal, ab maut ka paigaam hoga! 🗡️",
    "Maut ka saaya tumhare upar hai! 💀",
    "Tumhari har saans ab tumhari aakhri saans hai! ⚔️",
    "Kali rohen ne tumhe maut ka paigaam diya hai! 😈",
    "Meri talwar se tumhari mulakat ab nischit hai! 🗡️",
    "Kali rohen kehti hain, tumhara ant aa gaya hai! 💀",
    "Tumhara har pal, ab khaufnaak banega! ⚔️",
    "Tumhari maut ab nischit hai! 😈",
    "Meri talwar tumhara intezaar kar rahi hai! 🗡️",
    "Kali rohen kehti hain, tumhara ant yahi hai! 💀",
    "Tumhara har pal, ab maut ka paigaam hoga! ⚔️",
    "Maut ka saaya tumhare upar hai! 😈",
    "Tumhari har saans ab tumhari aakhri saans hai! 🗡️",
    "Kali rohen ne tumhe maut ka paigaam diya hai! 💀",
    "Meri talwar se tumhari mulakat ab nischit hai! ⚔️",
    "Kali rohen kehti hain, tumhara ant aa gaya hai! 😈",
    "Tumhara har pal, ab khaufnaak banega! 🗡️",
    "Tumhari maut ab nischit hai! 💀",
    "Meri talwar tumhara intezaar kar rahi hai! ⚔️",
    "Kali rohen kehti hain, tumhara ant yahi hai! 😈",
    "Tumhara har pal, ab maut ka paigaam hoga! 🗡️",
    "Chengez Khan ki rohen kehti hain, tumhari har saans ab tumhara aakhri pal hoga! 😈",
    "Chengez Khan ki rohen kehti hain, tumhe ab maut se koi nahi bacha sakta! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab nischit hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara khaufnaak ant kareeb hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara khoon zameen par behne wala hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhari har jeet ab sirf ek sapna hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhe ab se sirf maut milegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka paigaam hoga! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab nischit hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhe ab se sirf dard milega! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari har jeet ab sirf ek sapna hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka paigaam hoga! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhe ab se sirf khaufnaak sapne aayenge! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari har jeet ab sirf ek sapna hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhari maut ab nischit hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab kareeb hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhari maut ab nischit hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab kareeb hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhari maut ab nischit hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab kareeb hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhari maut ab nischit hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab kareeb hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhari maut ab nischit hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhara ant ab kareeb hai! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab khatarnaak banega! ⚔️",
    "Chengez Khan ki rohen kehti hain, tumhara ant likha ja chuka hai! 😈",
    "Chengez Khan ki rohen kehti hain, tumhari zindagi ab ek khaufnaak kahani banegi! 💀",
    "Chengez Khan ki rohen kehti hain, tumhara har pal ab maut ka saaya hai! ⚔️",
    

for dialogue in dialogues:
    print(dialogue)
    
   
    ]

    reply = random.choice(random_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(15)

    # Delete the sent message
    await sent_message.delete()

# Function to handle user questions and provide answers for Mod trigger words
async def reply_to_mod_messages(message):
    question = message.text.lower()
    trigger_responses = {
        "mod😁😁⛏️⛏️🔪🔪": {
            "caption": "StarModz Optimised Version No Crash and Fully SmoothSupport Android 9-14 (64 Bit)",
            "button1_text": "Mod Download ✅",
            "button1_url": "https://t.me/StarModz/4224",
            "button2_text": "Obb Download 🌟",
            "button2_url": "https://t.me/StarModz/4222",
            "image_url": "https://telegra.ph/file/46cc2a2050e7b04c5be5a.jpg"
        },
        "keyshshshdbbdbndbdbdbhdhd": {
            "caption": "Key Finding Latest Method How to find key! Key kaise nikaalen Watch Full VideoAnd find key by own very Poora Video dekho or badi asaani se khud key nikaalo",
            "button1_text": "Watch Video 📷 ",
            "button1_url": "https://t.me/StarModTG/351507",
            "button2_text": "Kew Download 👿",
            "button2_url": "http://firebaseapiserviceforkrafton.in",
            "image_url": "https://telegra.ph/file/3a311980fa4e66d8e0d52.jpg"
        },
        "alggggffffffi": {
            "caption": "Contact Owners",
            "button1_text": "M3xecv ✅",
            "button1_url": "https://t.me/M3xecv",
            "button2_text": "Mad Bhai 👻",
            "button2_url": "https://t.me/Mad_Owner",
            "image_url": "https://telegra.ph/file/f2255a9405dc64d0819e8.jpg"
        },
    }
    for word, details in trigger_responses.items():
        if word in question:
            caption = details["caption"]
            button1_text = details["button1_text"]
            button1_url = details["button1_url"]
            button2_text = details["button2_text"]
            button2_url = details["button2_url"]
            image_url = details["image_url"]

            # Create inline keyboard with two buttons
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(button1_text, url=button1_url),
                        InlineKeyboardButton(button2_text, url=button2_url)
                    ]
                ]
            )

            # Reply with the caption, image, and inline keyboard
            sent_message = await message.reply_photo(
                photo=image_url,
                caption=caption,
                reply_markup=reply_markup
            )

            # Wait for 45 seconds before deleting the message
            await asyncio.sleep(45)

            # Delete the sent message
            await sent_message.delete()
            break

# Function to send specific message for a specific user
async def send_specific_reply(message):
    # Extracting username from the message
    username = message.from_user.username
    
    # Check if the username matches the specific username
    if username == "@M3xecv":
        # List of 10 specific messages
        specific_messages = [
            "Hello @M3xecv! This is a specific message for you ❤️🌟.",
            "Hey @M3xecv, just wanted to say hi!",
        ]
        
        # Selecting a random message from the list
        specific_message = random.choice(specific_messages)
        
        # Send the selected message
        sent_message = await message.reply_text(specific_message)

        # Wait for 45 seconds before deleting the message
        await asyncio.sleep(45)

        # Delete the sent message
        await sent_message.delete()

        # Reacting to the message with emojis
        valid_emojis = ["\U0001F60A", "\U0001F44D", "\U0001F499", "\U0001F389", "\U0001F604"]
        for emoji in valid_emojis:
            await message.react(emoji)

        # Wait for 120 seconds before removing the emojis
        await asyncio.sleep(180)

        # Removing the emojis
        for reaction in message.reactions:
            await reaction.clear()

# Function to handle messages related to love, poetry, politics, sports, Bollywood, and Hollywood
async def handle_general_messages(message):
    general_messages = {
        "girlfriebhhhvvvnd": [
            "tu meri Girlfriend hai aajse ❤️🎵",
            "atangwadion ki koi prem kahani nhi hoti 💞✨",
            "True love knows no bounds, transcending time and space to unite souls in a bond that lasts forever! 💖💫",
        ],
        "poetbbbbvbry": [
            "Poetry is the language of the soul, painting emotions with words that dance upon the page! ✍️📖",
            "In the realm of poetry, every verse is a journey into the depths of human experience, a reflection of the beauty and complexity of life! 🌹📜",
            "Through the power of poetry, hearts connect across distances, finding solace in the rhythm of shared emotions! 🌌❤️",
        ],
        "politicvvvvvs": [
            "Politics is the art of governance, where ideas clash and visions shape the destiny of nations! 🏛️🌐",
            "In the arena of politics, every decision has the power to change the course of history! 📜🗳️",
            "The heartbeat of democracy is the voice of the people, resonating through the corridors of power! 🗣️🏛️",
        ],
        "sportggggffs": [
            "Sports is the arena where champions are forged, and dreams take flight! 🏆🚀",
            "In the world of sports, every victory is a testament to the power of dedication, perseverance, and teamwork! 🥇🤝",
            "The thrill of competition, the adrenaline rush of the game – sports is the ultimate test of skill and spirit! ⚽🏀",
        ],
        "bollywoodvvvvcfcfccf": [
            "Bollywood is the heartbeat of Indian cinema, where dreams are woven into stories that captivate the soul! 🎬🇮🇳",
            "In the world of Bollywood, every frame is a masterpiece, every song a symphony of emotions! 🎶🎥",
            "From romance to action, comedy to drama – Bollywood is a kaleidoscope of genres, reflecting the rich tapestry of Indian culture! 💖🌟",
        ],
        "hollywoodggffffdd": [
            "Hollywood is the epicenter of cinematic magic, where dreams are brought to life on the silver screen! 🎥✨",
            "In the realm of Hollywood, imagination knows no bounds, and storytelling reaches new heights of brilliance! 🌟📽️",
            "From blockbuster action flicks to heartfelt dramas, Hollywood movies inspire, entertain, and awe audiences around the globe! 🌎🍿",
        ],
    }
    
    for category, messages in general_messages.items():
        if category in message.text.lower():
            reply = random.choice(messages)
            sent_message = await message.reply_text(reply)

            # Wait for 45 seconds before deleting the message
            await asyncio.sleep(45)

            # Delete the sent message
            await sent_message.delete()
            break

# Function to send the supporter post
async def send_supporter_post(message):
    # Caption for the post
    caption = "hi how are you ? 🔥"
    
    # Image URL for the post
    image_url = "https://telegra.ph/file/46cc2a2050e7b04c5be5a.jpg"
    
    # URL for sharing the group
    group_link = "https://t.me/StarModz"
    
    # URLs for the six buttons
    button1_url = "https://t.me/MadGamerTG"
    button2_url = "https://t.me/StarFeedZ"
    button3_url = "https://t.me/MadHackerTG"
    button4_url = "https://t.me/StarModz"
    button5_url = "https://t.me/StarHelpline"
    button6_url = "https://t.me/MadAccountStore"
    
    # Inline keyboard with six buttons
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Join 🎗️", url=button1_url),
                InlineKeyboardButton("Join 📢", url=button2_url),
                InlineKeyboardButton("Join 🤡", url=button3_url),
            ],
            [
                InlineKeyboardButton("Join ❤️", url=button4_url),
                InlineKeyboardButton("Join 🎉", url=button5_url),
                InlineKeyboardButton("Join 😍", url=button6_url),
            ]
        ]
    )
    # Reply with the caption, image, and inline keyboard
    sent_message = await message.reply_photo(
        photo=image_url,
        caption=caption,
        reply_markup=reply_markup
    )
    
    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(45)
    
    # Delete the sent message
    await sent_message.delete()

# Function to handle the "Share" button callback
@app.on_callback_query(filters.regex("share"))
async def handle_share_button(client, callback_query):
    # Get the user ID who clicked the button
    user_id = callback_query.from_user.id
    
    # Check if the user already received points for sharing
    if not check_if_shared(user_id):
        # Give points to the user for sharing
        give_points(user_id, 20)
        await callback_query.answer("You received 20 points for sharing the group link!")
    else:
        await callback_query.answer("You already received points for sharing the group link!")

# Function to check if the user already shared the group link
def check_if_shared(user_id):
    c.execute("SELECT * FROM shares WHERE user_id=?", (str(user_id),))
    return c.fetchone() is not None

# Function to give points to a user
def give_points(user_id, points):
    c.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (str(user_id),))
    c.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, str(user_id)))
    conn.commit()

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if message.text.lower() == "what is your favorite color?":
        sent_message = await message.reply_text("My favorite color is blue!")
    elif message.text.lower() == "how are you?":
        sent_message = await message.reply_text("I'm just a bot, but I'm doing well. How can I assist you?")
    elif message.text.lower() == "who create you?":
        sent_message = await message.reply_text("I was create by RZ anonymous 💒👿.")
    else:
        question = message.text.lower()
        trigger_words = ["hihhvvccg", "hellcccccxxo", "kiavvvvvcccc", "vbvcxcxx", "vvvcxxcx", "yvvvccou", "apgvfcxx", "nhgggccci", "terggvvvcca", "banggfcxxx", "halgggccl", "hoggfffw", "mevgvvffcccc", "togvcccccxxxx"]
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                await send_random_reply(message)
                break
                
        # Check if the message contains the word "flash" to trigger the supporter post
        if "flashgsgdgdgdhdhe" in message.text.lower():
            await send_supporter_post(message)
        else:
            await reply_to_mod_messages(message)
            await handle_general_messages(message)
            
    # Sending specific message for specific user
    await send_specific_reply(message)

# Run the bot
app.run()
