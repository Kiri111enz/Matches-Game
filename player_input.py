from functools import partial
import tkinter as tk
import tkinter.font as tk_font
import helper
from input_handler import InputHandler


class PlayerInput(InputHandler):  # Класс, отвечающий за ввод от игрока, имплементация интерфейса InputHandler
    def __init__(self, index, min_take, max_take):
        super().__init__(min_take, max_take)
        self.font = tk_font.Font(family='Lucida Sans', size=14)

        self.index = index
        self.take = 0

    def decide_take(self, current_matches_number):
        app = tk.Tk()
        app.protocol('WM_DELETE_WINDOW', helper.block_exiting)
        app.title(f'Игрок {self.index}')
        entry = helper.get_new_entry(app, self.font)
        helper.create_button(app, 'Взять спички', self.font,
                             partial(self.get_take, app, entry, current_matches_number), 1, 0)
        app.mainloop()

        return self.take

    def get_take(self, app, entry, current_matches_number):  # обрабатывает введенные данные и убирает окно
        take = entry.get()

        try:  # проверка на то, что введено число
            take = int(take)
        except ValueError:
            helper.show_incorrect_input_warning()
            return

        if not self.min_take <= take <= self.max_take:  # проверка на то, что число подходит
            helper.show_incorrect_input_warning()
            return

        self.take = take

        if take > current_matches_number:  # проверка на то, что число не превосходит оставшегося количества спичек
            self.take = current_matches_number
            helper.show_he_took_last()

        helper.finish_application(app)
