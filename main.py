from typing import Final
from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters

# Create a file 'token' with the token
TOKEN: Final = open("token", "r").read().strip()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I was only in my mind\n" +
        "You were on the outside waiting\n" +
        "I could feel you all the time\n" +
        "Your voice could save me\n" +
        "Now all these Sirens sing for me\n" +
        "But I just wanna hear your melody\n" +
        "I call and I can hear you sing\n" +
        "But oh\n" +
        "It's only my echo\n" +
        "It's only my echo\n"
    )
    
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    
    
    print("Polling...")
    app.run_polling(3)