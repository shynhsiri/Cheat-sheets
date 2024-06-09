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


# print in terminal to check code  is running 
print("running")
bot.run()