from tkinter import*

window=Tk()

window.title("Tkinter")
window.minsize(width=500, height=400)

mylabel=Label(text="This is logesh")
mylabel.grid(row=1, column=1)

input=Entry()
input.grid(row=2, column=2)

def button_clicked():
    mylabel.config(text=input.get())

button= Button(text="button", command=button_clicked)
button.grid(row=3, column=4)

button1=Button(text="new button")
button1.grid(row=1,column=3)
# text=Text(height=5,width=30)
# text.focus()
# text.insert(END,"hai")
# print(text.get("1.0", END))
# text.pack()
#
# def spinbox_used():
#     print(spinbox.get())
#
# spinbox=Spinbox(from_=0, to=15, command=spinbox_used)
# spinbox.pack()
#
# def scale_used(value):
#     print(value)
#
# scale=Scale(from_=0, to=60, command=scale_used)
# scale.pack()
#
# def checkbutton_used():
#     print(check_state.get())
# check_state=IntVar()
# check_button=Checkbutton(text="Button on ", variable=check_state, command=checkbutton_used)
# check_button.pack()
#
# def radiobutton_clicked():
#     print(radio_state.get())
#
# radio_state=IntVar()
# radio_button1= Radiobutton(text="option 1",value=1, variable=radio_state, command=radiobutton_clicked)
# radio_button2= Radiobutton(text="option 2",value=2, variable=radio_state, command=radiobutton_clicked)
# radio_button1.pack()
# radio_button2.pack()
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
# listbox=Listbox(height=4)
# fruits=["apple","orange","Grapes","mango"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
#
# listbox.pack()


window.mainloop()

