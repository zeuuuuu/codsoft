import re
import random

class RuleBot:
    negative_response = ("no", "nope", "nah", "dont", "sorry", "never")
    exit_command = ("bye", "goodbye", "quit", "exit", "later")
    random_question = ("Who are you?", "Who created you?", "What is your name?")

    def __init__(self):
        self.support_responses = {
            'games_available': r'.*\s* games available',
            'on_sale': r'.*\s* on sale',
            'shop_accessories': r'.*\s* accessories',
            'gaming_consoles': r'.*\s* console',
            'delivery_conditions': r'.*\s* delivery',
            'return_policy': r'.*\s* return',
            'contact_us': r'.*contact.*help.*'
        }

    def greet(self):
        self.greet = input("Hello, Welcome! This is bubble. The game shop assistant!\n")
        self.name = input("Can you provide me with your username?")
        will_help = input(f"Hello {self.name}, is there any way I can help you?\n")
        if will_help in self.negative_response:
            print("Okay! Have a great day!")
        else:
            print("You can start chatting now.")
            self.chat()

    
   

    def make_exit(self, reply):
        if any(command in reply for command in self.exit_command):
            print("Thank you! Have a great day!")
            return True
        return False


    def chat(self):
        reply = input("How can I help you? Please list your query.")
        while not self.make_exit(reply):
            print(self.match_reply(reply))
            reply = input("Anything else?")

    def no_match_intent(self):
        return "I'm sorry, I didn't understand your query. Can you please provide more details?"

    def match_reply(self, reply):
        combined_responses = ""
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                combined_responses += self.get_response(intent)
        return combined_responses if combined_responses else self.no_match_intent()

    def get_response(self, intent):
        if intent == 'games_available':
            return self.games_available()
        elif intent == 'on_sale':
            return self.on_sale()
        elif intent == 'shop_accessories':
            return self.shop_accessories()
        elif intent == 'gaming_consoles':
            return self.gaming_consoles()
        elif intent == 'delivery_conditions':
            return self.delivery_conditions()
        elif intent == 'return_policy':
            return self.return_policy()
        elif intent == 'contact_us':
            return self.contact_us()

    def games_available(self):
        responses = ("Hey! We have a wide range of games. Listed below:",
                     "FIFA 23 (PS5) - 20 copies",
                     "Cyberpunk 2077 (Xbox Series X) - 15 copies",
                     "The Legend of Zelda: Breath of the Wild (Nintendo Switch) - 25 copies",
                     "Call of Duty: Warzone (PC) - 30 copies",
                     "Assassin's Creed Valhalla (PS4) - 15 copies\n",
                     "You can find all the details on our website.\n")
        return "\n".join(responses)

    def on_sale(self):
        responses = ("These are games that are on discount right now!:"
                     "FIFA 23 (PS5) Price: $69.99 Quantity: 20 Discount: 10%",
                     "Call of Duty: Warzone (PC) Price: $44.99 Quantity: 30 Discount: 20%\n",
                     "You can find all the details on our website.\n")
        return "\n".join(responses)

    def shop_accessories(self):
        responses = ("Accessories available!:"
                     "Wireless Gaming Mouse - 30 units",
                     "Mechanical Gaming Keyboard - 25 units",
                     "Gaming Headset - 40 units",
                     "Controller Charging Station - 20 units",
                     "Gaming Mouse Pad - 50 units\n",
                     "You can find all the details on our website.\n")
        return "\n".join(responses)

    def gaming_consoles(self):
        responses = ("Below listed are the gaming consoles available!:"
                     "PlayStation 5 - 10 units",
                     "Xbox Series X - 8 units",
                     "Nintendo Switch - 15 units\n",
                     "You can find all the details on our website.\n")
        return "\n".join(responses)

    def delivery_conditions(self):
        responses = ("We ship our products all over India."," Also, the delivery is free if the outstanding amount is above 999/- rupees.",
                     "Anything less than that will cost more 100/- rupees as a delivery fee.")
        return "\n".join(responses)

    def return_policy(self):
        responses = ("Returns are only allowed within 7 days after receiving the product.",
                     "Note: Returns are only applicable for consoles and accessories.",
                     "Will not be applicable for purchased games.")
        return "\n".join(responses)

    def contact_us(self):
        responses = ("For more details, you can visit our website. Or you can mail us your query at gameshop@gmail.com")
        return "\n".join(responses)


bot = RuleBot()
bot.greet()
