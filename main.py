from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)
km_text = Label(text="Km")
km_text.grid(column=2, row=1)
is_equal_text = Label(text="is equal to")
is_equal_text.grid(column=0, row=1)


def calculate():
    miles = input.get()
    km = round(float(miles) * 1.609)
    result.config(text= km)


calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(row=2, column=1)
result = Label(text="0")
result.grid(column=1,row=1)
input = Entry()
input.grid(row=0, column=1)

window.mainloop()
