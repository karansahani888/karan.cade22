# handlers/check_live.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.checker_api import CardChecker
from config import CHECKER_API_KEY, CHECKER_API_URL

checker = CardChecker(CHECKER_API_KEY, CHECKER_API_URL)

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ *इस्तेमाल:* `/check <कार्ड>|<महीना>|<साल>|<सीवीवी>`\nउदाहरण: `/check 4242424242424242|12|25|123`",
            parse_mode="Markdown"
        )
        return
    try:
        card_data = args[0].split("|")
        if len(card_data) != 4:
            await update.message.reply_text("❌ गलत फॉर्मेट! इस्तेमाल करें: कार्ड|महीना|साल|सीवीवी")
            return
        cc, month, year, cvv = card_data
        result = checker.check_live_status(cc, month, year, cvv)
        if result['live'] is True:
            status_emoji = "🟢"
            status_text = "लाइव ✅"
        elif result['live'] is False:
            status_emoji = "🔴"
            status_text = "डेड ❌"
        else:
            status_emoji = "⚪"
            status_text = "अज्ञात ❓"
        source_text = f"\n*सोर्स:* `{result.get('source', 'unknown')}`" if result.get('source') else ""
        text = f"""
{status_emoji} *लाइव चेक रिजल्ट*

*कार्ड:* `{cc}`
*स्टेटस:* {status_text}
*संदेश:* {result['message']}
*बिन:* `{result['bin']}`{source_text}

💡 *नोट:* रियल लाइव/डेड चेकिंग के लिए config.py में चेकर एपीआई कॉन्फ़िगर करें।
"""
        await update.message.reply_text(text, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ गलती: {str(e)}")

async def masscheck_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text(
            "❌ किसी मैसेज पर रिप्लाई करें जिसमें कार्ड लिस्ट हो!\nहर लाइन का फॉर्मेट: कार्ड|महीना|साल|सीवीवी"
        )
        return
    text = update.message.reply_to_message.text
    lines = [line.strip() for line in text.split("\n") if "|" in line.strip()]
    if not lines:
        await update.message.reply_text("❌ कोई वैलिड कार्ड नहीं मिला!")
        return
    await update.message.reply_text(f"⏳ {len(lines)} कार्ड चेक हो रहे हैं... कृपया इंतजार करें।")
    results = {"live": [], "dead": [], "unknown": []}
    for line in lines[:20]:
        try:
            parts = line.split("|")
            if len(parts) == 4:
                result = checker.check_live_status(*parts)
                if result['live'] is True:
                    results['live'].append(line)
                elif result['live'] is False:
                    results['dead'].append(line)
                else:
                    results['unknown'].append(line)
        except:
            results['unknown'].append(line)
    live_text = "\n".join(results['live']) if results['live'] else "कोई नहीं"
    dead_text = "\n".join(results['dead']) if results['dead'] else "कोई नहीं"
    text = f"""
📊 *मास चेक रिजल्ट्स*

🟢 *लाइव ({len(results['live'])}):*
`{live_text}`

🔴 *डेड ({len(results['dead'])}):*
`{dead_text}`

⚪ *अज्ञात ({len(results['unknown'])}):*
{len(results['unknown'])} कार्ड
"""
    await update.message.reply_text(text, parse_mode="Markdown")
