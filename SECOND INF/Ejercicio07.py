import tkinter as tk
import random

root = tk.Tk()
root.title("Juego de Memoria")

def initialize_cards():
    cards = [1, 2, 3, 4, 1, 2, 3, 4]
    random.shuffle(cards)
    return cards

cards = initialize_cards()

first_card = None
second_card = None
is_first = True

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

card_labels = []

def update_display():
    global canvas
    for i in range(8):
        if cards[i] == 0:
            canvas.itemconfig(card_labels[i], text=" ", font=("Arial", 16))
        else:
            canvas.itemconfig(card_labels[i], text=str(cards[i]), font=("Arial", 16))

def card_click(index):
    global first_card, second_card, is_first

    if is_first:
        first_card = index
        is_first = False
    else:
        second_card = index
        is_first = True

        if cards[first_card] == cards[second_card]:
            canvas.itemconfig(card_labels[first_card], text=" ")
            canvas.itemconfig(card_labels[second_card], text=" ")
            cards[first_card] = 0
            cards[second_card] = 0

            if sum(cards) == 0:
                result_label.config(text="¡Has ganado!")
            else:
                canvas.after(1000, reset_cards)
        else:
            canvas.after(1000, reset_cards)

    update_display()

def reset_cards():
    global canvas, cards
    cards = initialize_cards()
    update_display()

for i in range(8):
    x = (i % 4) * 100
    y = (i // 4) * 100
    label = canvas.create_text(x + 35, y + 35, text=str(cards[i]), font=("Arial", 16))
    card_labels.append(label)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

new_game_button = tk.Button(root, text="Nuevo Juego", command=reset_cards)
new_game_button.pack()

update_display()

root.mainloop()
