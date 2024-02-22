import tkinter as tk
import random

def read_words_from_file(file_path):
    words = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words.append(line.strip())  # Удаляем лишние пробелы и символы новой строки
    except FileNotFoundError:
        print("Файл не найден.")
    return words

def button_click(letter):
    global char_count, current_row
    if char_count < 5:
        label_list[current_row * 5 + char_count].config(text=letter)
        char_count += 1
    else:
        char_count = 0
        current_row += 1
        if current_row >= 6:
            current_row = 0
        label_list[current_row * 5 + char_count].config(text=letter)
        char_count += 1

def backspace():
    global char_count, current_row
    if char_count > 0:
        char_count -= 1
        label_list[current_row * 5 + char_count].config(text="")

def exit_program():
    aken.destroy()

''' Создание главного окна'''
aken = tk.Tk()
aken.title("WORDLE")
aken.configure(bg="black")  
aken.attributes('-fullscreen', True)  # Устанавливаем полноэкранный режим


main_frame = tk.Frame(aken, bg="black")
main_frame.pack(expand=True, fill=tk.BOTH)


button_frame = tk.Frame(main_frame, bg="black")  


backspace_button = tk.Button(button_frame, text="Backspace", font="Arial 14 bold", bg="black", fg="white", relief=tk.RAISED, command=backspace,width=20)
backspace_button.pack(side=tk.RIGHT, padx=10, pady=10)


exit_button = tk.Button(button_frame, text="EXIT", font="Arial 18 bold", bg="red", fg="white", relief=tk.RAISED, command=exit_program, width=20)
exit_button.pack(side=tk.LEFT, padx=10, pady=10)

button_frame.pack(side=tk.BOTTOM, fill=tk.X)  # Размещаем фрейм с кнопками "Backspace" и "Выход" внизу основного фрейма


game_frame = tk.Frame(main_frame, bg="black", border=10)
game_frame.pack(side=tk.TOP, padx=10, pady=10)


l = tk.Label(game_frame, text="WELCOME WORDLE", bg="#0000CD", fg="#FFFFFF", font="Algerian 32")
l.grid(row=0, column=0, columnspan=5, pady=10)

''' Создание ячеек '''
label_list = []
for i in range(6):
    for j in range(5):
        label = tk.Label(game_frame, text="", width=10, height=4, bg="#808080", borderwidth=1, relief="solid")
        label.grid(row=i+1, column=j, padx=5, pady=5)
        label_list.append(label)

# Создание кнопки "Проверить"
btn = tk.Button(game_frame, text="Проверить", font="Arial 18", bg="#00FFFF", relief=tk.RAISED, command=lambda: print("Команда для кнопки"))
btn.grid(row=8, column=2, columnspan=2, pady=10)

''' Создание кнопок клавиатуры '''
buttons = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]

char_count = 0  # Счетчик для отслеживания количества введенных символов
current_row = 0  

for row_buttons in buttons:
    button_frame = tk.Frame(main_frame, bg="black")  # Поле для кнопок
    button_frame.pack(side=tk.TOP, padx=10, pady=5)
    for button in row_buttons:
        tk.Button(button_frame, text=button, width=5, height=2,
                  command=lambda b=button: button_click(b), bg="black", fg="white").pack(side=tk.LEFT, padx=5, pady=5)

aken.mainloop()
