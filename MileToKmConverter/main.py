from tkinter import *

FONT = ("Arial", 12, "normal")


def calculate():
    miles = float(miles_entry.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

equality_label = Label(text="is equal to", font=FONT)
equality_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

window.mainloop()
