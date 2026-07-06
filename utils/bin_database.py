# utils/bin_database.py
import json
import os
import requests
from config import BIN_LOOKUP_API

DEFAULT_BIN_DATA = {
    "424242": {"बैंक": "Chase", "देश": "US", "प्रकार": "क्रेडिट", "लेवल": "Classic", "vbv": False},
    "400002": {"बैंक": "Bank of America", "देश": "US", "प्रकार": "डेबिट", "लेवल": "Platinum", "vbv": True},
    "401288": {"बैंक": "Visa Test", "देश": "US", "प्रकार": "क्रेडिट", "लेवल": "Classic", "vbv": False},
    "510000": {"बैंक": "Mastercard Test", "देश": "US", "प्रकार": "क्रेडिट", "लेवल": "Gold", "vbv": True},
    "371449": {"बैंक": "Amex", "देश": "US", "प्रकार": "क्रेडिट", "लेवल": "Platinum", "vbv": False},
    "601100": {"बैंक": "Discover", "देश": "US", "प्रकार": "क्रेडिट", "लेवल": "Classic", "vbv": False}
}

def load_bin_data(filepath="utils/bin_data.json"):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_BIN_DATA.copy()

def save_bin_data(data, filepath="utils/bin_data.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def lookup_bin_online(bin_number: str) -> dict:
    try:
        bin_clean = bin_number.replace(" ", "").replace("-", "")[:6]
        url = f"{BIN_LOOKUP_API}{bin_clean}"
        headers = {"Accept-Version": "3"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "बैंक": data.get("bank", {}).get("name", "अज्ञात"),
                "देश": data.get("country", {}).get("name", "अज्ञात"),
                "प्रकार": data.get("type", "अज्ञात").capitalize() if data.get("type") else "अज्ञात",
                "लेवल": data.get("brand", "अज्ञात"),
                "vbv": None,
                "source": "online"
            }
    except Exception:
        pass
    return None

def lookup_bin(bin_number: str) -> dict:
    bin_clean = bin_number.replace(" ", "").replace("-", "")[:6]
    online_data = lookup_bin_online(bin_number)
    if online_data:
        return online_data
    data = load_bin_data()
    return data.get(bin_clean, {
        "बैंक": "अज्ञात",
        "देश": "अज्ञात",
        "प्रकार": "अज्ञात",
        "लेवल": "अज्ञात",
        "vbv": None,
        "source": "local"
    })

def check_vbv_status(bin_number: str) -> str:
    bin_clean = bin_number.replace(" ", "").replace("-", "")[:6]
    info = lookup_bin_number(bin_number)
    if info.get("vbv") is True:
        return "✅ वीबीवी (3D Secure ON)"
    elif info.get("vbv") is False:
        return "❌ नॉन-वीबीवी (3D Secure OFF)"
    else:
        if bin_clean.startswith(("34", "37")):
            return "⚠️ शायद नॉन-वीबीवी (अमेक्स पैटर्न)"
        return "❓ अज्ञात (डेटाबेस में नहीं)"

def lookup_bin_number(bin_number: str) -> dict:
    return lookup_bin(bin_number)

def add_bin_data(bin_number: str, bank: str, country: str, card_type: str, level: str, vbv: bool):
    bin_clean = bin_number.replace(" ", "").replace("-", "")[:6]
    data = load_bin_data()
    data[bin_clean] = {
        "बैंक": bank,
        "देश": country,
        "प्रकार": card_type,
        "लेवल": level,
        "vbv": vbv
    }
    save_bin_data(data)
