from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
مرحبا بك {} في بوت {} هذا البوت مخصص لاستخراج كود تيرمكس .. تيليثون وبيروقرام .. المطور :: @YDDDE ::
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(- بدأ استخراج تيرمكس .", callback_data="generate")],
        [InlineKeyboardButton(text="- القائمة الرئيسية .", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- بدأ استخراج تيرمكس .", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- بدأ ستخراج تيرمكس .", callback_data="generate")],
        [InlineKeyboardButton("- صنع بواسطة", url="https://t.me/YDDDE")],
        [
            InlineKeyboardButton("- طريقة الاستعمال ؟ .", callback_data="help"),
            InlineKeyboardButton("- معلومات .", callback_data="about")
        ],
        [InlineKeyboardButton("- القناة .", url="https://t.me/zvvvn")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - about the bot
/help - This Message
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
**About this bot**

A telegram bot to take pyrogram and telethon string session by @zVVVn

Group Support: [Join] (https://t.me/XFFFW)

Framework: [pyrogram] (docs.pyrogramrogram.org)

Language: [python] (www.python.org)

Developer: @YDDDE
    """
