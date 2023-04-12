from tkinter import *
import math
from tkinter import messagebox

WORK_MIN=25
SHORT_BREAK=5
LONG_BREAK=20

def start_timer():
    count_down(120)

def restet_timer():
    is_ok = messagebox.askyesno(title="Restart", message="Do you want to restart:")
    if is_ok:
        count_down(120)

def count_down(count):

    count_min= math.floor(count/60)
    count_sec= count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count-1)




window=Tk()
window.title("pomodora",)
window.config(padx=100, pady=50, bg="#f7f5dd")

canvas=Canvas(width=200, height=214, bg="#f7f5dd", highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100, 102, image=tomato)
canvas.grid(row=2, column=1)
timer_text = canvas.create_text(102,128, text="00:00", fill="white", font=("courier", 30, "bold"))


timer= Label(text="Timer", fg="#FCC2FC", bg="#f7f5dd", font=("courier", 30, "bold"))
timer.grid(row=1, column=1)

start =Button(text="start", command=start_timer)
start.grid(row=3, column=0)

reset =Button(text="reset", command=restet_timer)
reset.grid(row=3, column=3)

checkmark= Label(text="✔", fg="#FCC2FC", bg="#f7f5dd")
checkmark.grid(row=4, column=1,)
window.mainloop()