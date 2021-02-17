from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=250)


# Miles input box
input_box = Entry()
input_box.grid(column=2, row=1, padx=20, pady=20)

# Miles label
ml = Label(text="Miles")
ml.grid(column=3, row=1, padx=20, pady=20)

# Is equal to label
equal_to = Label(text="is equal to")
equal_to.grid(column=1, row=2, padx=20, pady=20)

# results label
result = Label(text="0")
result.grid(column=2, row=2, padx=20, pady=20)

# Kilometer label
km = Label(text="Km")
km.grid(column=3, row=2, padx=20, pady=20)


# Miles to Km
def miles_to_km():
    formulary = int(input_box.get()) * 1.60934
    result["text"] = round(formulary, 2)


# Calculate button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=2, row=3, padx=20, pady=20)

window.mainloop()
