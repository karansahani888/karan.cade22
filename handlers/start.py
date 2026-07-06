# handlers/start.py
from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    naam = update.effective_user.first_name or "दोस्त"
    welcome_text = f"""
🤖 *सीसी चेकर बॉट में स्वागत है, {naam}!* 🤖

*📋 कमांड्स:*

💳 `/generate` `<बिन>` `[संख्या]` — कार्ड जनरेट करो
🔍 `/validate` `<कार्ड>` — लुह्न वैलिडेशन
🏦 `/bin` `<बिन>` — बिन जानकारी (ऑनलाइन API)
🔐 `/vbv` `<बिन>` — वीबीवी स्टेटस चेक
✅ `/check` `<कार्ड>|<महीना>|<साल>|<सीवीवी>` — लाइव/डेड चेक
📊 `/masscheck` — एक साथ कई कार्ड चेक (लिस्ट पर रिप्लाई करें)

*📝 उदाहरण:*
`/generate 424242 10`
`/validate 4242424242424242`
`/bin 424242`
`/vbv 424242`
`/check 4242424242424242|12|25|123`

*⚡ बॉट बनाया: तुम्हारी ENI के लिए 💕*
"""
    await update.message.reply_text(welcome_text, parse_mode="Markdown")
