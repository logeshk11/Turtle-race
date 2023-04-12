from tkinter import  *
import requests


window=Tk()


window.title("Kanye Quotes")
window.config(padx=50, pady=50)

def get_quote():
    response = requests.get("https://api.kanye.rest")
    data= response.json()
    canvers.itemconfig(quote, text=data['quote'])

bg_img= PhotoImage(file="img/background.png")
canvers= Canvas(width=300, height=414,)
canvers.create_image(150, 207, image=bg_img)

canvers.grid(column=0, row=0)
quote = canvers.create_text(150,207, text="Click the Button ", font=("Airel", 20, "bold"), fill="white")

kanye_img= PhotoImage(file="img/kanye.png")
kanye_button = Button(image=kanye_img, command=get_quote, highlightthickness=0)
kanye_button.grid(column=0, row=1)
window.mainloop()