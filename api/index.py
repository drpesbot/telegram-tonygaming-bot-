import os
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("TOKEN")

app = FastAPI()

async def start(update: Update, context):
    await update.message.reply_text(
        "**❤️اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد 👇👇\n❤️هذا هو الرابط تفضل بالضغط عليه 👇👇\nhttps://t.me/pes224\n👆👆👆👆👆👆👆**",
        parse_mode='MarkdownV2'
    )

async def echo(update: Update, context):
    await update.message.reply_text(
        "**❤️اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد 👇👇\n❤️هذا هو الرابط تفضل بالضغط عليه 👇👇\nhttps://t.me/pes224\n👆👆👆👆👆👆👆**",
        parse_mode='MarkdownV2'
    )

@app.post("/webhook")
async def webhook(request: Request):
    # Get the JSON data from the request body
    webhook_data = await request.json()

    # Initialize the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Process the update
    update = Update.de_json(webhook_data, application.bot)
    await application.process_update(update)

    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}


