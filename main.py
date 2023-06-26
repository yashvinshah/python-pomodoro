import math
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_br = SHORT_BREAK_MIN * 60
    long_br = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        countdown(long_br)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_br)
        label.config(text="Break", fg=PINK)
    else:
        countdown(work_secs)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        mark =""
        for x in range(math.floor(reps / 2)):
            mark += "✓"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)





label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_bt = Button(text="Start", command=start)
start_bt.grid(column=0, row=2)

reset_bt = Button(text="Reset", command=reset_timer)
reset_bt.grid(column=2, row=2)

check_marks = Label(font=("", 20, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

