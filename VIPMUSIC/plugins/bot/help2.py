from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app as Bot

# =============START_CMD====================
TEXT_ST = (
    "👋😄__Hello {},__\n\n"
    "<blockquote> Welcome to the 🎈𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡! This is a powerful⚡🌪️ bot for Telegram.</blockquote>\n\n"
    "**__Click help to know how to use me!__**"
)
BUTTONS_ST = [
    [
        InlineKeyboardButton("Channel 📢", url="https://t.me/XBOTS_X"),
        InlineKeyboardButton("Commands 📚", callback_data="help"),
        InlineKeyboardButton("About 💡", callback_data="abot"),
        InlineKeyboardButton("Sudo 👥", callback_data="sudo"),
    ],
    [InlineKeyboardButton("❌", callback_data="close")],
]


@Bot.on_callback_query(filters.regex("^home$"))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_ST.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_ST),
        disable_web_page_preview=True,
    )


# =============HELP_CMD====================
TEXT_HP = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="close"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="close"),
        InlineKeyboardButton("Auᴛʜ", callback_data="close")
        ],[
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="close"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="close"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="close")
        ],[
        InlineKeyboardButton("Boᴛ", callback_data="close"),
        InlineKeyboardButton("Bᴀɴ", callback_data="close"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="close")
        ],[
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="close"),
        InlineKeyboardButton("CʜᴀᴛGᴘᴛ", callback_data="close"),
        InlineKeyboardButton("Deᴠ", callback_data="close")
        ],[
        InlineKeyboardButton("❮", callback_data="close"),
        InlineKeyboardButton("❌", callback_data="close"), 
        InlineKeyboardButton("❯", callback_data="close")
    ]
]


@Bot.on_message(filters.command("help2") & filters.private)
async def hp_handler(bot, message):
    await message.reply_text(
        text=TEXT_HP.format(message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        quote=True,
    )


@Bot.on_callback_query(filters.regex("^settings$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        disable_web_page_preview=True,
    )


# =============ABOUT_CMD====================
text_ab = (
    "🎈 **AbouT Me** 🎈\n\n"
    "<blockquote expandable>**🤖 Bot Name:**  𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡!\n"
    "**📝 Language:** [Python 3](https://www.python.org/)\n"
    "**🧰 Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n"
    "**👨‍💻 Developer:** [VGX.LEO](https://t.me/Vignesh_leo)\n"
    "**📢 Updates Channel:** [X Bots](https://t.me/Xbots_x)\n"
    "**👥 Support Group:** [X Support](https://t.me/sp)</blockquote>"
)
buttons_ab = [
    [
        InlineKeyboardButton("⬅️", callback_data="home"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_message(filters.command("about") & filters.private)
async def ab_handler(bot, message):
    await message.reply_text(
        text=text_ab,
        reply_markup=InlineKeyboardMarkup(buttons_ab),
        quote=True,
        parse_mode=enums.ParseMode.HTML,
    )


@Bot.on_callback_query(filters.regex("^abot$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_ab,
        reply_markup=InlineKeyboardMarkup(buttons_ab),
        disable_web_page_preview=True,
    )


# ==============CLOSE===================
@Bot.on_callback_query(filters.regex("^close$"))
async def close_cb(bot, callback):
    await callback.answer("❌Closed the Module❌")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
