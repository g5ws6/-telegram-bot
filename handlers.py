from telegram import Update
from telegram.ext import ContextTypes

from ai import ask_ai


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في BulldozerAI\n\nاكتب أي سؤال وسأجيبك."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    reply = ask_ai(user_message)

    await update.message.reply_text(reply)
