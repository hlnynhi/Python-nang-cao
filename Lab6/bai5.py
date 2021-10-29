from tkinter import *

def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{celsius}"

window = Tk()
name = Label(window, text = "Temperature in Fahrenheit")
frm_entry = Frame(window)
ent_temperature = Entry(frm_entry)
lbl_temp = Label(frm_entry)

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = Button(window, text="Convert", command=fahrenheit_to_celsius)
btn_quit = Button(window, text="Quit", command=lambda: window.destroy())

lbl_result = Label(window)

name.grid(row=0, column=0, padx=10)
frm_entry.grid(row=1, column=0, padx=10)
lbl_result.grid(row=2, column=0, padx=10)
btn_convert.grid(row=3, column=0, pady=10)
btn_quit.grid(row=4, column=0)
window.mainloop()