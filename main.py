from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import requests

class TelegramBotApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = Label(text="ለቴሌግራም ቦት መልእክት ለመላክ ከታች ያለውን ይጫኑ", font_size=18)
        layout.add_widget(self.label)
        
        self.btn = Button(text='መልእክት ላክ (Send Message)', size_hint=(1, 0.3), font_size=18)
        self.btn.bind(on_press=self.send_telegram_message)
        layout.add_widget(self.btn)
        
        return layout

    def send_telegram_message(self, instance):
        # የቦትዎን ቶከን (Token) እና የቻት መታወቂያ (Chat ID) እዚህ ያስገቡ
        TOKEN = "YOUR_BOT_TOKEN_HERE"
        CHAT_ID = "YOUR_CHAT_ID_HERE"
        message = "ሰላም! ይህ ከአንድሮይድ አፕሊኬሽን የተላከ መልእክት ነው።"
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.label.text = "መልእክቱ በተሳካ ሁኔታ ተልኳል!"
            else:
                self.label.text = "መልእክቱን መላክ አልተቻለም።"
        except Exception as e:
            self.label.text = f"ስህተት አጋጥሟል: {str(e)}"

if __name__ == '__main__':
    TelegramBotApp().run()
