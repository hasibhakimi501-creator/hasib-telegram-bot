import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات گروه حسیب غزنوی خوش آمدید.\n\n"
        "دستورها:\n"
        "/help - راهنمای ربات\n"
        "/rules - قوانین گروه\n"
        "/id - نمایش شناسه شما"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 راهنمای ربات\n\n"
        "/start - شروع\n"
        "/help - راهنما\n"
        "/rules - قوانین گروه\n"
        "/id - شناسه کاربر"
    )

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 قوانین گروه:\n\n"
        "1️⃣ احترام به اعضا\n"
        "2️⃣ بدون ارسال اسپم\n"
        "3️⃣ بدون تبلیغات مزاحم\n"
        "4️⃣ رعایت قوانین تلگرام"
    )

async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 شناسه شما:\n{update.effective_user.id}"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN تنظیم نشده است.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("id", user_id))

    app.run_polling()

if __name__ == "__main__":
    main()
