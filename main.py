import os
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Telegram Bot Token
BOT_TOKEN = os.environ.get("8483748301:AAGSC3jQ05PikEsKYnD6nvCt_BD_LV18-po")

# Flask App (Render ko alive rakhne ke liye)
app = Flask(__name__)

@app.route('/')
def home():
    return "Fileprovider Official Bot is Running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 VIP Channel List", callback_data="vip_list")],
        [InlineKeyboardButton("💰 Payment Options", callback_data="payment_options")],
        [InlineKeyboardButton("📸 Send Payment Proof", callback_data="send_proof")],
        [InlineKeyboardButton("👨‍💼 Talk with Admin", callback_data="talk_admin")],
        [InlineKeyboardButton("🌐 Social Media", callback_data="social_media")],
        [InlineKeyboardButton("❓ Help / FAQ", callback_data="help")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 *Welcome to Fileprovider Official Network Bot!*\n\nChoose an option below 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "vip_list":
        vip_buttons = [
            [InlineKeyboardButton(f"Channel {i+1}", callback_data=f"ch{i+1}")]
            for i in range(20)
        ]
        await query.edit_message_text(
            "💎 *VIP Channel List:*\nSelect a channel 👇",
            reply_markup=InlineKeyboardMarkup(vip_buttons),
            parse_mode="Markdown"
        )

    elif query.data.startswith("ch"):
        ch_num = query.data.replace("ch", "")
        await query.edit_message_text(
            f"📢 *Channel {ch_num} Info:*\n\nयहां Channel {ch_num} की जानकारी रहेगी।\n🔗 https://t.me/fileprovider_channel{ch_num}",
            parse_mode="Markdown"
        )

    elif query.data == "payment_options":
        pay_keyboard = [
            [InlineKeyboardButton("UPI 1", callback_data="upi1")],
            [InlineKeyboardButton("UPI 2", callback_data="upi2")],
            [InlineKeyboardButton("💰 Crypto", callback_data="crypto")],
            [InlineKeyboardButton("💵 PayPal", callback_data="paypal")],
            [InlineKeyboardButton("Others", callback_data="others")],
        ]
        await query.edit_message_text(
            "💰 *Choose your payment option:*",
            reply_markup=InlineKeyboardMarkup(pay_keyboard),
            parse_mode="Markdown"
        )

    elif query.data in ["upi1", "upi2", "crypto", "paypal", "others"]:
        await query.edit_message_text(
            f"✅ *{query.data.upper()} Payment Instructions:*\n\nयहां तुम {query.data.upper()} payment details जोड़ सकते हो।",
            parse_mode="Markdown"
        )

    elif query.data == "send_proof":
        await query.edit_message_text(
            "📸 *Send Payment Proof Instructions:*\n\nकृपया payment screenshot Telegram पर इस ID पर भेजें:\n👉 [@fpofficialadminbot](https://t.me/fpofficialadminbot)",
            parse_mode="Markdown"
        )

    elif query.data == "talk_admin":
        await query.edit_message_text(
            "👨‍💼 *Talk with Admin:*\n\nAdmin से बात करने के लिए यहाँ जाएँ:\n👉 [@fpofficialadminbot](https://t.me/fpofficialadminbot)",
            parse_mode="Markdown"
        )

    elif query.data == "social_media":
        social_keyboard = [
            [InlineKeyboardButton("Telegram", url="https://t.me/yourchannel")],
            [InlineKeyboardButton("Instagram", url="https://instagram.com/yourpage")],
            [InlineKeyboardButton("Facebook", url="https://facebook.com/yourpage")],
        ]
        await query.edit_message_text(
            "🌐 *Follow us on Social Media:*",
            reply_markup=InlineKeyboardMarkup(social_keyboard),
            parse_mode="Markdown"
        )

    elif query.data == "help":
        await query.edit_message_text(
            "❓ *FAQ / Help Section:*\n\n1️⃣ कैसे join करें?\n2️⃣ Payment confirm होने में कितना समय लगता है?\n3️⃣ अगर कोई issue हो तो किससे contact करें?\n\n➡️ जवाब के लिए admin को DM करें।",
            parse_mode="Markdown"
        )

def run_bot():
    app_obj = Application.builder().token(BOT_TOKEN).build()
    app_obj.add_handler(CommandHandler("start", start))
    app_obj.add_handler(CallbackQueryHandler(button))
    print("🤖 Bot is running on Render...")
    app_obj.run_polling()

if __name__ == '__main__':
    from threading import Thread
    Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
