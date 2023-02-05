import telebot
import os

TOKEN = os.getenv("TELEBOT_TOKEN", "No token provided")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["test"])
def send_welcome(message):
    bot.reply_to(message, "Working.....")


@bot.message_handler(func=lambda message: True)
def show_options(message):
    bot.reply_to(message, "Welcome! I am your bot, will help you to manage your trade.\n")

bot.polling()
