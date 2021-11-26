#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>\n○ ʟᴀɴɢᴜᴀɢᴇ : <code>ᴘʏᴛʜᴏɴ 3</code>\n○ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ {__version__}</a>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/Z_Bots'>ɪ'ᴍ ɴᴏᴛ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ😼</a>\n○ ᴄʜᴀɴɴᴇʟ : @Z_Bots\n○ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @z_bots_support7</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝗖𝗟𝗢𝗦𝗘", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
