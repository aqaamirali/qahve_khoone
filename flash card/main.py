from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
    current_card = {}
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    current_card = {}


def next_card():
    global current_card
    current_card = random.choice(data_dict)
    canvas.itemconfig(language_word, text=current_card["French"], fill="black")
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(bg, image=card_front)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(language_word, text=current_card["English"], fill="white")
    canvas.itemconfig(bg, image=card_back)


def right_button_pressed():
    data_dict.remove(current_card)
    print(len((data_dict)))
    data1 = pandas.DataFrame(data_dict)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def wrong_button_pressed():
    next_card()


# window
window = Tk()
window.title(string="Flash_Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# card_front
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")


# card_back
card_back = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
bg = canvas.create_image(400, 263, image=card_front)
language_txt = canvas.create_text(400, 100, font=("Arial", 34, "italic"), text="Title")
language_word = canvas.create_text(400, 300, font=("Courier", 46, "bold"), text="Word")
canvas.grid(column=0, row=0, columnspan=2)


# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=right_button_pressed)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=wrong_button_pressed)
wrong_button.grid(column=0, row=1)

# where it all starts
next_card()





window.mainloop()
