import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- BOT TOKEN Setup ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
FALLBACK_TOKEN = "8483748301:AAGSC3jQ05PikEsKYnD6nvCt_BD_LV18-po"  # <-- अपने BotFather token डालो

if not BOT_TOKEN:
    print("⚠️ BOT_TOKEN not found in Environment, using fallback token.")
    BOT_TOKEN = FALLBACK_TOKEN

# --- Start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 VIP Channel List", callback_data="vip")],
        [InlineKeyboardButton("💰 Payment Options", callback_data="payment")],
        [InlineKeyboardButton("📸 Send Payment Proof", callback_data="proof")],
        [InlineKeyboardButton("🧑‍💻 Talk with Admin", callback_data="admin")],
        [InlineKeyboardButton("🌐 Social Media", callback_data="social")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome to *Fileprovider Official Network Bot!*\n\nSelect an option below:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Button Handlers ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "vip":
        keyboard = [[InlineKeyboardButton(f"Channel {i}", callback_data=f"ch{i}")] for i in range(1, 21)]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📜 *VIP Channel List:*\nSelect a channel below:", parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data.startswith("ch"):
        await query.edit_message_text(f"📢 *Channel Info for {query.data.replace('ch','Channel ')}*\nJoin link or details here...", parse_mode="Markdown")

    elif query.data == "payment":
        keyboard = [
            [InlineKeyboardButton("UPI 1", callback_data="upi1")],
            [InlineKeyboardButton("UPI 2", callback_data="upi2")],
            [InlineKeyboardButton("Crypto", callback_data="crypto")],
            [InlineKeyboardButton("PayPal", callback_data="paypal")],
            [InlineKeyboardButton("Others", callback_data="otherpay")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("💰 *Choose Payment Method:*", parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data in ["upi1","upi2","crypto","paypal","otherpay"]:
        await query.edit_message_text(f"🪙 Payment option selected: *{query.data.upper()}*\nSend amount to respective account.", parse_mode="Markdown")

    elif query.data == "proof":
        await query.edit_message_text("📸 *Send Payment Proof Instructions:*\nPlease send screenshot to admin on Telegram: @fpofficialadminbot", parse_mode="Markdown")

    elif query.data == "admin":
        await query.edit_message_text("🧑‍💻 *Talk with Admin:*\nMessage our admin at 👉 @fpofficialadminbot", parse_mode="Markdown")

    elif query.data == "social":
        keyboard = [
            [InlineKeyboardButton("Telegram", url="https://t.me/fpofficialnetwork")],
            [InlineKeyboardButton("Instagram", url="https://instagram.com/fpofficialnetwork")],
            [InlineKeyboardButton("Facebook", url="https://facebook.com/fpofficialnetwork")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Follow us on Social Media:*", parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "help":
        await query.edit_message_text("❓ *Help / FAQ:*\n1️⃣ Join VIP channel → Make payment\n2️⃣ Send proof → Wait for confirmation\n3️⃣ Need help? Contact admin.", parse_mode="Markdown")

# --- Main Function ---
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("✅ Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
