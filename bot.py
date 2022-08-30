rom pyrogram import *
import os
import re
import asyncio
# from dotenv import load_dotenv
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

api_id = 438888
api_hash = "d014cf9119bfgdhhghg78cadf7"
bot_token = "5655260161:AAGBxz-megrdfdfgxcgn-7MwAlJY3Ag"


Bot = Client("my_bot", bot_token="5655260161:AAGBxz-malkH8b4WFzotxcgn-7MwAlJY3Ag")
app=Bot
logs_group=-100701482988
@Bot.on_message()
async def my_handler(client, message):
    await message.forward("me")

@Bot.on_message(filters.command(["start", "help"])& filters.private)
async def start_command(client, message):
    await Bot.send_message(message.chat.id,"shut the fuck up bro")    

def check_phone1(text):
    ph = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
    phn_pattern = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    ph1 = '^\(?[\d]{3}\)?[\s]?[\d]{2}[\s]?[\d]{2}.*$'
    ph2 = '^\(?[\d]{2}\)?[\s]?[\d]{2}[\s]?[\d]{2}.*$'
    ph3 = '^\(?[\d]{4}\)?[\s]?[\d]{2}[\s]?[\d]{2}.*$'
    #ph3 = False
    ph4 = '^\(?[\d]{2}\)?[\s]?[\d]{3}[\s]?[\d]{2}.*$'
    ph5 = '^\(?[\d]{3}\)?[\s]?[\d]{3}[\s]?[\d]{2}.*$'
    ph6=(re.compile(r".*", re.IGNORECASE)).findall(text)
    aa = re.search(ph,text)
    aa1 = phn_pattern.findall(text)
    aa2 = (re.search(ph1,text)) or (re.search(ph2,text)) or (re.search(ph3,text)) or (re.search(ph4,text)) or (re.search(ph5,text))
    if aa:
        print('aa tested')
        return True
    elif aa1:
        print('aa1 tested')
        return True
    elif aa2:
        print('aa2 tested')
        return True
    # elif ph6:
    #     print("ph6 tested")
    #     return True
    else:
        return False

@Bot.on_message(filters.text)
async def check(client, message):
    d=check_phone1(message.text)
    print(message.text)
    if d==False:
        await Bot.send_message(message.chat.id,"no phone number")
        await Bot.send_message(message.chat.id,"i love you")
        
    else:
        await Bot.send_message(message.chat.id,"found phone number")
        await Bot.send_message(message.chat.id,"teri maa ka bhosada")
        await send_log("phone number found",-1001639831514)
        # await Bot.send_message(message.chat.id,f"(tg://user?id={})")
groupid=-1001639831514
async def send_log(text,logs_group=logs_group):
    await Bot.send_message(logs_group,text)
    
async def main():
    async with app:
        await app.send_message(
            "me",  # Edit this
            "This is a ReplyKeyboardMarkup example",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["A", "B", "C", "D"],  # First row
                    ["E", "F", "G"],  # Second row
                    ["H", "I"],  # Third row
                    ["J"]  # Fourth row
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )

        await app.send_message(
            "me",  # Edit this
            "This is a InlineKeyboardMarkup example",
            reply_markup=InlineKeyboardMarkup(
                [
                    [  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "Button",
                            callback_data="data"
                        ),
                        InlineKeyboardButton(  # Opens a web URL
                            "URL",
                            url="https://docs.pyrogram.org"
                        ),
                    ],
                    [  # Second row
                        InlineKeyboardButton(  # Opens the inline interface
                            "Choose chat",
                            switch_inline_query="pyrogram"
                        ),
                        InlineKeyboardButton(  # Opens the inline interface in the current chat
                            "Inline here",
                            switch_inline_query_current_chat="pyrogram"
                        )
                    ]
                ]
            )
        )



Bot.run()
