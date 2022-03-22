class Player:  # Класс, отвечающий за связь игры и ии/игрока, нужен для установки между ними четкого контракта
    def __init__(self, input_handler):
        self.input_handler = input_handler

    def decide_take(self, current_matches_number):
        return self.input_handler.decide_take(current_matches_number)
