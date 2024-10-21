from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = 1500
    short_break_sec = 300
    long_break_sec = 900
    if reps == 0 or reps % 2 == 0:
        reps += 1
        count_down(work_sec)
        text.config(text="Work", fg=GREEN)
    elif reps == 7:
        reps = 0
        count_down(long_break_sec)
        text.config(text="Long Break", fg=RED)
    else:
        reps += 1
        count_down(short_break_sec)
        text.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = math.floor(count / 60)
    sec = math.floor(count % 60)
    if 0 < sec < 10:
        sec = f"0{sec}"
    elif sec == 0:
        sec = "00"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Program")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, font=(FONT_NAME, 35, "bold"), fill="white", text="00:00")
canvas.grid(column=1, row=1)

text = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
text.grid(column=1, row=0)

button1 = Button(text="start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=3)

button2 = Button(text="reset", highlightthickness=0, command=reset_timer)
button2.grid(column=3, row=3)

check = Label(bg=PINK, fg=YELLOW, font=(FONT_NAME, 12, "bold"))
check.grid(column=1, row=4)

window.mainloop()
