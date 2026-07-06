# handlers/bin_lookup.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.bin_database import lookup_bin, check_vbv_status

async def bin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ *इस्तेमाल:* `/bin <बिन>`\nउदाहरण: `/bin 424242`",
            parse_mode="Markdown"
        )
        return
    bin_number = args[0].replace(" ", "").replace("-", "")[:6]
    info = lookup_bin(bin_number)
    source = info.get("source", "local")
    source_text = "🌐 ऑनलाइन" if source == "online" else "💾 लोकल"
    text = f"""
🏦 *बिन जानकारी* ({source_text})

*बिन:* `{bin_number}`
*बैंक:* {info['बैंक']}
*देश:* {info['देश']}
*प्रकार:* {info['प्रकार']}
*लेवल:* {info['लेवल']}

💡 वीबीवी चेक: `/vbv {bin_number}`
"""
    await update.message.reply_text(text, parse_mode="Markdown")

async def vbv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ *इस्तेमाल:* `/vbv <बिन>`\nउदाहरण: `/vbv 424242`",
            parse_mode="Markdown"
        )
        return
    bin_number = args[0]
    status = check_vbv_status(bin_number)
    text = f"""
🔐 *वीबीवी स्टेटस चेक*

*बिन:* `{bin_number}`
*स्टेटस:* {status}

_नोट: यह डेटाबेस/ह्यूरिस्टिक आधारित है। 100% सटीक नहीं हो सकता।_
"""
    await update.message.reply_text(text, parse_mode="Markdown")
