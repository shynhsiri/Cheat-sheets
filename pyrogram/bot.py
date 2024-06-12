from dotenv import load_dotenv
import os
from pyrogram import Client, filters

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

#  2/1-reply_text()

@bot.on_message(filters.command('reply'))
def reply(bot, message):
    message.reply_text("reply to message",  quote=True)
   
# 2/2-echo

# @bot.on_message(filters.text & filters.private)
# def echo(client, message):
#     message.reply_text(message.text)

#  3-welcome

GROUP = "#" #Group id/username and also can be a list
WELCOME_MESSAGE = "Welcome!" #message

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members) #filter new members
def welcome(client, message):
    message.reply_text(WELCOME_MESSAGE)#pay attention in groups quote default is True

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

# 5-delete_message

@bot.on_message(filters.text)
def delete_text(bot, message):
    word_list =  ["fuck", "wtf"]
    if any(word in message.text.lower() for word in word_list):
        bot.delete_messages(message.chat.id, [message.id])
        bot.send_message(message.chat.id, "Blocklist word detected!")

# print in terminal to check code  is running 
print("running")
bot.run()