from tkinter import*

window=Tk()
window.title("Miles to KM")
window.minsize(width=50, height=40)


def miles_km():
    m=float(milesin.get())
    km=m* 1.609
    ans.config(text=f"{km}")

milesin=Entry()
milesin.grid(row=1,column=2)

miles=Label(text="Miles")
miles.grid(row=1, column=3)

km=Label(text="KM")
km.grid(row=2, column=3)

equalto=Label(text="is equal to")
equalto.grid(row=2, column=1)

cal=Button(text="Calculate", command=miles_km)
cal.grid(row=3, column=2)

ans=Label(text="0")
ans.grid(row=2, column=2)





window.mainloop()