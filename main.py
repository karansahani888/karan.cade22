# main.py — रेंडर के लिए तैयार (हैल्थ एंडपॉइंट + कीप-अलाइव)
import logging
import os
import threading
import time
from flask import Flask
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN, PORT
from handlers.start import start_command
from handlers.generate import generate_command
from handlers.bin_lookup import bin_command, vbv_command
from handlers.validate import validate_command
from handlers.check_live import check_command, masscheck_command

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🌐 फ्लास्क ऐप (रेंडर के लिए वेब सर्वर)
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "🤖 CC Checker Bot is Running!"

@flask_app.route("/health")
def health():
    return {"status": "ok", "bot": "running"}

def run_flask():
    flask_app.run(host="0.0.0.0", port=PORT)

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("generate", generate_command))
    application.add_handler(CommandHandler("bin", bin_command))
    application.add_handler(CommandHandler("vbv", vbv_command))
    application.add_handler(CommandHandler("validate", validate_command))
    application.add_handler(CommandHandler("check", check_command))
    application.add_handler(CommandHandler("masscheck", masscheck_command))

    logger.info("🤖 बॉट चल रहा है...")
    application.run_polling()

if __name__ == "__main__":
    # फ्लास्क सर्वर अलग थ्रेड में चलाओ (रेंडर के लिए जरूरी)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # बॉट मेन थ्रेड में चलाओ
    run_bot()
