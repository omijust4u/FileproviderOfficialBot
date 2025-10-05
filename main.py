import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Bot token - Render ke environment variable se lega
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
def start(update: Update, context: CallbackContext):
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
    
    welcome_text = """
🤖 **Welcome to Our VIP Service Bot!**

Choose an option from the menu below to get started.
    """
    update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

# Menu handler
def menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
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
    
    query.edit_message_text(
        "🎯 **Main Menu**\n\nSelect an option:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# About Us
def about_us(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    about_text = """
🏢 **About Us**

We provide premium VIP channels with:
• Exclusive content
• Daily updates  
• 24/7 support
• Secure payments

100% customer satisfaction!
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(about_text, reply_markup=reply_markup, parse_mode='Markdown')

# VIP Channels
def vip_channels(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    vip_text = """
💎 **VIP Channel List & Pricing**

📺 **Basic Package - $10/month**
• Channel 1
• Channel 2
• Daily updates

📺 **Premium Package - $20/month**  
• All Basic channels
• Channel 3
• Channel 4
• Priority support

📺 **Ultimate Package - $30/month**
• All Premium channels  
• Channel 5
• Channel 6
• 24/7 support
    """
    keyboard = [
        [InlineKeyboardButton("💳 Make Payment", callback_data='payment')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(vip_text, reply_markup=reply_markup, parse_mode='Markdown')

# Payment Methods
def payment_methods(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    payment_text = """
💳 **Payment Methods**

We accept:
• PayPal: paypal@example.com
• Crypto: BTC, ETH, USDT
• Bank Transfer

Payment proof bhejne ke liye admin se contact karein.
    """
    keyboard = [
        [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(payment_text, reply_markup=reply_markup, parse_mode='Markdown')

# Payment Proof
def payment_proof(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    proof_text = """
📸 **Send Payment Proof**

Payment proof bhejne ke liye:
1. Screenshot lein
2. Admin ko directly bhejein
3. 24 hours mein verify ho jayega
    """
    keyboard = [
        [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(proof_text, reply_markup=reply_markup, parse_mode='Markdown')

# Social Media
def social_media(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    social_text = """
📱 **Follow Us on Social Media**

• Twitter: @OurService
• Instagram: @OurService  
• Telegram: @OurChannel

Updates ke liye follow karein!
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(social_text, reply_markup=reply_markup, parse_mode='Markdown')

# Talk with Admin
def talk_admin(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    admin_text = """
👨‍💼 **Talk with Admin**

Admin se contact karein:
📧 Email: admin@example.com
👤 Telegram: @AdminUsername

Response time: 2-4 hours
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(admin_text, reply_markup=reply_markup, parse_mode='Markdown')

# Help
def help_command(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    help_text = """
❓ **Help Center**

Common Issues:
• Payment verify nahi hua? - 24 hours wait karein
• Channel access nahi? - Subscription check karein
• Payment method issue? - Alternative try karein

Admin se contact: @AdminUsername
    """
    keyboard = [
        [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')

# Main function
def main():
    print("🤖 Starting Telegram Bot...")
    
    # Bot setup
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    
    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(menu, pattern='menu'))
    dp.add_handler(CallbackQueryHandler(about_us, pattern='about'))
    dp.add_handler(CallbackQueryHandler(vip_channels, pattern='vip'))
    dp.add_handler(CallbackQueryHandler(payment_methods, pattern='payment'))
    dp.add_handler(CallbackQueryHandler(payment_proof, pattern='proof'))
    dp.add_handler(CallbackQueryHandler(social_media, pattern='social'))
    dp.add_handler(CallbackQueryHandler(talk_admin, pattern='admin'))
    dp.add_handler(CallbackQueryHandler(help_command, pattern='help'))
    
    # Start bot
    print("✅ Bot started successfully!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
