from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# GANTI TOKEN INI DENGAN TOKEN BOT LO (sudah gue pasangin)
TOKEN = "8414995980:AAGlhVaWmmjr3ZA1tIlKq0Mgjab-ukCkrdk"

# Fungsi /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🗣 Ngobrol dengan Guru BK", callback_data='chat')],
        [InlineKeyboardButton("📋 Form Pengaduan", callback_data='form')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌿 Selamat datang di Ruang Teduh.\nSilakan pilih layanan di bawah:",
        reply_markup=reply_markup
    )

# Fungsi tombol
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'chat':
        await query.edit_message_text(
            text="✅ Kamu bisa ngobrol dengan Guru BK secara anonim.\nSilakan ketik pesanmu."
        )
    elif query.data == 'form':
        await query.edit_message_text(
            text="📋 Silakan isi form pengaduan di sini:\nhttps://forms.gle/ehcJo..."
        )

# Fungsi utama
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot sudah berjalan. Tekan Ctrl+C untuk keluar.")
    app.run_polling()

if __name__ == "__main__":
    main()
