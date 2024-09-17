from tkinter import *

def mile_to_kilo():
    miles=float(miles.input.get())
    km=miles*1.689
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilo Converter")
window.config(padx=20,pady=20)

mile_input=Entry(width=7)
mile_input.grid(column=1,row=0)

mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

result_label=Button(text="Calculate",command=mile_to_kilo)
result_label.grid(column=1,row=2)

window.mainloop()