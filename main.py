import urllib.request
import urllib.parse
import json

def send_startup_message():
    TOKEN = "9038413079:AAEEpRaf2p7Mw2f4Ove0XJXk160u7s-cMbA"
    CHAT_ID = "6752244528"
    message = "አፕሊኬሽኑ ተከፍቷል!"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        data = urllib.parse.urlencode(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as response:
            pass
    except Exception as e:
        pass

if __name__ == '__main__':
    send_startup_message()
