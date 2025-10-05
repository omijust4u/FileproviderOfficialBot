import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Bot token
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📋 Menu", callback_data='menu')],
        [InlineKeyboardButton("ℹ️ About Us", callback_data='about')],
        [InlineKeyboardButton("💎 VIP Channels", callback_data='vip')],
        [InlineKeyboardButton("💳 Payment Methods", callback_data='payment')],
        [InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof')],
        [InlineKeyboardButton("📱 Social Media", callback_data='social')],
        [InlineKeyboardButton("👨‍💼 Talk with Admin", callback_data='admin')],
        [InlineKeyboardButton("❓ Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = "🤖 Welcome to VIP Service Bot!\n\nChoose an option:"
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def handle_menu(update, context):
    query = update.callback_query
    query.answer()
    
    data = query.data
    
    if data == 'menu':
        keyboard = [
            [InlineKeyboardButton("📋 Menu", callback_data='menu')],
            [InlineKeyboardButton("ℹ️ About Us", callback_data='about')],
            [InlineKeyboardButton("💎 VIP Channels", callback_data='vip')],
            [InlineKeyboardButton("💳 Payment Methods", callback_data='payment')],
            [InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof')],
            [InlineKeyboardButton("📱 Social Media", callback_data='social')],
            [InlineKeyboardButton("👨‍💼 Talk with Admin", callback_data='admin')],
            [InlineKeyboardButton("❓ Help", callback_data='help')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("🎯 Main Menu - Select option:", reply_markup=reply_markup)
    
    elif data == 'about':
        text = """🏢 About Us

We provide premium VIP channels with:
• Exclusive content
• Daily updates  
• 24/7 support
• Secure payments"""
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'vip':
        text = """💎 VIP Channels & Pricing

Basic - $10/month
• Channel 1, 2
• Daily updates

Premium - $20/month  
• All Basic + Channel 3,4
• Priority support

Ultimate - $30/month
• All Premium + Channel 5,6
• 24/7 support"""
        keyboard = [
            [InlineKeyboardButton("💳 Payment", callback_data='payment')],
            [InlineKeyboardButton("🔙 Back", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'payment':
        text = """💳 Payment Methods

We accept:
• PayPal: paypal@example.com
• Crypto: BTC, ETH, USDT
• Bank Transfer

Payment proof admin ko bhejein."""
        keyboard = [
            [InlineKeyboardButton("👨‍💼 Admin", callback_data='admin')],
            [InlineKeyboardButton("🔙 Back", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'proof':
        text = """📸 Payment Proof

Payment proof bhejne ke liye:
1. Screenshot lein
2. Admin ko bhejein
3. 24 hours mein verify"""
        keyboard = [
            [InlineKeyboardButton("👨‍💼 Admin", callback_data='admin')],
            [InlineKeyboardButton("🔙 Back", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'social':
        text = """📱 Social Media

• Twitter: @OurService
• Instagram: @OurService  
• Telegram: @OurChannel

Follow for updates!"""
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'admin':
        text = """👨‍💼 Contact Admin

Admin se contact:
📧 Email: admin@example.com
👤 Telegram: @AdminUsername

Response: 2-4 hours"""
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)
    
    elif data == 'help':
        text = """❓ Help Center

Common Issues:
• Payment verify? - Wait 24 hours
• Channel access? - Check subscription
• Payment issue? - Try alternative

Contact: @AdminUsername"""
        keyboard = [
            [InlineKeyboardButton("👨‍💼 Admin", callback_data='admin')],
            [InlineKeyboardButton("🔙 Back", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup)

def main():
    print("🚀 Starting Bot...")
    
    try:
        updater = Updater(BOT_TOKEN)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(handle_menu))
        
        print("✅ Bot Started Successfully!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
