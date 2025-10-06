import logging
import pickle
import os
from pathlib import Path
from telebot import TeleBot, types

# ✅ Render.com compatible configuration
BOT_TOKEN = os.environ.get('BOT_TOKEN', "8483748301:AAEtNbx1_VKD5UqS6FzPhkzjkWrev1Sz66o")
OWNER_ID = int(os.environ.get('OWNER_ID', '1455752446'))

# ✅ Proper file paths for Render
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

USER_DATA_FILE = DATA_DIR / "user_data.pkl"
AGE_VERIFICATION_FILE = DATA_DIR / "age_verified_users.pkl"

# Bot initialize karein
bot = TeleBot(BOT_TOKEN)

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# VIP channels categories with detailed descriptions and pricing
VIP_CATEGORIES = {
    'apps': {
        'name': '📱 Premium/Mod Android Apps (2)',
        'channels': [
            ["VIP1: Premium Android Apps 📱", "channel1"],
            ["VIP2: Adult Android Apps 🔞", "channel2"]
        ]
    },
    'movies': {
        'name': '🎬 Movies & Webseries (4)',
        'channels': [
            ["VIP3: Hindi Movies 🎬", "channel3"],
            ["VIP4: Hindi OTT Webseries 📽️", "channel4"],
            ["VIP5: Exclusive Adult Movies 🔞", "channel5"],
            ["VIP6: Desi Adult Webseries 🔞", "channel6"]
        ]
    },
    'desi': {
        'name': '🔞 Exclusive Desi Contents (18+ Only) (13)',
        'channels': [
            ["VIP7: Tango/Stripchat/Chamet Videos 🔞", "channel7"],
            ["VIP8: Actress/Models Paid Contents 🔞", "channel8"],
            ["VIP9: Latest Desi Leaked Videos 🔞", "channel9"],
            ["VIP10: 121 Paid VC Videos 🔞", "channel10"],
            ["VIP11: My X/GF Private Leaks 🔞", "channel11"],
            ["VIP12: Hidden/Spy/CCTV Videos 🔞", "channel12"],
            ["VIP13: Desi Outdoor caught Couples 🔞", "channel13"],
            ["VIP14: Homemade/Selfmade Videos 🔞", "channel14"],
            ["VIP15: Latest Desi Album 🔞", "channel15"],
            ["VIP16: 1000+ Desi Album Collection 🔞", "channel16"],
            ["VIP17: Desi Viral Videos Collection 🔞", "channel17"],
            ["VIP18: Big Boobs Wale Videos 🔞", "channel18"],
            ["VIP19: Desi Hardcore Videos 🔞", "channel19"]
        ]
    },
    'admin': {
        'name': '⭐ Fileprovider Official Exclusive (1)',
        'channels': [
            ["VIP20: FP Exclusive Contents ⭐ ", "channel20"]
        ]
    }
}

# Channel details with descriptions and pricing
CHANNEL_DETAILS = {
    'channel1': {
        'name': 'VIP1: Premium Android Apps 📱',
        'price': '₹299/lifetime',
        'description': 'Here you\'ll get <b>Premium, Paid, Modded & Cracked Android Apps —</b> all in one place!\n\nWe work with trusted <b>developers</b> who expertly remove ads, unlock premium features, and enhance your app experience.\n\nWant any specific app in <b>premium or ad-free version?</b> Just <b>contact us directly —</b> we\'ll try to provide it ASAP!.',
        'content': '• Premium & Paid Android Apps\n• Modded & Cracked Versions\n• Ad-Free & Unlocked APKs\n• Developer-Customized Builds\n• Direct App Request Support',
        'updates': 'Regular',
        'access': 'Instant after payment verification',
        'note': 'This channel <b>does NOT contain any 18+ (adult) apps.</b> For adult content, check out our <b>2nd VIP Channel</b> (exclusive for 18+ apps)',
        'category': 'apps'
    },
    'channel2': {
        'name': 'VIP2: Adult Android Apps 🔞',
        'price': '₹299/lifetime',
        'description': 'While our <b>1st channel</b> is for <b>non-adult Android apps,</b> this <b>2nd VIP Channel</b> is dedicated <b>exclusively to 18+ Adult Category Android Apps.</b>\n\nHere you\'ll get <b>Premium / Subscribed Desi OTT Apps</b> like: Ullu, Jugnu, MoodX, ALTT, Cinema, Bindastimes, Jeel, CineOn, Atrangi, Hungama Gold, CineTV, Maza Entertainment, Kahani Play, Hichki Prime, Funters Pro, Hulchul, Waah Play — and many more! (Too many to list 😎)\n\nIf you\'re looking for <b>Adult Paid Android Apps absolutely FREE,</b> this is the <b>perfect channel for you!</b>\n\nJust pay one-time membership, and get lifetime updates with no extra cost ever!',
        'content': '• Premium Desi OTT Apps\n• Adult Category Android Apps\n• Modded & Unlocked APKs\n• Lifetime Free Updates\n• One-Time VIP Membership',
        'updates': 'Weekly',
        'access': 'Instant after payment verification',
        'note': 'Join now and unlock the ultimate 18+ entertainment world!',
        'category': 'apps'
    },
    'channel3': {
        'name': 'VIP3: Hindi Movies 🎬',
        'price': '₹399/lifetime',
        'description': 'This is our <b>3rd VIP Channel</b>, dedicated to the <b>latest Bollywood, South Indian, and Hollywood movies</b> — all in one place!\n\n<b>South Indian & Hollywood movies</b> are provided in <b>multi-audio formats</b> for your convenience — so you can enjoy them in your favorite language.\n\nAlong with <b>new releases</b>, we also upload <b>superhit movie collections</b> from past years — making this the ultimate hub for movie lovers!\n\nTill now, <b>thousands of movies</b> have already been uploaded and are <b>instantly accessible</b> once you become a member.\n\n<b>All movies are available in streaming format</b> — no downloads, no hassle, just play and enjoy!',
        'content': '• Latest Bollywood, South & Hollywood Movies\n• Multi-Audio & Dubbed Versions\n• HD Streaming Access (No Download Needed)\n• Old Hit Collections Added Regularly\n• Regular New Releases',
        'updates': 'Daily (2-3 movies)',
        'access': 'Instant after payment verification',
        'note': 'This channel <b>does NOT include any adult movies or web series</b>. For that, check out our <b>dedicated adult channels</b> 🔞 available separately.',
        'category': 'movies'
    },
    'channel4': {
        'name': 'VIP4: Hindi OTT Webseries 📽️',
        'price': '₹499/lifetime',
        'description': 'All Your Favorite OTT Web Series in One Place. This is our <b>4th VIP Channel</b>, dedicated completely to <b>Premium Web Series</b> from the world\'s top OTT platforms — including <b>Netflix, Amazon Prime, ZEE5, SonyLIV</b>, and many more!\n\nEnjoy <b>HD-quality web series</b> from every genre — action, drama, thriller, romance, and more — all available in <b>instant streaming format.</b>\n\nAlready <b>1500+ web series uploaded</b> and new releases are <b>added regularly</b> — so you\'ll never run out of fresh content to watch!\n\nIf you\'re a true <b>web series lover</b>, this channel is an <b>absolute must-have</b> for your entertainment list!',
        'content': '• Premium Web Series from Top OTTs\n• Netflix, Prime Video, ZEE5, SonyLIV & More\n• HD Streaming (No Download Needed)\n• 1500+ Series Already Uploaded\n• Regular Updates with New Releases',
        'updates': 'Daily (1-2 series)',
        'access': 'Instant after payment verification',
        'note': 'This channel <b>does NOT include Desi Adult or Uncensored Web Series</b>. For that, check out our <b>separate dedicated adult channel</b> 🔞.',
        'category': 'movies'
    },
    'channel5': {
        'name': 'VIP5: Exclusive Adult Movies 🔞',
        'price': '₹299/lifetime',
        'description': ' <b>World\'s Hottest Adult Movies – All in One Channel</b>\n\n🔞 This is the <b>5th VIP Channel</b> of the <b>Fileprovider Official Network</b>, featuring a massive collection of <b>Adult / Uncensored Movies</b> from around the world 🌍.\n\n✅ <b>Thousands of movies</b> are already uploaded — and new ones are added <b>regularly</b> to keep your collection fresh!\n✅ Watch in <b>multiple languages</b> including <b>Hindi, English, Chinese, Korean</b>, and many more 🎧.\n✅ All movies are available in <b>HD streaming format</b> for smooth and easy viewing — no downloads needed!',
        'content': '• Worldwide Adult & Uncensored Movies\n• Multi-Language Streaming (Hindi, English & More)\n• Multiple Categories\n• HD Quality with Fast Access\n• Regularly Updated Collection',
        'updates': 'Regular',
        'access': 'Instant after payment verification',
        'note': 'If you\'re looking for a <b>global collection of adult movies</b> in one secure and premium place, this channel is the <b>perfect choice</b> for you!',
        'category': 'movies'
    },
    'channel6': {
        'name': 'VIP6: Desi Adult Webseries 🔞',
        'price': '₹499/lifetime',
        'description': '🔞 This is the <b>6th VIP Channel</b> of the <b>Fileprovider Official Network</b> — and also the <b>first channel in our Desi Adult Category Series</b>.\nFrom here onwards, all VIP channels in this section are dedicated exclusively to <b>Desi Adult & Uncensored Content</b>.\n\n🎬 In this channel, you\'ll get access to <b>18+ & Uncensored Web Series</b> from top <b>Desi OTT platforms</b> such as <b>Ullu, Jugnu, MoodX, ALTT, Cinema, BindasTimes, Jeel, CineOn, Atrangi, Hungama Gold, CineTV, Maza Entertainment, Kahani Play, Hichki Prime, Funters Pro, Hulchul, Waah Play</b>, and many more!\n\n✅ <b>Over 2000+ episodes</b> are already uploaded — and new releases are added <b>regularly</b> so you never miss the latest updates!',
        'content': '• Desi 18+ & Uncensored Web Series\n• Premium OTT Platforms Access\n• HD Streaming Format – No Downloads Needed\n• 2000+ Episodes Uploaded Already\n• Regular Updates with New Releases',
        'updates': 'Daily',
        'access': 'Instant after payment verification',
        'note': 'If you\'re a fan of <b>Desi Uncensored Web Series</b>, then this channel is a <b>must-have membership</b> for you.\n💥 <b>Join now and explore the hottest Desi web series collection – exclusively available here!</b>',
        'category': 'movies'
    },
    'channel7': {
        'name': 'VIP7: Tango/Stripchat/Chamet Videos 🔞',
        'price': '₹299/lifetime',
        'description': '🎥 <b>All Your Favorite Desi Live Shows in One Place</b>\n\n🔞 This is the <b>7th Channel</b> of the <b>Fileprovider Official Network</b> and the <b>2nd channel in our Desi Adult Category</b>.\n\nHere, you will find <b>recorded videos</b> from popular <b>live-streaming platforms</b> such as <b>Tango, Chamet, Stripchat, Charubate, Bongacam</b> and many more — featuring several <b>well-known models</b>.\n\n👉 <b>Content includes</b> solo nude shows, masturbation videos, couple live sessions, and much more.\n✅ <b>1000+ videos</b> are already uploaded, with new videos added <b>regularly</b> to keep the collection fresh.',
        'content': '• Desi Live Show Recordings\n• Popular Platforms (Tango, Chamet, Stripchat & More)\n• Solo & Couple Live Sessions\n• 1000+ Videos Already Uploaded\n• Regularly Updated Collection',
        'updates': 'Daily (10-15 videos)',
        'access': 'Within 1 hour after payment',
        'note': 'If you enjoy <b>live-stream style Desi adult content</b>, this channel is the <b>perfect choice</b> for you!\n💥 <b>Join now and enjoy the hottest Desi live shows – all in one exclusive channel!</b>',
        'category': 'desi'
    },
    'channel8': {
        'name': 'VIP8: Actress/Models Paid Contents 🔞',
        'price': '₹499/lifetime',
        'description': 'Paid content from famous actresses and models from OnlyFans and other platforms.',
        'content': '• Actress Paid Content\n• Models Exclusive Videos\n• OnlyFans Content\n• Premium Collections\n• HD Quality',
        'updates': 'Daily',
        'access': 'Within 2 hours after payment',
        'category': 'desi'
    },
    'channel9': {
        'name': 'VIP9: Latest Desi Leaked Videos 🔞',
        'price': '₹999/lifetime',
        'description': 'Latest leaked videos from Indian social media and personal collections.',
        'content': '• Latest Leaked Videos\n• Social Media Leaks\n• Personal Collection Leaks\n• Regular Updates\n• Exclusive Content',
        'updates': 'Daily (5-10 videos)',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel10': {
        'name': 'VIP10: 121 Paid VC Videos 🔞',
        'price': '₹299/lifetime',
        'description': 'One-on-one video call recordings and paid private session videos.',
        'content': '• Private Video Calls\n• One-on-One Sessions\n• Exclusive Content\n• HD Quality\n• Regular New Videos',
        'updates': 'Daily',
        'access': 'Within 3 hours after payment',
        'category': 'desi'
    },
    'channel11': {
        'name': 'VIP11: My X/GF Private Leaks 🔞',
        'price': '₹299/lifetime',
        'description': 'Extremely private and personal content leaks from relationships.',
        'content': '• Personal Relationship Videos\n• Private Moments\n• Exclusive Leaks\n• HD Quality Content\n• Very Private Collection',
        'updates': 'Weekly',
        'access': 'Within 6 hours after payment verification',
        'note': 'Strict verification required',
        'category': 'desi'
    },
    'channel12': {
        'name': 'VIP12: Hidden/Spy/CCTV Videos 🔞',
        'price': '₹499/lifetime',
        'description': 'Hidden camera, spy videos and CCTV footage from various locations.',
        'content': '• Hidden Camera Videos\n• Spy Camera Footage\n• CCTV Recordings\n• Various Locations\n• Exclusive Content',
        'updates': 'Weekly',
        'access': 'Within 4 hours after payment',
        'note': 'For educational purposes only',
        'category': 'desi'
    },
    'channel13': {
        'name': 'VIP13: Desi Outdoor caught Couples 🔞',
        'price': '₹299/lifetime',
        'description': 'Indian couples caught in outdoor locations and public places.',
        'content': '• Outdoor Caught Videos\n• Public Place Recordings\n• Desi Couples Content\n• Various Locations\n• Regular Updates',
        'updates': 'Weekly (3-5 videos)',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel14': {
        'name': 'VIP14: Homemade/Selfmade Videos 🔞',
        'price': '₹299/lifetime',
        'description': 'Authentic homemade and self-recorded videos from real couples.',
        'content': '• Homemade Videos\n• Self Recorded Content\n• Real Couples\n• Authentic Experience\n• Regular New Content',
        'updates': 'Daily',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel15': {
        'name': 'VIP15: Latest Desi Album 🔞',
        'price': '₹499/lifetime',
        'description': 'Latest Indian photoshoots and album collections from various models.',
        'content': '• Latest Photo Albums\n• Model Photoshoots\n• HD Quality Photos\n• Regular New Albums\n• Multiple Models',
        'updates': 'Daily (2-3 albums)',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel16': {
        'name': 'VIP16: 1000+ Desi Album Collection 🔞',
        'price': '₹299/lifetime',
        'description': 'Massive collection of 1000+ Indian albums and photoshoots.',
        'content': '• 1000+ Albums Collection\n• Historical Archive\n• Various Models\n• HD Quality Photos\n• Complete Collections',
        'updates': 'Weekly new additions',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel17': {
        'name': 'VIP17: Desi Viral Videos Collection 🔞',
        'price': '₹499/lifetime',
        'description': 'Collection of viral Indian videos from social media platforms.',
        'content': '• Viral Video Collection\n• Social Media Trends\n• Regular New Virals\n• Various Categories\n• HD Quality',
        'updates': 'Daily (5-10 videos)',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel18': {
        'name': 'VIP18: Big Boobs Wale Videos 🔞',
        'price': '₹299/lifetime',
        'description': 'Specialized content featuring well-endowed Indian women.',
        'content': '• Specialized Category\n• Curated Collection\n• HD Quality Videos\n• Regular Updates\n• Exclusive Content',
        'updates': 'Daily',
        'access': 'Instant after payment',
        'category': 'desi'
    },
    'channel19': {
        'name': 'VIP19: Desi Hardcore Videos 🔞',
        'price': '₹399/lifetime',
        'description': 'Hardcore Indian adult content with explicit material.',
        'content': '• Hardcore Content\n• Explicit Material\n• HD Quality Videos\n• Regular New Content\n• Various Categories',
        'updates': 'Daily',
        'access': 'Within 1 hour after payment',
        'note': '18+ Only - Extreme content warning',
        'category': 'desi'
    },
    'channel20': {
        'name': 'VIP20: FP Exclusive Contents ⭐',
        'price': '₹2499/lifetime',
        'description': 'Ultimate premium package with access to all exclusive content from Fileprovider Official.',
        'content': '• All Categories Access\n• Priority Support\n• Early Access Content\n• Exclusive Releases\n• Complete Archive Access\n• Personal Assistant',
        'updates': 'Multiple daily updates',
        'access': 'Within 15 minutes after payment',
        'note': 'Premium membership with all benefits',
        'category': 'admin'
    }
}

def load_user_data():
    """User data load karein"""
    try:
        with open(USER_DATA_FILE, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return set()

def save_user_data(user_data):
    """User data save karein"""
    with open(USER_DATA_FILE, 'wb') as f:
        pickle.dump(user_data, f)

def load_age_verified_users():
    """Age verified users load karein"""
    try:
        with open(AGE_VERIFICATION_FILE, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return set()

def save_age_verified_users(verified_users):
    """Age verified users save karein"""
    with open(AGE_VERIFICATION_FILE, 'wb') as f:
        pickle.dump(verified_users, f)

def is_owner(user_id):
    """Check karein ki user owner hai ya nahi"""
    return user_id == OWNER_ID

def is_age_verified(user_id):
    """Check karein ki user age verified hai ya nahi"""
    verified_users = load_age_verified_users()
    return user_id in verified_users

def mark_age_verified(user_id):
    """User ko age verified mark karein"""
    verified_users = load_age_verified_users()
    verified_users.add(user_id)
    save_age_verified_users(verified_users)

def show_age_verification_popup(call, category='desi'):
    """Age verification popup show karein"""
    user_id = call.from_user.id
    
    text = """🔞 <b>AGE VERIFICATION REQUIRED</b> 🔞

⚠️ <b>WARNING: ADULT CONTENT AHEAD</b> ⚠️

This category contains explicit adult content that is restricted to viewers who are <b>18 years of age or older</b>.

<b>Content includes:</b>
• Explicit adult material
• Nudity and sexual content  
• Mature themes and situations

🚫 <b>Access Restrictions:</b>
• Must be 18+ years old
• Content not suitable for minors
• By proceeding, you confirm you are legally allowed to view such content

<b>Please confirm:</b>
1. I am 18 years of age or older
2. I want to view adult content willingly
3. I understand the nature of this material"""

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("✅ I AM 18+ & AGREE", callback_data=f'age_verify_yes_{category}'),
        types.InlineKeyboardButton("❌ CANCEL & EXIT", callback_data='age_verify_no')
    ]
    for button in buttons:
        keyboard.add(button)
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

# Command handlers
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name or "User"
    
    # User data mein save karein
    user_data = load_user_data()
    user_data.add(user_id)
    save_user_data(user_data)
    
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    buttons = [
        types.InlineKeyboardButton("ℹ️ About Us", callback_data='about'),
        types.InlineKeyboardButton("💎 VIP Channels", callback_data='vip_categories'),
        types.InlineKeyboardButton("💳 Payment Methods", callback_data='payment'),
        types.InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof'),
        types.InlineKeyboardButton("📱 Social Media Links", callback_data='social'),
        types.InlineKeyboardButton("👨‍💼 Talk with Admin", callback_data='admin'),
        types.InlineKeyboardButton("❓ Help", callback_data='help')
    ]
    
    # Agar owner hai toh admin panel button add karein
    if is_owner(user_id):
        buttons.append(types.InlineKeyboardButton("👑 Admin Panel", callback_data='admin_panel'))
    
    for button in buttons:
        keyboard.add(button)
    
    welcome_text = f"""
Hello {user_first_name}! 👋

<b>🤖 Welcome to Fileprovider Official Network VIP Service Bot!</b>

Choose an option from the menu below to get started."""
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['vipchannels', 'vip'])
def vip_channels_command(message):
    """VIP Channels command handler"""
    show_vip_categories_command(message)

@bot.message_handler(commands=['adminpanel', 'adminpannel'])
def admin_panel_command(message):
    """Admin Panel command handler"""
    user_id = message.from_user.id
    
    if not is_owner(user_id):
        bot.send_message(message.chat.id, "❌ Unauthorized access! This command is for admin only.")
        return
    
    text = """<b>👑 Admin Panel</b>

Welcome to admin panel! Select an option:"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("📊 User Statistics", callback_data='user_stats'),
        types.InlineKeyboardButton("📢 Broadcast Message", callback_data='broadcast'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    ]
    for button in buttons:
        keyboard.add(button)
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['aboutus', 'about'])
def about_us_command(message):
    """About Us command handler"""
    text = """<b>🏢 About Fileprovider Official</b>

Fileprovider Official is an exclusive Telegram network offering access to 20+ premium private channels across multiple categories. With 90% adult content, members enjoy rare and high-quality material that's nearly impossible to find elsewhere.

<b>📂 VIP Categories:</b>
• 📱 Apps & Premium Software
• 🎬 Movies & Webseries  
• 🔞 Desi Exclusive Adult Categories
• 👮 FP Exclusive Collection

<b>✅ Benefits:</b>
• One-time membership, lifetime access
• Regular updates on every channel
• Exclusive & rare Desi adult content
• Direct Telegram files – no fake links, no clickbait
• Smooth streaming experience

<b>🔥 Join Fileprovider Official Network today and unlock the most exclusive and premium content library on Telegram!</b>"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help_command(message):
    """Help command handler"""
    text = """<b>❓ Help Center</b>

<b>Common Issues:</b>

🔹 <b>Payment not verified?</b>
Wait 24 hours, then contact admin

🔹 <b>Can't access channel?</b>
Check if subscription is active

🔹 <b>Payment method not working?</b>
Try alternative method

For immediate assistance, contact @FPOfficialAdminBot"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    )
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['contactus', 'contact', 'admincontact'])
def contact_us_command(message):
    """Contact Us command handler"""
    text = """<b>👨‍💼 Talk with Admin</b>

You can contact our admin directly:

<b>📧 Email:</b> fileprovider.official@gmail.com
<b>👤 Telegram:</b> @FPOfficialAdminBot

<b>Office Hours:</b>
Monday-Friday: 9AM-6PM
Saturday: 10AM-2PM

We typically respond within 2-4 hours."""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['payment', 'payments'])
def payment_command(message):
    """Payment Methods command handler"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("UPI 1", callback_data='upi1'),
        types.InlineKeyboardButton("UPI 2", callback_data='upi2'),
        types.InlineKeyboardButton("Crypto", callback_data='crypto'),
        types.InlineKeyboardButton("PayPal", callback_data='paypal'),
        types.InlineKeyboardButton("Others", callback_data='others'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    ]
    for button in buttons:
        keyboard.add(button)
    
    text = """<b>💳 Payment Methods</b>

Select your preferred payment method:"""
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['sendpaymentproof', 'paymentproof', 'proof'])
def payment_proof_command(message):
    """Send Payment Proof command handler"""
    text = """<b>📸 Send Payment Proof</b>

Please send your payment screenshot/receipt here.

<b>Instructions:</b>
1. Take clear screenshot of payment confirmation
2. Send it to <a href="https://t.me/FPOfficialAdminBot">Admin</a> as photo/document
3. Include your username in message
4. We'll verify within 24 hours

After verification, you'll be added to VIP channels."""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    )
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['socialmedia', 'social'])
def social_media_command(message):
    """Social Media command handler"""
    text = """<b>📱 Follow Us on Social Media</b>

Stay updated with our latest news and offers:

• <b>Facebook:</b> <a href="https://www.facebook.com/Fileproviderofficial">@FileproviderOfficial</a>
• <b>Instagram:</b> <a href="https://instagram.com/fileprovider_official">@Fileprovider_Official</a>
• <b>Telegram Channel:</b> <a href="https://t.me/Fileprovider_Official">@Fileprovider_Official</a>
• <b>Telegram Backup Channel:</b> <a href="https://t.me/FileproviderOfficial">@FileproviderOfficial</a>
• <b>Website:</b> <a href="https://telegra.ph/Fileprovider-Official-09-20">Fileprovider Official</a>

Follow us for updates and announcements!"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

# Helper function for VIP categories command
def show_vip_categories_command(message):
    """VIP categories show karein for command"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    buttons = [
        types.InlineKeyboardButton(VIP_CATEGORIES['apps']['name'], callback_data='vip_category_apps'),
        types.InlineKeyboardButton(VIP_CATEGORIES['movies']['name'], callback_data='vip_category_movies'),
        types.InlineKeyboardButton(VIP_CATEGORIES['desi']['name'], callback_data='vip_category_desi'),
        types.InlineKeyboardButton(VIP_CATEGORIES['admin']['name'], callback_data='vip_category_admin'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    ]
    
    for button in buttons:
        keyboard.add(button)
    
    text = """<b>💎 VIP Channels Categories</b>

Select a category to view available channels:"""
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    data = call.data
    
    if data == 'about':
        text = """<b>🏢 About Fileprovider Official</b>

Fileprovider Official is an exclusive Telegram network offering access to 20+ premium private channels across multiple categories. With 90% adult content, members enjoy rare and high-quality material that's nearly impossible to find elsewhere.

<b>📂 VIP Categories:</b>
• 📱 Apps & Premium Software
• 🎬 Movies & Webseries  
• 🔞 Desi Exclusive Adult Categories
• 👮 FP Exclusive Collection

<b>✅ Benefits:</b>
• One-time membership, lifetime access
• Regular updates on every channel
• Exclusive & rare Desi adult content
• Direct Telegram files – no fake links, no clickbait
• Smooth streaming experience

<b>🔥 Join Fileprovider Official Network today and unlock the most exclusive and premium content library on Telegram!</b>"""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'vip_categories':
        show_vip_categories(call)
    
    elif data.startswith('vip_category_'):
        category = data.replace('vip_category_', '')
        
        # Agar desi category hai aur user age verified nahi hai toh verification show karein
        if category == 'desi' and not is_age_verified(user_id):
            show_age_verification_popup(call, category)
        else:
            show_vip_channels(call, category)
    
    elif data.startswith('age_verify_yes_'):
        # User ne age verify kar liya
        category = data.replace('age_verify_yes_', '')
        mark_age_verified(user_id)
        
        # Success message
        success_text = """✅ <b>AGE VERIFICATION SUCCESSFUL</b>

You have been granted access to adult content categories.

⚠️ <b>Remember:</b>
• Content is for personal use only
• Do not share with minors
• Respect all content guidelines

You can now browse the adult content category."""
        bot.edit_message_text(success_text, call.message.chat.id, call.message.message_id, parse_mode='HTML')
        
        # Thoda wait karke channels show karein
        import time
        time.sleep(2)
        show_vip_channels(call, category)
    
    elif data == 'age_verify_no':
        # User ne cancel kiya
        cancel_text = """❌ <b>ACCESS DENIED</b>

You have chosen not to proceed with age verification.

Adult content categories remain restricted.

Returning to main menu..."""
        bot.edit_message_text(cancel_text, call.message.chat.id, call.message.message_id, parse_mode='HTML')
        
        # Thoda wait karke main menu show karein
        import time
        time.sleep(2)
        show_main_menu(call, user_id)
    
    elif data == 'payment':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        buttons = [
            types.InlineKeyboardButton("UPI 1", callback_data='upi1'),
            types.InlineKeyboardButton("UPI 2", callback_data='upi2'),
            types.InlineKeyboardButton("Crypto", callback_data='crypto'),
            types.InlineKeyboardButton("PayPal", callback_data='paypal'),
            types.InlineKeyboardButton("Others", callback_data='others'),
            types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
        ]
        for button in buttons:
            keyboard.add(button)
        
        text = """<b>💳 Payment Methods</b>

Select your preferred payment method:"""
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'proof':
        text = """<b>📸 Send Payment Proof</b>

Please send your payment screenshot/receipt here.

<b>Instructions:</b>
1. Take clear screenshot of payment confirmation
2. Send it to <a href="https://t.me/FPOfficialAdminBot">Admin</a> as photo/document
3. Include your username in message
4. We'll verify within 24 hours

After verification, you'll be added to VIP channels."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin'),
            types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'social':
        text = """<b>📱 Follow Us on Social Media</b>

Stay updated with our latest news and offers:

• <b>Facebook:</b> <a href="https://www.facebook.com/Fileproviderofficial">@FileproviderOfficial</a>
• <b>Instagram:</b> <a href="https://instagram.com/fileprovider_official">@Fileprovider_Official</a>
• <b>Telegram Channel:</b> <a href="https://t.me/Fileprovider_Official">@Fileprovider_Official</a>
• <b>Telegram Backup Channel:</b> <a href="https://t.me/FileproviderOfficial">@FileproviderOfficial</a>
• <b>Website:</b> <a href="https://telegra.ph/Fileprovider-Official-09-20">Fileprovider Official</a>

Follow us for updates and announcements!"""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'admin':
        text = """<b>👨‍💼 Talk with Admin</b>

You can contact our admin directly:

<b>📧 Email:</b> fileprovider.official@gmail.com
<b>👤 Telegram:</b> @FPOfficialAdminBot

<b>Office Hours:</b>
Monday-Friday: 9AM-6PM
Saturday: 10AM-2PM

We typically respond within 2-4 hours."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Main", callback_data='main'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'help':
        text = """<b>❓ Help Center</b>

<b>Common Issues:</b>

🔹 <b>Payment not verified?</b>
Wait 24 hours, then contact admin

🔹 <b>Can't access channel?</b>
Check if subscription is active

🔹 <b>Payment method not working?</b>
Try alternative method

For immediate assistance, contact @FPOfficialAdminBot"""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👨‍💼 Contact Admin", callback_data='admin'),
            types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'main':
        show_main_menu(call, user_id)
    
    elif data == 'admin_panel':
        if not is_owner(user_id):
            bot.edit_message_text("❌ Unauthorized access!", call.message.chat.id, call.message.message_id)
            return
        
        text = """<b>👑 Admin Panel</b>

Welcome to admin panel! Select an option:"""
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        buttons = [
            types.InlineKeyboardButton("📊 User Statistics", callback_data='user_stats'),
            types.InlineKeyboardButton("📢 Broadcast Message", callback_data='broadcast'),
            types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
        ]
        for button in buttons:
            keyboard.add(button)
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'user_stats':
        if not is_owner(user_id):
            bot.edit_message_text("❌ Unauthorized access!", call.message.chat.id, call.message.message_id)
            return
        
        user_data = load_user_data()
        total_users = len(user_data)
        
        # Age verified users count
        verified_users = load_age_verified_users()
        verified_count = len(verified_users)
        
        text = f"""<b>📊 User Statistics</b>

🤖 <b>Total Users:</b> {total_users}
🔞 <b>Age Verified Users:</b> {verified_count}
📅 <b>Bot Status:</b> Running
🆔 <b>Your ID:</b> {user_id}

<i>Last updated: Just now</i>"""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("🔄 Refresh Stats", callback_data='user_stats'),
            types.InlineKeyboardButton("🔙 Back to Admin Panel", callback_data='admin_panel')
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'broadcast':
        if not is_owner(user_id):
            bot.edit_message_text("❌ Unauthorized access!", call.message.chat.id, call.message.message_id)
            return
        
        # Broadcast message ke liye prompt send karein
        msg = bot.send_message(call.message.chat.id, 
                              "<b>📢 Broadcast Message</b>\n\nPlease send the message you want to broadcast to all users.\n\nType /cancel to cancel.", 
                              parse_mode='HTML')
        
        # Next message wait karein
        bot.register_next_step_handler(msg, process_broadcast_message)
    
    elif data.startswith('channel'):
        show_channel_details(call, data)
    
    elif data == 'upi1':
        text = """<b>📱 UPI 1 Payment</b>

<b>UPI ID:</b> example1@upi
<b>Name:</b> Your Name
<b>Amount:</b> As per package

After payment, send screenshot to admin."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Payment Methods", callback_data='payment'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'upi2':
        text = """<b>📱 UPI 2 Payment</b>

<b>UPI ID:</b> example2@upi
<b>Name:</b> Your Name
<b>Amount:</b> As per package

After payment, send screenshot to admin."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Payment Methods", callback_data='payment'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'crypto':
        text = """<b>₿ Crypto Payment</b>

We accept:
• Bitcoin (BTC)
• Ethereum (ETH)
• USDT (TRC20/ERC20)

<b>Contact admin for wallet address</b>

After payment, send transaction hash to admin."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Payment Methods", callback_data='payment'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'paypal':
        text = """<b>💸 PayPal Payment</b>

<b>PayPal Email:</b> example@paypal.com
<b>Amount:</b> As per package

After payment, send screenshot to admin."""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Payment Methods", callback_data='payment'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    
    elif data == 'others':
        text = """<b>💳 Other Payment Methods</b>

We also accept:
• Bank Transfer
• Credit/Debit Cards
• Google Pay
• PhonePe
• Amazon Pay

<b>Contact admin for details</b>"""
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("🔙 Back to Payment Methods", callback_data='payment'))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

def show_main_menu(call, user_id):
    """Main menu show karein"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    buttons = [
        types.InlineKeyboardButton("ℹ️ About Us", callback_data='about'),
        types.InlineKeyboardButton("💎 VIP Channels", callback_data='vip_categories'),
        types.InlineKeyboardButton("💳 Payment Methods", callback_data='payment'),
        types.InlineKeyboardButton("📸 Send Payment Proof", callback_data='proof'),
        types.InlineKeyboardButton("📱 Social Media Links", callback_data='social'),
        types.InlineKeyboardButton("👨‍💼 Talk with Admin", callback_data='admin'),
        types.InlineKeyboardButton("❓ Help", callback_data='help')
    ]
    
    if is_owner(user_id):
        buttons.append(types.InlineKeyboardButton("👑 Admin Panel", callback_data='admin_panel'))
    
    for button in buttons:
        keyboard.add(button)
    
    welcome_text = f"""
Hello {call.from_user.first_name or 'User'}! 👋

<b>🤖 Welcome to Fileprovider Official Network VIP Service Bot!</b>

Choose an option from the menu below to get started."""
    bot.edit_message_text(welcome_text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

def show_vip_categories(call):
    """VIP categories show karein"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    buttons = [
        types.InlineKeyboardButton(VIP_CATEGORIES['apps']['name'], callback_data='vip_category_apps'),
        types.InlineKeyboardButton(VIP_CATEGORIES['movies']['name'], callback_data='vip_category_movies'),
        types.InlineKeyboardButton(VIP_CATEGORIES['desi']['name'], callback_data='vip_category_desi'),
        types.InlineKeyboardButton(VIP_CATEGORIES['admin']['name'], callback_data='vip_category_admin'),
        types.InlineKeyboardButton("🔙 Back to Main", callback_data='main')
    ]
    
    for button in buttons:
        keyboard.add(button)
    
    text = """<b>💎 VIP Channels Categories</b>

Select a category to view available channels:"""
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

def show_vip_channels(call, category):
    """VIP channels show karein specific category ke liye"""
    if category not in VIP_CATEGORIES:
        bot.edit_message_text("❌ Category not found!", call.message.chat.id, call.message.message_id)
        return
    
    category_data = VIP_CATEGORIES[category]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    # Category ke channels ke buttons add karein
    for channel in category_data['channels']:
        keyboard.add(types.InlineKeyboardButton(channel[0], callback_data=channel[1]))
    
    # Back button add karein
    keyboard.add(types.InlineKeyboardButton("🔙 Back to Categories", callback_data='vip_categories'))
    
    text = f"""<b>{category_data['name']}</b>

Select a channel to view details and pricing:"""
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

def show_channel_details(call, channel_id):
    """Channel details show karein"""
    if channel_id not in CHANNEL_DETAILS:
        bot.edit_message_text("❌ Channel not found!", call.message.chat.id, call.message.message_id)
        return
    
    channel = CHANNEL_DETAILS[channel_id]
    
    text = f"""<b>{channel['name']}</b>

💰 <b>Price:</b> {channel['price']}

📝 <b>Description:</b>
{channel['description']}

📂 <b>Content Includes:</b>
{channel['content']}

🔄 <b>Updates:</b> {channel['updates']}
⚡ <b>Access:</b> {channel['access']}"""

    # Agar note hai toh add karein
    if 'note' in channel:
        text += f"\n\n⚠️ <b>Note:</b> {channel['note']}"

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("💳 Buy Now", callback_data='payment'),
        types.InlineKeyboardButton("🔙 Back to Category", callback_data=f"vip_category_{channel['category']}")
    )
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

def process_broadcast_message(message):
    """Broadcast message process karein"""
    if message.text == '/cancel':
        bot.send_message(message.chat.id, "❌ Broadcast cancelled.")
        return
    
    user_data = load_user_data()
    success_count = 0
    fail_count = 0
    
    # Progress message send karein
    progress_msg = bot.send_message(message.chat.id, f"📢 Broadcasting to {len(user_data)} users...\n\n0/{len(user_data)} sent")
    
    for user_id in user_data:
        try:
            bot.send_message(user_id, message.text, parse_mode='HTML')
            success_count += 1
        except Exception as e:
            fail_count += 1
            logger.error(f"Failed to send to {user_id}: {e}")
        
        # Progress update karein every 10 users
        if success_count % 10 == 0:
            try:
                bot.edit_message_text(
                    f"📢 Broadcasting to {len(user_data)} users...\n\n{success_count}/{len(user_data)} sent\n✅ Success: {success_count}\n❌ Failed: {fail_count}",
                    progress_msg.chat.id,
                    progress_msg.message_id
                )
            except:
                pass
    
    # Final result show karein
    bot.edit_message_text(
        f"✅ <b>Broadcast Completed!</b>\n\n📊 <b>Results:</b>\n✅ Success: {success_count}\n❌ Failed: {fail_count}\n📱 Total Users: {len(user_data)}",
        progress_msg.chat.id,
        progress_msg.message_id,
        parse_mode='HTML'
    )

if __name__ == "__main__":
    print("🤖 Bot is running on Render...")
    logger.info("Starting bot with infinity polling...")
    bot.infinity_polling()