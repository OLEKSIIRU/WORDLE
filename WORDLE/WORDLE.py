import tkinter as tk
from tkinter import messagebox
import random

# Определение глобальных переменных
char_count = 0
current_row = 0
input_labels = []
random_word_parts = []
label_list = []  # Создаем пустой список меток

def read_words_from_file(file_path):
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words.append(line.strip())  # Удаляем лишние пробелы и символы новой строки
    except FileNotFoundError:
        print("Файл не найден.")
    return words

def choose_random_word(words):
    return random.choice(words)

def split_random_word_into_five_letters(random_word):
    five_letter_parts = []
    
    # Разбиваем случайное слово на пятибуквенные части и добавляем их в список
    for i in range(0, len(random_word), 5):
        five_letter_parts.append(random_word[i:i+5])
    
    return five_letter_parts

def check_word_match(input_labels, random_word_parts):
    # Получаем введенные значения из меток
    entered_letters = [label.cget("text") for label in input_labels]
    
    # Сравниваем каждую букву введенного слова с буквой на соответствующей позиции в случайном слове
    for i, (entered_letter, random_letter) in enumerate(zip(entered_letters, random_word_parts)):
        if entered_letter == random_letter:
            input_labels[i].config(bg="green")  # Закрашиваем фон зеленым, если буквы совпадают на правильной позиции
        elif entered_letter in random_word_parts:  # Проверяем совпадение буквы на другой позиции
            input_labels[i].config(bg="yellow")  # Закрашиваем фон желтым, если буквы совпадают, но на другой позиции
        else:
            input_labels[i].config(bg="white")  # В противном случае закрашиваем фон белым
    
    # Если все буквы введенного слова совпадают с буквами в случайном слове на тех же позициях, возвращаем True
    return entered_letters == random_word_parts

def check_win(input_labels, random_word_parts):
    entered_word = ''.join([label.cget("text") for label in input_labels])
    return entered_word == ''.join(random_word_parts)

def check_loss(current_row):
    return current_row == 6

def button_click(letter):
    global char_count, current_row
    
    if char_count < 5:
        label_list[current_row * 5 + char_count].config(text=letter)
        char_count += 1

def check_button_click():
    global char_count, current_row
    
    if char_count == 5:
        char_count = 0
        current_row += 1
        if current_row >= 6:
            current_row = 0
        if check_win(label_list[current_row * 5 : current_row * 5 + 5], random_word_parts):
            messagebox.showinfo("Поздравляем!", "Вы победили!")
        elif check_loss(current_row):
            messagebox.showinfo("Игра окончена.", "Вы проиграли.")

def backspace():
    global char_count, current_row
    if char_count > 0:
        char_count -= 1
        label_list[current_row * 5 + char_count].config(text="")

def exit_program():
    aken.destroy()

# Создание главного окна
aken = tk.Tk()
aken.title("WORDLE")
aken.configure(bg="black")  
aken.attributes('-fullscreen', True)  # Устанавливаем полноэкранный режим

# Чтение слов из файла
words = read_words_from_file("words.txt")

# Выбор случайного слова
random_word = choose_random_word(words)

# Разбиение случайного слова на пятибуквенные части
random_word_parts = split_random_word_into_five_letters(random_word)

# Создание фреймов и других элементов интерфейса
main_frame = tk.Frame(aken, bg="black")
main_frame.pack(expand=True, fill=tk.BOTH)

button_frame = tk.Frame(main_frame, bg="black")  
button_frame.pack(side=tk.BOTTOM, fill=tk.X)  # Размещаем фрейм с кнопками "Backspace" и "Выход" внизу основного фрейма

backspace_button = tk.Button(button_frame, text="Backspace", font="Arial 14 bold", bg="black", fg="white", relief=tk.RAISED, command=backspace,width=20)
backspace_button.pack(side=tk.RIGHT, padx=10, pady=10)

exit_button = tk.Button(button_frame, text="EXIT", font="Arial 18 bold", bg="red", fg="white", relief=tk.RAISED, command=exit_program, width=20)
exit_button.pack(side=tk.LEFT, padx=10, pady=10)

game_frame = tk.Frame(main_frame, bg="black", border=10)
game_frame.pack(side=tk.TOP, padx=10, pady=10)

l = tk.Label(game_frame, text="WELCOME WORDLE", bg="#0000CD", fg="#FFFFFF", font="Algerian 32")
l.grid(row=0, column=0, columnspan=5, pady=10)

# Создание ячеек
for i in range(6):
    for j in range(5):
        label = tk.Label(game_frame, text="", width=10, height=4, bg="#808080", borderwidth=1, relief="solid")
        label.grid(row=i+1, column=j, padx=5, pady=5)
        label_list.append(label)

# Создание кнопки "Проверить"
btn = tk.Button(game_frame, text="Проверить", font="Arial 18", bg="#00FFFF", relief=tk.RAISED, command=check_button_click)
btn.grid(row=8, column=2, columnspan=2, pady=10)

# Создание кнопок клавиатуры
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
