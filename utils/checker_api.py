# utils/checker_api.py
import requests
from config import CHECKER_API_KEY, CHECKER_API_URL

class CardChecker:
    def __init__(self, api_key: str = "", api_url: str = ""):
        self.api_key = api_key or CHECKER_API_KEY
        self.api_url = api_url or CHECKER_API_URL

    def check_live_status(self, cc: str, month: str, year: str, cvv: str) -> dict:
        if self.api_url and self.api_key:
            try:
                payload = {
                    "card": cc,
                    "month": month,
                    "year": year,
                    "cvv": cvv,
                    "key": self.api_key
                }
                response = requests.post(self.api_url, json=payload, timeout=30)
                if response.status_code == 200:
                    api_result = response.json()
                    return {
                        "status": api_result.get("status", "unknown"),
                        "message": api_result.get("message", "API से जवाब मिला"),
                        "cc": cc,
                        "live": api_result.get("live"),
                        "bin": cc[:6],
                        "source": "custom_api"
                    }
            except Exception:
                pass

        try:
            from utils.luhn_validator import validate_luhn
            known_dead_bins = ["000000", "111111", "999999"]
            if cc[:6] in known_dead_bins:
                return {
                    "status": "dead",
                    "message": "❌ डेड कार्ड (ज्ञात इनवैलिड बिन)",
                    "cc": cc,
                    "live": False,
                    "bin": cc[:6],
                    "source": "heuristic"
                }

            if not validate_luhn(cc):
                return {
                    "status": "dead",
                    "message": "❌ डेड कार्ड (लुह्न इनवैलिड)",
                    "cc": cc,
                    "live": False,
                    "bin": cc[:6],
                    "source": "luhn_check"
                }

            return {
                "status": "unknown",
                "message": "⚠️ लुह्न वैलिड है लेकिन रियल चेकर एपीआई कॉन्फ़िगर नहीं है। config.py में CHECKER_API_KEY और CHECKER_API_URL डालें।",
                "cc": cc,
                "live": None,
                "bin": cc[:6],
                "source": "luhn_only"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ चेकिंग में गलती: {str(e)}",
                "cc": cc,
                "live": None,
                "bin": cc[:6],
                "source": "error"
            }

    def mass_check(self, cards: list) -> list:
        results = []
        for card in cards:
            result = self.check_live_status(
                card["cc"], 
                card["month"], 
                card["year"], 
                card["cvv"]
            )
            results.append(result)
        return results

    def check_bin_only(self, bin_number: str) -> dict:
        from utils.bin_database import lookup_bin
        return lookup_bin(bin_number)
