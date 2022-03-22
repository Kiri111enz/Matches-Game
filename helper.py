import tkinter as tk
import tkinter.messagebox as tk_mbox


def clear_grid(parent):  # убирает существующие элементы интерфейса
    for slave in parent.grid_slaves():
        slave.destroy()


def show_incorrect_input_warning():  # указывает пользователю на неверность ввода
    tk_mbox.showwarning('Ошибка ввода!', 'Похоже, введенные данные некорректны! Проверьте их еще раз.')


def create_button(parent, text, font, command, row=0, column=0):  # размещает кнопку
    tk.Button(parent, text=text, font=font, command=command).grid(row=row, column=column, sticky='ew')


def create_label(parent, text, font, anchor='center', row=0, column=0):  # размещает текст
    tk.Label(parent, text=text, font=font, anchor=anchor).grid(row=row, column=column, sticky='ew')


def get_new_entry(parent, font, row=0, column=0):  # возвращает новую линию ввода
    entry = tk.Entry(parent, font=font)
    entry.grid(row=row, column=column)

    return entry


def show_he_took_last():  # указывает пользователю, что взяты оставшиеся спички
    tk_mbox.showwarning('Осталось меньше спичек, чем вы взяли!', 'Взяты оставшиеся спички.')


def block_exiting():  # указывает пользователю на невозможность выйти
    tk_mbox.showwarning('Вы пытаетесь выйти!', 'Выход из программы доступен с помощью кнопки "Выйти" в меню.')


def finish_application(parent):  # завершает работу приложения и закрывает его
    parent.quit()
    parent.destroy()
