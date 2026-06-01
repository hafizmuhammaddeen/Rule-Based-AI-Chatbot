import time
import random
from datetime import datetime

# ANSI Color Codes for Professional Terminal Look
G = "\033[92m"  # Green (Bot)
B = "\033[94m"  # Blue (User)
Y = "\033[93m"  # Yellow (System)
R = "\033[91m"  # Red
W = "\033[0m"   # Reset

class DecodeLabsProBot:
    def __init__(self):
        # Expanded Knowledge Base using PDF Info (Page 21)
        self.knowledge_base = {
            "greeting": {
                "keywords": ["hi", "hello", "hey", "salam", "salaam", "slm", "greetings"],
                "responses": ["Walaykum Assalam! How can I assist you today?", "Hello! DecodeLabs Assistant at your service.", "Hey there! Ready to explore AI?"]
            },
            "status": {
                "keywords": ["how are you", "hru", "how is it going", "sab theek"],
                "responses": ["I'm functioning at 100% efficiency, thank you!", "I am online and ready to process your queries."]
            },
            "contact": {
                "keywords": ["contact", "email", "phone", "number", "address", "location"],
                "responses": [
                    f"📍 Location: Greater Lucknow, India\n   📞 Phone: +91 89330 06408\n   📧 Email: decodelabs.tech@gmail.com"
                ]
            },
            "ai_logic": {
                "keywords": ["ai", "artificial intelligence", "what is ai", "machine learning"],
                "responses": ["AI is the simulation of human intelligence. In Project 1, we use Rule-Based Deterministic logic."]
            },
            "internship": {
                "keywords": ["internship", "project", "batch", "2026", "decode"],
                "responses": ["You are part of the Batch 2026. Project 1 is your foundation in Control Flow and Logic."]
            },
            "thanks": {
                "keywords": ["thanks", "thank you", "shukriya", "jazakallah"],
                "responses": ["You're welcome! Always here to help.", "No problem! Let me know if you need anything else."]
            }
        }
        self.is_running = True

    def header(self):
        print(f"{Y}" + "="*60)
        print("""
     ____                      _      _         _         
    |  _ \  ___  ___ ___   __| | ___| |    __ _| |__  ___ 
    | | | |/ _ \/ __/ _ \ / _` |/ _ \ |   / _` | '_ \/ __|
    | |_| |  __/ (_| (_) | (_| |  __/ |__| (_| | |_) \__ \\
    |____/ \___|\___\___/ \__,_|\___|_____\__,_|_.__/|___/
                INDUSTRIAL AI ENGINE - v2.0
        """)
        print("="*60 + f"{W}")

    def typing_effect(self, text):
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"{G}[{timestamp}] BOT:{W} ", end="", flush=True)
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.015)
        print()

    def get_response(self, user_input):
        clean_input = user_input.lower().strip()

        if clean_input in ["exit", "bye", "quit", "terminate"]:
            self.is_running = False
            return "Session terminated. Goodbye!"

        # Advanced Matching
        for intent, data in self.knowledge_base.items():
            if any(key in clean_input for key in data["keywords"]):
                return random.choice(data["responses"])

        return "I'm sorry, that's outside my current rule-set. Try asking about 'Contact', 'AI', or 'Internship'."

    def start(self):
        self.header()
        user_name = input(f"{Y}ENTER YOUR NAME TO INITIALIZE:{W} ").upper() or "INTERN"
        self.typing_effect(f"System Check... OK. Welcome, {user_name}.")
        
        while self.is_running:
            try:
                user_msg = input(f"\n{B}{user_name}:{W} ")
                if not user_msg.strip(): continue
                
                response = self.get_response(user_msg)
                self.typing_effect(response)
            except KeyboardInterrupt:
                break

        print(f"\n{R}[SYSTEM SHUTDOWN]{W}")

if __name__ == "__main__":
    bot = DecodeLabsProBot()
    bot.start()