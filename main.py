import os
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("Number_Collection_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Dictionary to store user numbers
user_numbers = {}

# Function to handle the /start command and ask for contact sharing
@app.on_message(filters.command("start"))
async def start(client, message):
    contact_button = KeyboardButton("Share Contact", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], one_time_keyboard=True)
    await message.reply_text("Please share your contact number.", reply_markup=reply_markup)

# Function to handle contact messages
@app.on_message(filters.contact)
async def contact_handler(client, message):
    contact = message.contact
    if contact:
        user_numbers[message.from_user.id] = contact.phone_number
        await message.reply_text(f"Thanks for sharing your number: {contact.phone_number}")

# Function to handle /FFD command and show the stored number
@app.on_message(filters.command("FFD"))
async def show_number(client, message):
    user_id = message.from_user.id
    if user_id in user_numbers:
        await message.reply_text(f"Your stored number is: {user_numbers[user_id]}")
    else:
        await message.reply_text("No number found. Please share your contact first.")

# Run the bot
app.run()
