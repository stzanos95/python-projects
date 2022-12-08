from tkinter import *


def convert():
    value = float(entry_val.get())
    if radio_state.get() == 1:
        converted_value = value * 1.609
    else:
        converted_value = value * 0.621
    write_text(converted_value)

def update_fields():
    entry_val.delete(0, END)
    entry_val.insert(END, string="")
    write_text("")
    if radio_state.get() == 1:
        entry_unit["text"] = "miles"
        text_unit["text"] = "km"
    else:
        entry_unit["text"] = "km"
        text_unit["text"] = "miles"


def write_text(text):
    text_conv.config(state=NORMAL)
    text_conv.delete('1.0', END)
    text_conv.insert(END, text)
    text_conv.config(state=DISABLED)


window = Tk()
window.title("mile - km converter")
window.minsize(width=300, height=30)
window.config(padx=30, pady=20)


# Conversion fields
entry_val = Entry(width=10)
entry_val.place(x=0, y=50)
entry_unit = Label(text="miles")
entry_unit.place(x=87, y=53)
text_conv = Text(width=10, height=1)
text_conv.focus()
text_conv.config(state=DISABLED)
text_conv.place(x=0, y=75)
text_unit = Label(text="km")
text_unit.place(x=87, y=78)

# Buttons
button_conv = Button(text="convert", command=convert)
button_conv.place(x=150, y=58)

# Radiobuttons
radio_state = IntVar()
radiobutton1 = Radiobutton(text="miles to km",
                           value=1,
                           variable=radio_state,
                           command=update_fields)
radiobutton1.place(x=0, y=0)
radiobutton2 = Radiobutton(text="km to miles",
                           value=2,
                           variable=radio_state,
                           command=update_fields)
radiobutton2.place(x=120, y=0)


# Keep UI up
window.mainloop()
