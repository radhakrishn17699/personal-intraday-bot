import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN not found. "
        "Create a .env file and add your bot token."
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Personal Intraday Trading Bot is online!\n\n"
        "Commands:\n"
        "/start - Check bot status\n"
        "/help - Show commands"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Available commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show help\n\n"
        "Coming soon:\n"
        "📊 /setup - Intraday setup\n"
        "📈 /stock - Stock analysis\n"
        "📰 /news - Latest verified news\n"
        "🌙 /aftermarket - After-market study"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot is starting...")

    app.run_polling()


if __name__ == "__main__":
    main()
