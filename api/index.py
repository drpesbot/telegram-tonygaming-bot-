import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot

TOKEN = os.environ.get("TOKEN")  # التوكن هيتحدد في Vercel

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    bot = Bot(token=TOKEN)
    update = Update.de_json(await request.json(), bot)

    if update.message:
        chat_id = update.message.chat_id
        text = update.message.text

        # الرسالة المطلوبة للبوت الجديد مع تنسيق الخط العريض
        response_message = "**❤️اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد 👇👇\n❤️هذا هو الرابط تفضل بالضغط عليه 👇👇\nhttps://t.me/pes224\n👆👆👆👆👆👆👆**"

        if text == "/start":
            await bot.send_message(
                chat_id=chat_id,
                text=response_message,
                parse_mode='MarkdownV2'
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=response_message,
                parse_mode='MarkdownV2'
            )
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}

