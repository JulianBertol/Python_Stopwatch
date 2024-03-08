import tkinter as tk
import threading
seconds = 0
minutes = 0
stop = 0
pressed_start = 0

def start_timer():
    global stop, pressed_start
    if pressed_start == 0:
        stop = 0
        timer_func()
        pressed_start = 1

def timer_func():
    if stop == 0:
        global seconds, minutes
        threading.Timer(1.0, timer_func).start()
        if seconds >= 59:
            minutes = minutes + 1
            seconds = 0
        seconds = seconds + 1
        if seconds < 10 and minutes < 10:
            timer.config(text="0{} : 0{}".format(minutes, seconds))
        elif seconds < 10 and minutes > 9:
            timer.config(text="{} : 0{}".format(minutes, seconds))
        elif seconds > 9 and minutes < 10:
            timer.config(text="0{} : {}".format(minutes, seconds))
        else:
            timer.config(text="{} : {}".format(minutes, seconds))

def stop_timer():
    global stop, pressed_start
    stop = 1
    pressed_start = 0

window = tk.Tk()
window.title("Stopuhr")
win_width= window.winfo_screenwidth()
win_height= window.winfo_screenheight()
window.geometry("%dx%d" % (win_width, win_height))
window.configure(bg="gray")


time = str(minutes) + "0 : 0" + str(seconds)
timer = tk.Label(text = time,
                 foreground ="white",
                 background = "blue",
                 )

font_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.5 * 0.4)  # 40% der Bildschirmgröße
timer.config(font=("Helvetica", font_size))

timer.place(
    relx=0.25,  # 50% der Breite (0.5) / 2 = 0.25
    rely=0.25,  # 50% der Höhe (0.5) / 2 = 0.25
    relwidth=0.5,  # 50% der Breite
    relheight=0.5,  # 50% der Höhe
)

#Start Button
button = tk.Button(
    text = "Start",
    bg = "green",
    fg = "white",
    command = start_timer
)
button.place(
    relx = 0.35,
    rely = 0.75,
    relwidth = 0.15,
    relheight = 0.15
)
btn_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.5 * 0.05)  # 40% der Bildschirmgröße
button.config(font=("Helvetica", btn_size))

#button stop
btn_stop = tk.Button(
    text = "Stop",
    bg = "red",
    fg = "white",
    command = stop_timer
)
btn_stop.place(
    relx = 0.5,
    rely = 0.75,
    relwidth = 0.15,
    relheight = 0.15
)
btn_stop.config(font=("Helvetica", btn_size))
window.mainloop()
