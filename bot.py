from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس  ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="6711048210:AAGeTTCLCXyBmcgcgC264YPkmI5g5xBJSnQ",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "H_8_o"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
