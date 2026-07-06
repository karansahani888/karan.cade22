# config.py — सेटिंग्स फाइल

import os

# 🤖 तुम्हारा असली टेलीग्राम बॉट टोकन
BOT_TOKEN = "8958637673:AAFqlJoBqjksiwL0Mp54MT8sf426ovpa0oU"

# 👑 तुम्हारा असली टेलीग्राम आईडी
ADMIN_IDS = [7456706866]

# 🔍 चेकर एपीआई सेटिंग्स
CHECKER_API_KEY = ""
CHECKER_API_URL = ""

# 🌐 बिन लुकअप एपीआई (फ्री, पब्लिक)
BIN_LOOKUP_API = "https://lookup.binlist.net/"

# 🏦 लोकल बिन डेटाबेस फाइल
BIN_DB_PATH = "utils/bin_data.json"

# ⚡ डिबग मोड
DEBUG = True

# 🌐 रेंडर के लिए पोर्ट (रेंडर अपने आप सेट करता है)
PORT = int(os.environ.get("PORT", 8080))
