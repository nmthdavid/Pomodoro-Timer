from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
t = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(t)
    canvas.itemconfig(timer,text="00:00")
    label.config(text="Timer",fg = GREEN)
    mark = ""
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    shortbreak_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps ==7:
        countdown(work_sec)
        label.config(text="Work",fg="red")
    elif reps % 2 == 0:
        countdown(shortbreak_sec)
        label.config(text="Break",fg="green")
    elif reps == 8:
        countdown(longbreak_sec)
        label.config(text="Break", fg="green")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    time_min = math.floor(time/60)
    time_sec = time % 60
    if time_sec < 10:
        time_sec= f"0{time_sec}"
    canvas.itemconfig(timer,text=f"{time_min}:{time_sec}")
    if time > 0:
        global t
        t = window.after(1000,countdown,time-1)

    else:
        start_timer()
        mark = ""
        work = math.floor(reps/2)
        for _ in range(work):
            mark += "✔"
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=image)
timer = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

start_button = Button(text="Start",highlightthickness=0,highlightbackground=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,highlightbackground=YELLOW,command=reset)
reset_button.grid(column=2,row=2)

checkmark = Label(fg=GREEN,bg=YELLOW)
checkmark.grid(row=2,column=1)

window.mainloop()