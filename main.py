from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_dic = {}
timer_count = None

window = Tk()
window.title("Flash Card")

window.maxsize(width=900, height=1200)
window.resizable(False, False)
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)


try:
    data = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv").to_dict(orient="records")


def next_card():
    global return_timer, random_dic
    window.after_cancel(return_timer)
    random_dic = random.choice(data)
    canvas.itemconfig(word, text=random_dic["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    return_timer = window.after(3000, func=return_card)


def return_card():
    canvas.itemconfig(word, text=random_dic["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def is_known():
    data.remove(random_dic)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


return_timer = window.after(3000, func=return_card)

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="Text1", font=("Arial", 25, "italic"))
word = canvas.create_text(400, 263, text="Text2", font=("Arial", 40, "bold"))
timer_text = canvas.create_text(725, 50, text="", font=("Arial", 35, "italic"), fill="black")


image_right = PhotoImage(file="images/right.png")
canvas_button_ok = Button(image=image_right, highlightthickness=0, borderwidth=0, command=is_known)
canvas_button_ok.grid(row=1, column=0)

image_wrong = PhotoImage(file="images/wrong.png")
canvas_button_ok = Button(image=image_wrong, highlightthickness=0, borderwidth=0, command=next_card)
canvas_button_ok.grid(row=1, column=1)

next_card()

window.mainloop()
