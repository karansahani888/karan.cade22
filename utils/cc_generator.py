# utils/cc_generator.py — कार्ड जनरेटर
import random
from datetime import datetime

def generate_from_bin(bin_number: str, count: int = 10) -> list:
    cards = []
    bin_clean = bin_number.replace(" ", "").replace("-", "")
    if len(bin_clean) < 6:
        return []
    for _ in range(count):
        bachi_lambai = 15 - len(bin_clean)
        if bachi_lambai < 0:
            continue
        core = bin_clean + ''.join([str(random.randint(0, 9)) for _ in range(bachi_lambai)])
        check_digit = calculate_luhn_check_digit(core)
        poora_card = core + str(check_digit)
        cards.append(poora_card)
    return cards

def calculate_luhn_check_digit(pan: str) -> int:
    kul = 0
    ulte_ank = pan[::-1]
    for i, ank in enumerate(ulte_ank):
        n = int(ank)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        kul += n
    return (10 - (kul % 10)) % 10

def generate_with_details(bin_number: str, count: int = 10) -> list:
    vartman_sal = datetime.now().year
    cards = []
    generated = generate_from_bin(bin_number, count)
    for cc in generated:
        cvv = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        mahina = str(random.randint(1, 12)).zfill(2)
        sal = str(random.randint(vartman_sal + 1, vartman_sal + 5))[-2:]
        cards.append({
            "cc": cc,
            "cvv": cvv,
            "month": mahina,
            "year": sal,
            "formatted": f"{cc}|{mahina}|{sal}|{cvv}"
        })
    return cards
