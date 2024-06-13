# 1. tk.Tk() - создание основного окна приложения.
# 2. pack() - метод для управления расположением виджета в окне.
# 3. grid() - метод для расположения виджетов в сетке окна.
# 4. place() - метод для позиционирования виджетов с точными координатами.
#
# Для создания различных виджетов и их конфигурации:
#
# 1. tk.Label() - создание текстовой метки.
# 2. tk.Button() - создание кнопки.
# 3. tk.Entry() - создание поля ввода текста.
# 4. tk.Text() - создание многострочного текстового поля.
# 5. tk.Checkbutton() - создание флажка (чекбокса).
# 6. tk.Radiobutton() - создание радиокнопки.
# 7. tk.Listbox() - создание списка для выбора элементов.
# 8. tk.Canvas() - создание холста для рисования графики.
#
# Для работы с событиями и обработки пользовательского ввода:
#
# 1. bind() - метод для привязки событий к виджетам.
# 2. get() - метод для получения значения из поля ввода.
# 3. insert() - метод для вставки текста в виджет.
# 4. delete() - метод для удаления части текста из виджета.
# 5. curselection() - метод для получения выбранных элементов из списка или другого виджета.
# 6. itemconfig() - метод для конфигурации отдельных элементов в списке или холсте.

# Напишите программу на Python с использованием модуля tkinter,
# которая позволяет пользователю ввести свое имя в окно ввода,
# а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk

root = tk.Tk()
root.title("Приветствие!")

label = tk.Label(root, text="Введите свое имя:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

label2 = tk.Label(root, text="")
label2.grid(row=2)

def on_get_greeting():
    name = entry.get()
    label2.config(text=f"Привет, {name}!")

button = tk.Button(root, text="Get greeting", command=on_get_greeting)
button.grid(row=1)

root.mainloop()