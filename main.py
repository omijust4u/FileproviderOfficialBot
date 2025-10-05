import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Bot configuration - YE BADME CHANGE KARENGE
BOT_TOKEN = os.environ.get('8483748301:AAEtNbx1_VKD5UqS6FzPhkzjkWrev1Sz66o')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
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
    
    await query.edit_message_text(
        "🎯 **Main Menu**\n\nSelect an option:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    about_text = """
🏢 **About Us**

We provide premium content through VIP channels with:
• Exclusive content
• Daily updates
• 24/7 support
• Secure payments

We've been serving customers since 2023 with 100% satisfaction rate.
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(about_text, reply_markup=reply_markup, parse_mode='Markdown')

async def vip_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
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
• Early access

💫 **Special Offer: 3 months - 20% discount!**
    """
    keyboard = [
        [InlineKeyboardButton("💳 Make Payment", callback_data='payment')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(vip_text, reply_markup=reply_markup, parse_mode='Markdown')

async def payment_methods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    payment_text = """
💳 **Payment Methods**

We accept following payment methods:

• **PayPal** - send to: paypal@example.com
• **Cryptocurrency** 
  BTC: 1ABC123...
  ETH: 0x123...
• **Bank Transfer**
  Account details available on request

After payment, please send screenshot as proof.
    """
    keyboard = [
        [InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(payment_text, reply_markup=reply_markup, parse_mode='Markdown')

async def payment_proof(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    proof_text = """
📸 **Send Payment Proof**

Please send your payment screenshot/receipt here.

**Instructions:**
1. Take clear screenshot of payment confirmation
2. Send it as photo/document
3. Include your username in message
4. We'll verify within 24 hours

After verification, you'll be added to VIP channels.
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(proof_text, reply_markup=reply_markup, parse_mode='Markdown')

async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    social_text = """
📱 **Follow Us on Social Media**

Stay updated with our latest news and offers:

• **Twitter**: [@OurService](https://twitter.com/OurService)
• **Instagram**: [@OurService](https://instagram.com/OurService)
• **Telegram Channel**: [@OurChannel](https://t.me/OurChannel)

Follow us for updates and announcements!
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(social_text, reply_markup=reply_markup, parse_mode='Markdown')

async def talk_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    admin_text = """
👨‍💼 **Talk with Admin**

You can contact our admin directly:

📧 **Email**: admin@example.com
👤 **Telegram**: @AdminUsername

**Office Hours:**
Monday-Friday: 9AM-6PM
Saturday: 10AM-2PM

We typically respond within 2-4 hours.
    """
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(admin_text, reply_markup=reply_markup, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    help_text = """
❓ **Help Center**

**Common Issues:**

🔹 **Payment not verified?**
Wait 24 hours, then contact admin

🔹 **Can't access channel?**
Check if subscription is active

🔹 **Payment method not working?**
Try alternative method

For immediate assistance, contact @AdminUsername
    """
    keyboard = [
        [InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin')],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle payment proof photos"""
    user = update.message.from_user
    
    await update.message.reply_text(
        "✅ Thank you! We've received your payment proof. We'll verify it within 24 hours.",
        parse_mode='Markdown'
    )

def main():
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu, pattern='^menu$'))
    application.add_handler(CallbackQueryHandler(about_us, pattern='^about$'))
    application.add_handler(CallbackQueryHandler(vip_channels, pattern='^vip$'))
    application.add_handler(CallbackQueryHandler(payment_methods, pattern='^payment$'))
    application.add_handler(CallbackQueryHandler(payment_proof, pattern='^proof$'))
    application.add_handler(CallbackQueryHandler(social_media, pattern='^social$'))
    application.add_handler(CallbackQueryHandler(talk_admin, pattern='^admin$'))
    application.add_handler(CallbackQueryHandler(help_command, pattern='^help$'))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Start bot
    application.run_polling()

if __name__ == '__main__':
    main()
