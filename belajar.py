import telebot
from telebot import types

TOKEN = "8973716483:AAEc9KJCZPuxWGz1czdc_N2BCWMrWBAy7ns"
bot = telebot.TeleBot(TOKEN)
pesanan = {}

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛍️ Harga", "🛒 Order")
    markup.add("📱 Kontak", "❓ Bantuan")
    bot.reply_to(message, "halo! selamat datang di toko kinta 🔥\npilih menu:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🛍️ Harga")
def harga(message):
    bot.reply_to(message, "📦 daftar harga:\n- hoodie: Rp 85.000\n- kaos: Rp 55.000\n- celana: Rp 95.000")

@bot.message_handler(func=lambda message: message.text == "🛒 Order")
def order(message):
    pesanan[message.chat.id] = "waiting"
    bot.reply_to(message, "mau order apa? ketik nama produk + ukuran\ncontoh: hoodie L")

@bot.message_handler(func=lambda message: message.chat.id in pesanan and pesanan[message.chat.id] == "waiting")
def proses_order(message):
    pesanan[message.chat.id] = message.text
    bot.reply_to(message, f"✅ order diterima!\nproduk: {message.text}\n\namin segera dihubungi untuk konfirmasi pembayaran 😊")

@bot.message_handler(func=lambda message: message.text == "📱 Kontak")
def kontak(message):
    bot.reply_to(message, "📱 hubungi admin:\nWA: 08xxxxxxxxxx\nIG: @apalah")

@bot.message_handler(func=lambda message: message.text == "❓ Bantuan")
def bantuan(message):
    bot.reply_to(message, "tekan tombol menu di bawah ya! 😊")

@bot.message_handler(func=lambda message: True)
def balas(message):
    bot.reply_to(message, "halo! tekan /start untuk mulai 😊")

bot.polling()