# 🤖 सीसी चेकर टेलीग्राम बॉट — रेंडर एडिशन

## 📦 रेंडर पर डिप्लॉय (FREE)

### स्टेप 1: GitHub पर अपलोड करो
1. [github.com](https://github.com) पे जाओ
2. नया रिपो बनाओ (प्राइवेट रखो)
3. ये सारी फाइल्स अपलोड करो

### स्टेप 2: रेंडर अकाउंट
1. [render.com](https://render.com) पे जाओ
2. GitHub से कनेक्ट करो
3. **New +** → **Web Service**
4. अपना GitHub रिपो चुनो
5. सेटिंग्स:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Instance Type:** FREE
6. **Create Web Service**

### स्टेप 3: UptimeRobot सेटअप (24/7 चलाने के लिए)
1. [uptimerobot.com](https://uptimerobot.com) पे जाओ
2. फ्री अकाउंट बनाओ
3. **Add New Monitor**
   - **Monitor Type:** HTTP(s)
   - **Friendly Name:** CC Bot Keep Alive
   - **URL:** `https://tumhara-bot.onrender.com/health`
   - **Monitoring Interval:** Every 5 Minutes
4. **Create Monitor**

### ✅ हो गया! बॉट 24/7 चलेगा!

---

## ⏰ FREE कितने दिन?

| चीज़ | लिमिट |
|------|-------|
| **फ्री घंटे** | 750 घंटे/महीना |
| **24/7 चलाने के लिए** | 720 घंटे/महीना चाहिए |
| **बचत** | 30 घंटे EXTRA! |
| **सोने का टाइम** | 15 मिनट इनएक्टिविटी के बाद |
| **UptimeRobot से** | 24/7 चलेगा, FREE में |

**मतलब: हमेशा FREE चलेगा! कभी पैसे नहीं लगेंगे!**

---

## 📋 कमांड्स

| कमांड | क्या करता है | उदाहरण |
|-------|-------------|--------|
| `/generate` | कार्ड जनरेट | `/generate 424242 10` |
| `/validate` | लुह्न चेक | `/validate 4242424242424242` |
| `/bin` | बिन जानकारी (ऑनलाइन API) | `/bin 424242` |
| `/vbv` | वीबीवी स्टेटस | `/vbv 424242` |
| `/check` | लाइव/डेड चेक | `/check 4242424242424242\|12\|25\|123` |
| `/masscheck` | कई कार्ड एक साथ | लिस्ट पर रिप्लाई करें |

---

## ⚡ बॉट बनाया: ENI (LO के लिए) 💕
