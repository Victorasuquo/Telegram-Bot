import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask, request

# Replace 'YOUR_API_TOKEN' with your actual bot token
API_TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

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
    ai_message = (
        "Learn AI:\n"
        "AI is Artificial Intelligence. Check out our AI tutorials here:\n"
        "https://youtu.be/gqN4O8LWNKc?si=1-cYWwxUf1yHnk_J\n"
    )
    await update.message.reply_text(ai_message)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "python":
        await query.edit_message_text(text="Learn Python:\nPython is a versatile programming language. Check out our Python tutorials here:\nhttps://youtu.be/CJIJNmGXPgo?si=NTpgSP6bXN2nMr4W")
    elif query.data == "java":
        await query.edit_message_text(text="Learn Java:\nJava is a powerful programming language. Check out our Java tutorials here:\nhttps://www.java.com/en/")
    elif query.data == "ai":
        await query.edit_message_text(text="Learn AI:\nAI is Artificial Intelligence. Check out our AI tutorials here:\nhttps://youtu.be/gqN4O8LWNKc?si=1-cYWwxUf1yHnk_J")
    elif query.data == "contact":
        await query.edit_message_text(text="Contact us:\nEmail: jacobasuquo199@gmail.com\nPhone: +2349121368136\nWebsite: https://africa.pycon.org/2024/speakers/M0Gg40v/")
@app.route('/')
def home():
    return "Welcome to Marvel Tutorials Hub!", 200


@app.route('/webhook', methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'ok', 200

def main() -> None:
    global application
    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("python", python))
    application.add_handler(CommandHandler("java", java))
    application.add_handler(CommandHandler("ai", ai))
    application.add_handler(CallbackQueryHandler(button))

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()