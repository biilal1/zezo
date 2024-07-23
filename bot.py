from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس  ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=9671629,
    api_hash="be5c84e9dc1ca0e2b53d54b71e5751247",
    bot_token="7324813477:AAEU31qskRcD8U-M4IsGpLeGnTT8UIhQRR4",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "BDB0B"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
