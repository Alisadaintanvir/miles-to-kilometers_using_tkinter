from tkinter import *


def miles_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(height=400, width=600)
window.config(padx=100, pady=100)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

miles_label_2 = Label(text="is equal to")
miles_label_2.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)

window.mainloop()
