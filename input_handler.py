from abc import ABCMeta, abstractmethod


class InputHandler(metaclass=ABCMeta):  # Интерфейс для классов, управляющих игроком (настоящим или виртуальным)
    def __init__(self, min_take, max_take):
        self.min_take = min_take
        self.max_take = max_take

    @abstractmethod
    def decide_take(self, current_matches_number):  # возвращает число спичек, взятое игроком или ботом
        pass
