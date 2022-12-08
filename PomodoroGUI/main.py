from tkinter import *


# ------------------- CONSTANTS ------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
POMODOROS = 0
TIMER = None
reps = 0

# ------------------ TIMER RESET ------------------ #
def reset():
    global reps, POMODOROS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    task.config(text="Ready to work?")
    pomodoros.config(text="Pomodoros: None", fg=GREEN)
    reps = 0
    POMODOROS = 0

# ---------------- TIMER MECHANISM ---------------- #
def start():
    global reps, POMODOROS
    reps += 1
    if reps % 8 == 0:
        task.config(text="Long break!", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        task.config(text="Short break!", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        task.config(text="Work!", fg=GREEN)
        POMODOROS += 1
        countdown(WORK_MIN*60)
    display_pomodoros()

def display_pomodoros():
    pomodoros.config(text="Session: {}/4".format(POMODOROS))
    if POMODOROS == 4:
        reset_pomodoros()

def reset_pomodoros():
    global POMODOROS
    POMODOROS = 0

# -------------- COUNTDOWN MECHANISM -------------- #
def countdown(seconds):
    global TIMER
    canvas.itemconfig(timer_text, text="{}:{}".format(timer_format(seconds // 60), timer_format(seconds % 60)))
    if seconds > 0:
        TIMER = window.after(1000, countdown, seconds-1)
    else:
        start()

def timer_format(number):
    if number > 9:
        return "{}".format(number)
    else:
        return "0{}".format(number)


# -------------------- UI SETUP ------------------- #

# Window
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=75, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# Labels
task = Label(text="Ready to work?", font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
task.place(x=105, y=-40, anchor=CENTER)
pomodoros = Label(text="Session: None", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
pomodoros.pack()

# Buttons
button_start = Button(text="START", command=start)
button_start.place(x=0, y=250)
button_reset = Button(text="RESET", command=reset)
button_reset.place(x=130, y=250)

# Keep UI up
window.mainloop()
