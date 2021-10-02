from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا بوت الاغاني

بامكاني تشغيل الاغاني في مكالمات الجروبات 
قم برفعي مشرف في الجروب مع البوت المساعد

معـرف البـوت المساعـد في النـبذة

قم باضافتي الى مجموعتك لتشغيل الاغاني**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️ المطـور ️", url="https://t.me/UUOUOU_7")
                  ],[
                    InlineKeyboardButton(
                        " قـناة البوت ", url="https://t.me/BLACK_TEAM_4"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "اضفني الى مجموعتك", url="https://t.me/MU_BL_K_BOT?StartGroup=New"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "للتواصل", url="https://t.me/UUOUOU_7")
                ]
            ]
        )
   )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** البوت يختص بتحميل والبحث عن الاغاني 

ارسل يوزر البوت مع اسم الاغنيه للبحث
مثال : 
معرف البوت + الكلمه

تستطيع تحميل الاغاني ايضا
بالاوامر التاليه :
- /ytp رابط الاغنيه من اليوتيوب
- /song رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه 
- /play بالرد على الاغنيه او الرابط للتشغيل
- /pause لايقاف الاغنيه موقتا داخل المكالمه
- /resume لتكمله الاغنيه المتوقفه
- /stop لايقاف البوت عن تشغيل الاغنيه
- /skip لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " قنـاة البوت", url="https://t.me/BLACK_TEAM_4")
                ],[
                    InlineKeyboardButton(
                        " المطور", url="https://t.me/UUOUOU_7"
                    )
                ]
            ]
        )
   )
