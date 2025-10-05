import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Bot token - ye aapko set karna hoga
BOT_TOKEN = "8483748301:AAEtNbx1_VKD5UqS6FzPhkzjkWrev1Sz66o"

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
    
    welcome_text = """
🤖 **Welcome to VIP Service Bot!**

Choose an option from the menu below to get started.
    """
    update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

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
        query.edit_message_text("🎯 **Main Menu**\n\nSelect an option:", reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'about':
        text = """🏢 **About Us**

We provide premium VIP channels with:
• Exclusive content
• Daily updates  
• 24/7 support
• Secure payments

100% customer satisfaction!"""
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'vip':
        text = """💎 **VIP Channel List & Pricing**

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

💫 **Special Offer: 3 months - 20% discount!**"""
        keyboard = [
            [InlineKeyboardButton("💳 Make Payment", callback_data='payment')],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'payment':
        text = """💳 **Payment Methods**

We accept following payment methods:

• **PayPal** - send to: paypal@example.com
• **Cryptocurrency** 
  BTC: 1ABC123...
  ETH: 0x123...
• **Bank Transfer**
  Account details available on request

After payment, please send screenshot as proof."""
        keyboard = [
            [InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof')],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'proof':
        text = """📸 **Send Payment Proof**

Please send your payment screenshot/receipt here.

**Instructions:**
1. Take clear screenshot of payment confirmation
2. Send it as photo/document
3. Include your username in message
4. We'll verify within 24 hours

After verification, you'll be added to VIP channels."""
        keyboard = [
            [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'social':
        text = """📱 **Follow Us on Social Media**

Stay updated with our latest news and offers:

• **Twitter**: [@OurService](https://twitter.com/OurService)
• **Instagram**: [@OurService](https://instagram.com/OurService)
• **Telegram Channel**: [@OurChannel](https://t.me/OurChannel)

Follow us for updates and announcements!"""
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'admin':
        text = """👨‍💼 **Talk with Admin**

You can contact our admin directly:

📧 **Email**: admin@example.com
👤 **Telegram**: @AdminUsername

**Office Hours:**
Monday-Friday: 9AM-6PM
Saturday: 10AM-2PM

We typically respond within 2-4 hours."""
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == 'help':
        text = """❓ **Help Center**

**Common Issues:**

🔹 **Payment not verified?**
Wait 24 hours, then contact admin

🔹 **Can't access channel?**
Check if subscription is active

🔹 **Payment method not working?**
Try alternative method

For immediate assistance, contact @AdminUsername"""
        keyboard = [
            [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    print("🚀 Starting Telegram Bot...")
    
    try:
        updater = Updater(BOT_TOKEN)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(handle_menu))
        
        print("✅ Bot Started Successfully!")
        print("🤖 Bot is now running...")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
