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

@bot.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply_text(message.text)

#  3-welcome

GROUP = "#" #Group id/username and also can be a list
WELCOME_MESSAGE = "Welcome!" #message

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members) #filter new members
def welcome(client, message):
    message.reply_text(WELCOME_MESSAGE)#pay attention in groups quote default is True

# print in terminal to check code  is running 
print("running")
bot.run()