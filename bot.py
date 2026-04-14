import requests


BOT_TOKEN = "8725076272:AAGXqwhvU5lTrGT9-wCLJsaT-Y6yuyktR84"
CHAT_ID = "1039489267"

def send_security_alert(filename, risk_level, pr_url):
    """
    Отправляет красивое уведомление в Telegram.
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
  
    text = (
        f" *KZ-CodeGuard: ОБНАРУЖЕНА УЯЗВИМОСТЬ* \n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🇰🇿 *Қауіп деңгейі:* {risk_level}\n"
        f"Файл: `{filename}`\n\n"
        f"🇷🇺 *Уровень риска:* {risk_level}\n"
        f"Файл: `{filename}`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 Агент создал Pull Request с исправлениями согласно Закону РК о ПДн и стандартам КНБ."
    )
    
 
    keyboard = {
        "inline_keyboard": [[
            {"text": "Посмотреть и одобрить PR 🔗", "url": pr_url}
        ]]
    }
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": keyboard
    }
    
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            print(" Уведомление успешно отправлено в Telegram!")
        else:
            print(f" Ошибка: {r.text}")
    except Exception as e:
        print(f" Проблема с сетью: {e}")


if __name__ == "__main__":
 
    example_url = "https://github.com/Distales/LLM_for_Bug_chek"
    send_security_alert("auth_service.py", "КРИТИЧЕСКИЙ (КНБ РК)", example_url)
