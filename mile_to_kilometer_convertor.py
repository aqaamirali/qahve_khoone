from tkinter import *
window = Tk()
window.title("mile to km converter")


def mile_to_km(value=0):
    value = int(entry.get())
    value *= 1.60934
    km.config(text=f"{round(value, 2)}")
    entry.delete(0, END)


# user entry
entry = Entry()
entry.grid(column=1, row=0)

# labels
mile = Label(text="Miles")
mile.grid(column=2, row=0)
eq = Label(text="is equal to")
eq.grid(column=0, row=1)
km = Label(text="0")
km.grid(column=2, row=1)

# button
button = Button(text="calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
