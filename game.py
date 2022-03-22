from player import Player
from player_input import PlayerInput
from bot_input import BotInput


class Game:  # Класс, отвечающий за логику игры
    def __init__(self, application, is_standard_game, is_single_player, matches_number, min_take, max_take):
        self.application = application
        self.is_standard_game = is_standard_game
        self.players = [Player(PlayerInput(1, min_take, max_take)), Player(BotInput(min_take, max_take))
                        if is_single_player else Player(PlayerInput(2, min_take, max_take))]
        self.matches_number = matches_number

    def play(self):  # непосредственно игра
        while True:
            for i in range(len(self.players)):
                self.matches_number -= self.players[i].decide_take(self.matches_number)
                self.application.update_matches_number(self.matches_number)

                if self.matches_number <= 0:
                    return self.players[i - 1 if self.is_standard_game else i]
