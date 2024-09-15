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


#==============================MAIN_HELP_CMD====================
#==============================MAIN_HELP_CMD====================
#==============================MAIN_HELP_CMD====================
TEXT_HP = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings3"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings2"),
    ],
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

TEXT_HP2 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP2 = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings3"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings2$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP2.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP2),
        disable_web_page_preview=True,
    )

TEXT_HP3 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP3 = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings2"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings3$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP3.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP3),
        disable_web_page_preview=True,
    )

#=============================EXTRA_CMD================================
#=============================EXTRA_CMD================================

text_act = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Acᴛɪᴠᴇ:

々 /ac - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ ʙᴏᴛ.

々 /activevoice - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /activevideo - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /stats - Cʜᴇᴄᴋ Bᴏᴛs Sᴛᴀᴛs
"""
buttons_act = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^act$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_act,
        reply_markup=InlineKeyboardMarkup(buttons_act),
        disable_web_page_preview=True,
    )


text_adm = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Adᴍɪɴ:
c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /pause ᴏʀ /cpause - Pᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /resume ᴏʀ /cresume - Rᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ.
々 /mute ᴏʀ /cmute - Mᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /unmute ᴏʀ /cunmute - Uɴᴍᴜᴛᴇ ᴛʜᴇ ᴍᴜᴛᴇᴅ ᴍᴜsɪᴄ.
々 /skip ᴏʀ /cskip - Sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /stop ᴏʀ /cstop - Sᴛᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /shuffle ᴏʀ /cshuffle - Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ.
々 /seek ᴏʀ /cseek - Fᴏʀᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /seekback ᴏʀ /cseekback - Bᴀᴄᴋᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /reboot - Rᴇʙᴏᴏᴛ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /skip ᴏʀ /cskip [Nᴜᴍʙᴇʀ (ᴇxᴀᴍᴘʟᴇ: 𝟹)] - Sᴋɪᴘs ᴍᴜsɪᴄ ᴛᴏ ᴀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ǫᴜᴇᴜᴇᴅ ɴᴜᴍʙᴇʀ. Exᴀᴍᴘʟᴇ: /skip 𝟹 ᴡɪʟʟ sᴋɪᴘ ᴍᴜsɪᴄ ᴛᴏ ᴛʜɪʀᴅ ǫᴜᴇᴜᴇᴅ ᴍᴜsɪᴄ ᴀɴᴅ ᴡɪʟʟ ɪɢɴᴏʀᴇ 𝟷 ᴀɴᴅ 𝟸 ᴍᴜsɪᴄ ɪɴ ǫᴜᴇᴜᴇ.
々 /loop ᴏʀ /cloop [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] ᴏʀ [Nᴜᴍʙᴇʀs ʙᴇᴛᴡᴇᴇɴ 𝟷-𝟷𝟶] - Wʜᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ, ʙᴏᴛ ʟᴏᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴛᴏ 𝟷-𝟷𝟶 ᴛɪᴍᴇs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. Dᴇғᴀᴜʟᴛ ᴛᴏ 𝟷𝟶 ᴛɪᴍᴇs.
"""
buttons_adm = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^adm$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_adm,
        reply_markup=InlineKeyboardMarkup(buttons_adm),
        disable_web_page_preview=True,
    )


text_aut = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Auᴛʜ:

Aᴜᴛʜ Usᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /auth [Usᴇʀɴᴀᴍᴇ] - Aᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /unauth [Usᴇʀɴᴀᴍᴇ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /authusers - Cʜᴇᴄᴋ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_aut = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^aut$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_aut,
        reply_markup=InlineKeyboardMarkup(buttons_aut),
        disable_web_page_preview=True,
    )


text_adv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴅᴠɪᴄᴇ:

々 /advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ
々 /astronomical - ᴛᴏ ɢᴇᴛ ᴛᴏᴅᴀʏ's ᴀsᴛʀᴏɴᴏᴍɪᴄᴀʟ  ғᴀᴄᴛ
"""
buttons_adv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^adv$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_adv,
        reply_markup=InlineKeyboardMarkup(buttons_adv),
        disable_web_page_preview=True,
    )


text_apr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴘᴘʀᴏᴠᴇ:

Tʜɪs ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛ ᴄʜᴀᴛ ɪᴏɪɴ ʀᴇǫᴜᴇsᴛ sᴇɴᴅ ʙʏ ᴀ ᴜsᴇʀ ᴛʜʀᴏᴜɢʜ ɪɴᴠɪᴛᴀᴛɪᴏɴ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ

Mᴏᴅᴇs:
ᴡʜᴇɴ ʏᴏᴜ sᴇɴᴅ /autoapprove ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʏᴏᴜ sᴇᴇ ᴛᴜʀɴ ᴏɴ ʙᴜᴛᴛᴏɴ ɪғ ᴀᴜᴛᴛᴏᴘʀᴏᴠᴇ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ ɪғ ᴀʟʀᴇᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ʏᴏᴜ ᴡɪʟʟ sᴇ ᴛᴡᴏ ᴍᴏᴅᴇs ᴛʜᴀᴛ's ᴀʀᴇ ʙᴇʟᴏᴡ ᴀɴᴅ ʜɪs ᴜsᴀsɢᴇ


々 Automatic - ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛs ᴄʜᴀᴛ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ.

々 Manual - ᴀ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ʙʏ ᴛᴀɢɢɪɴɢ ᴛʜᴇ ᴀᴅᴍɪɴs. ᴛʜᴇ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴄᴄᴇᴘᴛ ᴏʀ ᴅᴇᴄʟɪɴᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛs.

々 /clearpending ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴘᴇɴᴅɪɴɢ ᴜsᴇʀ ɪᴅ ғʀᴏᴍ ᴅʙ. ᴛʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴇɴᴅ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ.
"""
buttons_apr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^apr$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_apr,
        reply_markup=InlineKeyboardMarkup(buttons_apr),
        disable_web_page_preview=True,
    )


text_blt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ B-ʟɪsᴛ:

々 /blacklistchat [ᴄʜᴀᴛ ɪᴅ] - Bʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /whitelistchat [ᴄʜᴀᴛ ɪᴅ] - Wʜɪᴛᴇʟɪsᴛ ᴀɴʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /blacklistedchat - Cʜᴇᴄᴋ ᴀʟʟ ʙʟᴏᴄᴋᴇᴅ ᴄʜᴀᴛs.

々 /block [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Pʀᴇᴠᴇɴᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.
々 /unblock [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's Bʟᴏᴄᴋᴇᴅ Lɪsᴛ.
々 /blockedusers - Cʜᴇᴄᴋ ʙʟᴏᴄᴋᴇᴅ Usᴇʀs Lɪsᴛs

ⓘ /gban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Gʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴏᴘ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.
ⓘ /ungban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's ɢʙᴀɴɴᴇᴅ Lɪsᴛ ᴀɴᴅ ᴀʟʟᴏᴡ ʜɪᴍ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
ⓘ /gbannedusers - Cʜᴇᴄᴋ Gʙᴀɴɴᴇᴅ Usᴇʀs Lɪsᴛs
"""
buttons_blt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^blt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_blt,
        reply_markup=InlineKeyboardMarkup(buttons_blt),
        disable_web_page_preview=True,
    )


text_bt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Boᴛ:

々 c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /stats - Gᴇᴛ Tᴏᴘ 𝟷𝟶 Tʀᴀᴄᴋs Gʟᴏʙᴀʟ Sᴛᴀᴛs, Tᴏᴘ 𝟷𝟶 Usᴇʀs ᴏғ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Cʜᴀᴛs ᴏɴ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Pʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

々 /sudolist - Cʜᴇᴄᴋ Sᴜᴅᴏ Usᴇʀs ᴏғ Bᴏᴛ

々 /lyrics [Mᴜsɪᴄ Nᴀᴍᴇ] - Sᴇᴀʀᴄʜᴇs Lʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ Mᴜsɪᴄ ᴏɴ ᴡᴇʙ.

々 /player - Gᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ Pʟᴀʏɪɴɢ Pᴀɴᴇʟ.

々 /queue ᴏʀ /cqueue - Cʜᴇᴄᴋ Qᴜᴇᴜᴇ Lɪsᴛ ᴏғ Mᴜsɪᴄ.

    ⚡️Pʀɪᴠᴀᴛᴇ Bᴏᴛ:  
ⓘ /authorize [CHAT_ID] - Aʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /unauthorize[CHAT_ID] - Dɪsᴀʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /authorized - Cʜᴇᴄᴋ ᴀʟʟ ᴀʟʟᴏᴡᴇᴅ ᴄʜᴀᴛs ᴏғ ʏᴏᴜʀ ʙᴏᴛ.
"""
buttons_bt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^bt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bt,
        reply_markup=InlineKeyboardMarkup(buttons_bt),
        disable_web_page_preview=True,
    )


text_bn = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴀɴ:

/ban - Ban A User
/banall - Ban All Users
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message
/unpinall - unpinall messages
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins.
"""
buttons_bn = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^bn$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bn,
        reply_markup=InlineKeyboardMarkup(buttons_bn),
        disable_web_page_preview=True,
    )


text_bts = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛs:

ʙᴏᴛs

々 /bots - ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ʙᴏᴛs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_bts = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^bts$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bts,
        reply_markup=InlineKeyboardMarkup(buttons_bts),
        disable_web_page_preview=True,
    )


text_bsk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛsᴄʜᴋ:

Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Cʜᴇᴄᴋs ᴛʜᴇ ᴏɴɪɴᴇ sᴛᴀᴛᴜs ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ʙʏ sᴇɴᴅɪɴɢ ɪᴛ ᴀ /start ᴍᴇssᴀɢᴇ.

Usᴀɢᴇ:
/botschk Bᴏᴛ_Usᴇʀɴᴀᴍᴇ

Dᴇᴛᴀɪs:
々 Sᴇɴᴅs /start ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋs ɪғ ɪᴛ ʀᴇsᴘᴏɴᴅs.
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's sᴛᴀᴛᴜs ᴀs ᴇɪᴛʜᴇʀ ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Exᴀᴍᴘᴇs:
々 /botschk @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ: Cʜᴇᴄᴋs ɪғ @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ ɪs ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Nᴏᴛᴇs:
々 Tʜᴇ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ ᴍᴜsᴛ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴀs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ.
々 Tʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪ ᴅɪsᴘᴀʏ ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ɪғ ᴛʜᴇ ᴜsᴇʀɴᴀᴍᴇ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ ᴏʀ ɪғ ᴛʜᴇʀᴇ ᴀʀᴇ ɪᴍɪᴛᴀᴛɪᴏɴs.

Oᴜᴛᴘᴜᴛ:
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's ᴍᴇɴᴛɪᴏɴ ᴀɴᴅ ɪᴛs ᴏɴɪɴᴇ sᴛᴀᴛᴜs.
々 Sʜᴏᴡs ᴛʜᴇ ᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴛɪᴍᴇ.
"""
buttons_bsk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^bsk$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bsk,
        reply_markup=InlineKeyboardMarkup(buttons_bsk),
        disable_web_page_preview=True,
    )


text_ai = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Cʜᴀᴛ Ai:

々 /advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
々 /ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
々 /gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ
々 /bard [ǫᴜᴇʀʏ] -ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ʙᴀʀᴅ ᴀɪ
"""
buttons_ai = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^ai$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_ai,
        reply_markup=InlineKeyboardMarkup(buttons_ai),
        disable_web_page_preview=True,
    )


text_dv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Deᴠ:

🔰Aᴅᴅ Aɴᴅ Rᴇᴍᴏᴠᴇ Sᴜᴅᴏ Usᴇʀ's:
々 /addsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
々 /delsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]

🤖Bᴏᴛ Cᴏᴍᴍᴀɴᴅs:
ⓘ /restart - Rᴇsᴛᴀʀᴛ ʏᴏᴜʀ Bᴏᴛ. 
ⓘ /update , /gitpull - Uᴘᴅᴀᴛᴇ Bᴏᴛ.
ⓘ /speedtest - Cʜᴇᴄᴋ sᴇʀᴠᴇʀ sᴘᴇᴇᴅs
ⓘ /maintenance [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ]
ⓘ /logger [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ] - Bᴏᴛ ʟᴏɢs ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ ǫᴜᴇʀɪᴇs ɪɴ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ.
ⓘ /get_log [Nᴜᴍʙᴇʀ ᴏғ Lɪɴᴇs] - Gᴇᴛ ʟᴏɢ ᴏғ ʏᴏᴜʀ ʙᴏᴛ ғʀᴏᴍ ʜᴇʀᴏᴋᴜ ᴏʀ ᴠᴘs. Wᴏʀᴋs ғᴏʀ ʙᴏᴛʜ.
ⓘ /autoend [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ] - Eɴᴀʙʟᴇ Aᴜᴛᴏ sᴛʀᴇᴀᴍ ᴇɴᴅ ᴀғᴛᴇʀ 𝟹 ᴍɪɴs ɪғ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ.
"""
buttons_dv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^dv$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_dv,
        reply_markup=InlineKeyboardMarkup(buttons_dv),
        disable_web_page_preview=True,
    )
#=============================================================
#=============================================================
#=============================================================

# ==============CLOSE===================
@Bot.on_callback_query(filters.regex("^close$"))
async def close_cb(bot, callback):
    await callback.answer("❌Closed the Module❌")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
