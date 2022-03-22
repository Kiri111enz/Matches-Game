import random
from input_handler import InputHandler


class BotInput(InputHandler):  # Класс, отвечающий за решения ИИ, имплементация интерфейса InputHandler
    def decide_take(self, current_matches_number):
        return min(current_matches_number, random.randint(self.min_take, self.max_take))
