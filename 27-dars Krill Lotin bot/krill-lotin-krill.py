import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "5503875646:AAGtAAESPldR3rYVLle4iagHTWweg-45FPA" 
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    xabar = f"Assalom alaykum, {message.from_user.first.name}\nKrill-Lotin-Krill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()


