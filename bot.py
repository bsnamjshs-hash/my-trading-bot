import time
import requests
import telebot

TELEGRAM_TOKEN = "8431068671:AAFlBGJlpLXKxeVUB16yD57xmn1GPAGAT6M"
CHAT_ID = "5592644721"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "🚀 **بوت التداول الذكي يعمل بنجاح!**\n\nأرسل /price لمعرفة السعر الحالي.")

@bot.message_handler(commands=['price'])
def send_price(message):
    price = get_crypto_price()
    bot.send_message(message.chat.id, f"💵 **سعر البيتكوين الحالي:** `{price}$`", parse_mode='Markdown')

if __name__ == "__main__":
    bot.send_message(CHAT_ID, "✅ **تم تشغيل سيرفر البوت بنجاح!**")
    bot.polling(non_stop=True)
