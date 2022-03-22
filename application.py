from functools import partial
import tkinter as tk
import tkinter.font as tk_font
import helper
from game import Game
from bot_input import BotInput


class Application(tk.Frame):  # Класс, отвечающий за интерфейс и его функционал
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.protocol('WM_DELETE_WINDOW', helper.block_exiting)
        self.parent.title('Спички')
        self.font = tk_font.Font(family='Lucida Sans', size=14)
        self.entries = []

        self.is_single_player = False
        self.is_standard_game = True

        self.choose_game_mode()

    def choose_game_mode(self):  # выбор режима игры
        labels = 'Играть с другим игроком', 'Играть против бота', 'Выйти'
        commands = partial(self.set_game_mode, False), partial(self.set_game_mode, True), \
            partial(helper.finish_application, self.parent)

        helper.clear_grid(self.parent)

        for i in range(len(labels)):
            helper.create_button(self.parent, labels[i], self.font, commands[i], i, 0)

    def set_game_mode(self, is_single_player):  # сохранение режима игры и переход к дальнейшей ее настройке
        self.is_single_player = is_single_player

        if self.is_single_player:
            self.choose_single_player_mode()
        else:
            self.choose_game_properties()

    def choose_game_properties(self):  # создает интерфейс для настройки условий игры
        labels = 'Изначальное количество спичек', \
                 'Минимальное количество спичек, которое можно взять', \
                 'Максимальное количество спичек, которое можно взять'

        helper.clear_grid(self.parent)
        self.entries = []

        for i in range(len(labels)):
            helper.create_label(self.parent, labels[i], self.font, 'e', i, 0)
            self.entries.append(helper.get_new_entry(self.parent, self.font, i, 1))

        helper.create_button(self.parent, 'Играть', self.font, self.try_start_the_game, len(labels), 1)

    def try_start_the_game(self):  # начинает игру, если введенные данные корректны
        matches_number, min_take, max_take = (entry.get() for entry in self.entries)

        try:  # проверка на то, что введенные данные - числа
            matches_number, min_take, max_take = int(matches_number), int(min_take), int(max_take)
        except ValueError:
            helper.show_incorrect_input_warning()
            return

        if min(matches_number, min_take, max_take) <= 0 or max(min_take, max_take) >= matches_number or \
                min_take >= max_take:  # проверка на то, что эти числа подходят
            helper.show_incorrect_input_warning()
            return

        game = Game(self, self.is_standard_game, self.is_single_player, matches_number, min_take, max_take)
        self.update_matches_number(matches_number)
        winner = game.play()

        self.show_end_game_screen(winner)

    def choose_single_player_mode(self):  # выбор стандартного режима или антиспичек при игре с ботом
        helper.clear_grid(self.parent)
        helper.create_button(self.parent, 'Обычная игра', self.font, partial(self.set_single_player_mode, True))
        helper.create_button(self.parent, 'Антиспички', self.font, partial(self.set_single_player_mode, False), 1, 0)

    def set_single_player_mode(self, is_standard_game):  # установка режима игры и переход к выбору других настроек
        self.is_standard_game = is_standard_game
        self.choose_game_properties()

    def show_end_game_screen(self, winner):  # показ результатов игры
        input_handler = winner.input_handler
        text = 'Выиграл бот' if isinstance(input_handler, BotInput) else f'Выиграл игрок {input_handler.index}'
        helper.create_label(self.parent, text, self.font)
        helper.create_button(self.parent, 'Вернуться в меню', self.font, self.choose_game_mode, 1, 0)
        helper.create_button(self.parent, 'Выйти', self.font, partial(helper.finish_application, self.parent), 2, 0)

    def update_matches_number(self, matches_number):  # обновление количества спичек после хода
        helper.clear_grid(self.parent)
        helper.create_label(self.parent, f'Оставшееся количество спичек: {matches_number}', self.font)


if __name__ == '__main__':
    Application(tk.Tk()).mainloop()  # запуск приложения
