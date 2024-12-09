import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace 'YOUR_API_TOKEN' with your actual bot token
API_TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "Welcome to Marvel Tutorials Hub!\n"
        "We teach programming courses. Use the buttons below to navigate or use the following commands:\n"
        "/help - Get a list of available commands\n"
        "/contact - Contact information\n"
    )
    keyboard = [
        [InlineKeyboardButton("Python", callback_data="python")],
        [InlineKeyboardButton("Java", callback_data="java")],
        [InlineKeyboardButton("ai", callback_data="ai")],
        [InlineKeyboardButton("Contact Us", callback_data="contact")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_message = (
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Get a list of available commands\n"
        "/contact - Contact information\n"
        "/python - Learn about Python\n"
        "/java - Learn about Java\n"
        "/ai - Learn about AI\n"
    )
    await update.message.reply_text(help_message)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact_message = (
        "Contact us:\n"
        "Email: jacobasuquo199@gmail.com\n"
        "Phone: +2349121368136\n"
        "Website: https://africa.pycon.org/2024/speakers/M0Gg40v/\n"
    )
    await update.message.reply_text(contact_message)

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    python_message = (
        "Learn Python:\n"
        "Python is a versatile programming language. Check out our Python tutorials here:\n"
        "https://youtu.be/CJIJNmGXPgo?si=NTpgSP6bXN2nMr4W\n"
    )
    await update.message.reply_text(python_message)

async def java(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    java_message = (
        "Learn Java:\n"
        "Java is a powerful programming language. Check out our Java tutorials here:\n"
        "https://www.java.com/en/\n"
    )
    await update.message.reply_text(java_message)

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    csharp_message = (
        "Learn AI:\n"
        "AI is a Artificial Intelligence. Check out our AI tutorials here:\n"
        "https://youtu.be/gqN4O8LWNKc?si=1-cYWwxUf1yHnk_J\n"
    )
    await update.message.reply_text(csharp_message)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "python":
        await query.edit_message_text(text="Learn Python:\nPython is a versatile programming language. Check out our Python tutorials here:\nhttps://youtu.be/CJIJNmGXPgo?si=NTpgSP6bXN2nMr4W")
    elif query.data == "java":
        await query.edit_message_text(text="Learn Java:\nJava is a powerful programming language. Check out our Java tutorials here:\nhttps://www.java.com/en/")
    elif query.data == "ai":
        await query.edit_message_text(text="AI is a Artificial Intelligence. Check out our AI tutorials here:\nhttps://youtu.be/gqN4O8LWNKc?si=1-cYWwxUf1yHnk_J")
        await query.edit_message_text(text="Contact us:\nEmail: jacobasuqo199@gmail.com \nPhone: +2349121368136\nWebsite: https://africa.pycon.org/2024/speakers/M0Gg40v/")

def main() -> None:
    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("python", python))
    application.add_handler(CommandHandler("java", java))
    application.add_handler(CommandHandler("ai", ai))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
