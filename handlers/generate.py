# handlers/generate.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.cc_generator import generate_with_details

async def generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ *इस्तेमाल:* `/generate <बिन> [संख्या]`\nउदाहरण: `/generate 424242 10`",
            parse_mode="Markdown"
        )
        return
    bin_number = args[0]
    try:
        count = int(args[1]) if len(args) > 1 else 10
    except:
        count = 10
    count = min(count, 50)
    try:
        cards = generate_with_details(bin_number, count)
        if not cards:
            await update.message.reply_text("❌ गलत बिन फॉर्मेट!")
            return
        header = f"💳 *जनरेटेड कार्ड्स ({count})*\nबिन: `{bin_number}`\n\n"
        body = ""
        for i, card in enumerate(cards, 1):
            body += f"{i}. `{card['formatted']}`\n"
        full_text = header + body
        if len(full_text) > 4000:
            chunks = [body[i:i+3500] for i in range(0, len(body), 3500)]
            await update.message.reply_text(header + chunks[0], parse_mode="Markdown")
            for chunk in chunks[1:]:
                await update.message.reply_text(chunk, parse_mode="Markdown")
        else:
            await update.message.reply_text(full_text, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ गलती: {str(e)}")
