# utils/luhn_validator.py
import re

def validate_luhn(card_number: str) -> bool:
    card = card_number.replace(" ", "").replace("-", "")
    if not card.isdigit() or len(card) < 13:
        return False
    kul = 0
    ulte_ank = card[::-1]
    for i, ank in enumerate(ulte_ank):
        n = int(ank)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        kul += n
    return kul % 10 == 0

def get_card_brand(card_number: str) -> str:
    card = card_number.replace(" ", "").replace("-", "")
    pattern = {
        "वीज़ा": r"^4",
        "मास्टरकार्ड": r"^5[1-5]|^2[2-7]",
        "अमेक्स": r"^3[47]",
        "डिस्कवर": r"^6(?:011|5)",
        "जेसीबी": r"^35",
        "डाइनर्स": r"^3(?:0[0-5]|[68])"
    }
    for brand, pattern_re in pattern.items():
        if re.match(pattern_re, card):
            return brand
    return "अज्ञात"

def get_card_type(card_number: str) -> str:
    card = card_number.replace(" ", "").replace("-", "")
    if len(card) == 15:
        return "अमेक्स (क्रेडिट)"
    elif card.startswith("4"):
        return "क्रेडिट/डेबिट"
    elif card.startswith("5"):
        return "क्रेडिट/डेबिट"
    return "अज्ञात"
