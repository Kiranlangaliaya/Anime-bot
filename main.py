from pyrogram import Client, filters
from pyrogram.types import Message
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
CHANNEL_USER = os.environ.get("CHANNEL_USER")  # without @

bot = Client("filter_bot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.text & filters.group)
async def filter_handler(client, message: Message):
    query = message.text.lower()

    async for msg in bot.search_messages(CHANNEL_USER, query, limit=5):
        try:
            await msg.copy(chat_id=message.chat.id, reply_to_message_id=message.id)
        except:
            pass

bot.run()