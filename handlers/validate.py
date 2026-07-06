# handlers/validate.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.luhn_validator import validate_luhn, get_card_brand, get_card_type

async def validate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ *इस्तेमाल:* `/validate <कार्ड नंबर>`\nउदाहरण: `/validate 4242424242424242`",
            parse_mode="Markdown"
        )
        return
    cc = args[0].replace(" ", "").replace("-", "")
    is_valid = validate_luhn(cc)
    brand = get_card_brand(cc)
    card_type = get_card_type(cc)
    status = "✅ वैलिड" if is_valid else "❌ इनवैलिड"
    text = f"""
🔍 *लुह्न वैलिडेशन*

*कार्ड:* `{cc}`
*ब्रांड:* {brand}
*प्रकार:* {card_type}
*स्टेटस:* {status}
*लंबाई:* {len(cc)} अंक
"""
    await update.message.reply_text(text, parse_mode="Markdown")
