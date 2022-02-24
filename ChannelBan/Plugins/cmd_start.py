from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!</b>
 `Heya I'm A Anti-Channel telegram bot to delete and ban message sent by channels in groups`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/international_english_chattings"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "IFCC Admin", url="https://t.me/IFCR_BOT"
                    )
                ]
            ]
        )
    )
