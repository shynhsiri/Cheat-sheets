from dotenv import load_dotenv
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
bot =Client(
    "SHYNHSIRI",#name
    api_id= os.getenv("API_KEY"), #api id
    api_hash= os.getenv("API_HASH"),  #api hash
    bot_token= os.getenv("BOT_TOKEN") #bot token
)

# 1-send_message()

@bot.on_message(filters.command('start') & filters.private) #creating command
def start(bot, message): #function
    bot.send_message(message.chat.id, "Hello World")#method

#---------------------------------------------------------------------------

#  2/1-reply_text()

@bot.on_message(filters.command('reply'))
def reply(bot, message):
    message.reply_text("reply to message",  quote=True)
   
# 2/2-echo

# @bot.on_message(filters.text & filters.private)
# def echo(client, message):
#     message.reply_text(message.text)

#---------------------------------------------------------------------------

#  3-welcome

GROUP = "#" #Group id/username and also can be a list
WELCOME_MESSAGE = "Welcome!" #message

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members) #filter new members
def welcome(client, message):
    message.reply_text(WELCOME_MESSAGE)#pay attention in groups quote default is True

#---------------------------------------------------------------------------

# 4-media
# be  sure to disable echo

# send_photo

@bot.on_message(filters.command('photo'))
def photo(bot, message):
    bot.send_photo(message.chat.id, "https://unsplash.com/photos/black-android-smartphone-vXInUOv1n84") #path
    bot.send_photo(message.chat.id, "#") #second photo path

# get  media(audio/document/video/sticker/animation/voice)

@bot.on_message(filters.audio & filters.private)
def audioget(bot, message):
    message.reply(message.audio.file_id)  #get file ids
# replace audio with data types in parentheses

# send  media(audio/document/video/sticker/animation/voice)

@bot.on_message(filters.command('audio'))
def audiosend(bot, message):
    bot.send_audio(message.chat.id, "#")  #insert the id that given by bot
# replace audio with data types in parentheses

#---------------------------------------------------------------------------

# 5-delete_message

# @bot.on_message(filters.text)
# def delete_text(bot, message):
#     word_list =  ["fuck", "wtf"]
#     if any(word in message.text.lower() for word in word_list):
#         bot.delete_messages(message.chat.id, [message.id])
#         bot.send_message(message.chat.id, "Blocklist word detected!")

#---------------------------------------------------------------------------

# 6/1-Inline_Keyboard
# make sure delete_massage section is commented

# inline keyboard is a keyboard that appears right below the message
# it can be used to provide users with a set of options to interact with your bot
# inline keyboard can be used to send callback data to the bot
# callback data can be used to identify the button that was pressed


# Define the /inline command handler
@bot.on_message(filters.command("inline"))
async def inline(client, message):
    # Create an inline keyboard with 4 buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Button 1", callback_data="btn1")],
        [InlineKeyboardButton("Button 2", callback_data="btn2")],
        [InlineKeyboardButton("Button 3", callback_data="btn3")],
        [InlineKeyboardButton("Button 4", url="https://shynhsiri.github.io/")]
    ])
    # Send a message with the inline keyboard
    await message.reply("Choose an option:", reply_markup=keyboard)

# Define the callback query handler
@bot.on_callback_query()
async def callback_query(client, callback_query):
    data = callback_query.data
    if data == "btn1":
        await callback_query.answer("You clicked Button 1")
    elif data == "btn2":
        await callback_query.answer("You clicked Button 2")
    elif data == "btn3":
        await callback_query.answer("You clicked Button 3")
    elif data == "btn4":
        await callback_query.answer("You clicked Button 4")
    else:
        await callback_query.answer("Unknown button")

# 6/2-Reply_Keyboard
# reply keyboard is a keyboard that appears at the bottom of the chat

# Define the /repc command handler
@bot.on_message(filters.command("repc"))
async def start(client, message):
    # Create a reply keyboard with 4 buttons
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("Button 1")],
        [KeyboardButton("Button 2")],
        [KeyboardButton("Button 3")],
        [KeyboardButton("Button 4")]
    ], resize_keyboard=True)  # Resize the keyboard to fit the screen
    # Send a message with the reply keyboard
    await message.reply("Choose an option:", reply_markup=keyboard)

# Define a message handler for the buttons
@bot.on_message(filters.text)
async def handle_button(client, message):
    text = message.text
    if text == "Button 1":
        await message.reply("You pressed Button 1")
    elif text == "Button 2":
        await message.reply("You pressed Button 2")
    elif text == "Button 3":
        await message.reply("You pressed Button 3")
    elif text == "Button 4":
        await message.reply("You pressed Button 4")
    else:
        await message.reply("Unknown button")

# print in terminal to check code  is running 
print("running")
bot.run()