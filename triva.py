import requests
from tkinter import *
from question import *
import html
response=requests.get("https://opentdb.com/api.php?amount=10&category=19&type=boolean")
response.raise_for_status()


data= response.json()["results"]

question_bank = []
for i in data:
    question= i["question"]
    answer=i["correct_answer"]
    question_ans=(question, answer)
    question_bank.append(question_ans)


question= Question(question_bank)


def tick_click():
    if question.still_has_question() is True:
        if question.check_ans(user_ans="True") is True:
            canvas.config(bg="green")
            score.config(text=f"score: {question.score}")
        else:
            canvas.config(bg="red")
        window.after(1000, func=white)
        canvas.itemconfig(new_question, text=html.unescape(question.next_question()))
    else:
        canvas.itemconfig(new_question, text="Quiz has ended")
        tick_button.config(state="disabled")

def white():
    canvas.config(bg="white")

def x_click():
    if question.still_has_question() is True:
        if question.check_ans(user_ans= "False") is True :
            score.config(text=f"score: {question.score}")
            canvas.config(bg="green")
        else:
            canvas.config(bg="red")
        window.after(1000, func=white)
        canvas.itemconfig(new_question, text=html.unescape(question.next_question()))
    else:
        canvas.itemconfig(new_question, text="Quiz has come to an end:")
        x_button.config(state="disabled")

window= Tk()
window.title("Quizzler")
window.config(width=500, height=600, bg="black")


score= Label(text=f"score: 0", bg="white")
score.place(x=380, y=30)

canvas= Canvas()
canvas.config(bg="white", width=350, height=400)
new_question = canvas.create_text(180, 200, width=320, text=question.next_question())
canvas.place(x=80,y=60)

tick_img= PhotoImage(file="img/right.png")
tick_button=Button(image=tick_img, bg="black", highlightthickness=0, command=tick_click)
tick_button.place(x=150,y=480)

x_img= PhotoImage(file="img/wrong.png")
x_button=Button(image=x_img, bg="black", highlightthickness=0, command=x_click)
x_button.place(x=300, y=480)
window.mainloop()