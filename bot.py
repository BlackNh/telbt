from email import message
from http import client
import types
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
import COVID19Py

bot = Client(
    session_name="Robot",
    api_id= 18700603,
    api_hash= "15cb7f0ad5e7868d9327b69988c9c94d",
    bot_token= "2026527558:AAGHD8Xo3wIDvCp1XQ3RClJnuiRiWH88LLA"
)
#--------------------# Bot Send #--------------------#
async def Start(client,message):
    chat_id = message.chat.id
    user = message.chat.first_name 
    mark = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("Wallpaper🖼"),
        KeyboardButton("Music🎧"),
        KeyboardButton("Covid19🦠")
        ],
        [KeyboardButton("About"),
        KeyboardButton("Wather"),
        KeyboardButton("Support")
        ]
        ],resize_keyboard=True)
    await bot.send_message(chat_id,f"""
    سلام {user} عزیز
    به ربات همه کاره خوش اومدی
    """,reply_markup=mark)
async def Music(client,message):
    pass
async def Wallpaper(client,message):
    pass
async def Covid19(client,message):
    chat_id = message.chat.id
    covid19 = COVID19Py.COVID19()
    locationn = covid19.getLocationByCountryCode("IR")
    countryy= locationn['country']
    countryy =countryy.replace("   ","")
    for i in locationn:
        await bot.send_message(chat_id, f"""
        آمار کرونا ایران
        کشور : {i['country']}
        مبتلایان : {i['latest']['confirmed']}
        فوت شدگان : {i['latest']['deaths']}
        بهبود یافتگان : {i['latest']['recovered']}
        آخرین بروزرسانی : {i['last_updated']}
        توجه:این پیام به صورت خودکار بروزرسانی میشود!
        """)
async def About(client,message):
    await bot.send_message(message.chat.id , "این ربات توسط @god_killer ساخته شده است")
async def Support(client ,message):
    await bot.send_message(message.chat.id ,"""
    لطفا پیام خود را به صورت زیر به ربات ارسال کنید
    /support
    این یک متن تستی است
    """)
async def SupportMessage(client,message):
    txt = message.text
    txt_now = txt.replace("/support" , "")
    print(txt_now)    
#--------------------# Bot Main #--------------------#
@bot.on_message()
async def Main(client,message):
    txt = message.text
    chat_id = message.chat.id
    if txt == "/start":
        await Start(client,message)
    elif txt =="Wallpaper🖼":
        await Wallpaper(client,message)
    elif txt =="Music🎧":
            await Music(client,message)
    elif txt =="Covid19🦠":
        await Covid19(client,message)
    elif txt =="About":
        await About(client,message)
    elif txt =="Wather":
        await Covid19(client,message)
    elif txt =="Support":
        await Support(client,message)
    elif txt[0:8] =="/support":
        await SupportMessage(client,message)
    else:
        pass
#--------------------# Start Bot #--------------------#
if __name__ == "__main__":
    bot.run()