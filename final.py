import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

# -------------------------
# Global flags
# -------------------------
stop_flag = False
pause_flag = False

# -------------------------
# Typing function
# -------------------------
def type_text(text, delay, speed):
    global stop_flag, pause_flag
    
    # Countdown
    for i in range(delay, 0, -1):
        if stop_flag:
            countdown_label.config(text="Typing Stopped!")
            return
        countdown_label.config(text=f"Starting in {i} seconds...")
        time.sleep(1)

    countdown_label.config(text="Typing Started!")
    
    # Typing loop
    for char in text:
        if stop_flag:
            countdown_label.config(text="Typing Stopped!")
            return
        while pause_flag:
            countdown_label.config(text="Typing Paused...")
            time.sleep(0.2)
        pyautogui.write(char)
        time.sleep(speed)
    
    countdown_label.config(text="Typing Completed!")
    messagebox.showinfo("Done", "Typing completed!")

# -------------------------
# Button functions
# -------------------------
def start_typing():
    global stop_flag, pause_flag
    stop_flag = False
    pause_flag = False

    text = text_entry.get("1.0", tk.END).strip()
    delay = delay_entry.get()
    speed = speed_entry.get()

    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return
    if not delay.isdigit():
        messagebox.showerror("Error", "Enter a valid delay time in seconds.")
        return
    try:
        speed_val = float(speed)
        if speed_val <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter a valid typing speed (e.g., 0.05).")
        return

    delay = int(delay)
    threading.Thread(target=type_text, args=(text, delay, speed_val)).start()

def stop_typing():
    global stop_flag
    stop_flag = True

def pause_typing():
    global pause_flag
    pause_flag = not pause_flag  # toggle pause/resume

def restart_gui():
    global stop_flag, pause_flag
    stop_flag = True
    pause_flag = False
    text_entry.delete("1.0", tk.END)
    delay_entry.delete(0, tk.END)
    speed_entry.delete(0, tk.END)
    countdown_label.config(text="")

def exit_app():
    stop_typing()
    root.destroy()

# -------------------------
# GUI Setup
# -------------------------
root = tk.Tk()
root.title("SwiftType Pro")
root.geometry("550x450")
root.configure(bg="#f0f0f0")

# -------------------------
# Big Title at Top
# -------------------------
title_label = tk.Label(root, text="SWIFTTYPE PRO -DEVELOPED BY SANTHOSH THE MATHEMATICIAN", font=("Helvetica", 26, "bold"), fg="#2c3e50", bg="#f0f0f0")
title_label.pack(pady=15)

# -------------------------
# Text input
# -------------------------
tk.Label(root, text="Enter Text:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
text_entry = tk.Text(root, height=6, font=("Arial", 11))
text_entry.pack(padx=15, pady=5)

# Delay input
tk.Label(root, text="Enter Delay (seconds):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
delay_entry = tk.Entry(root, font=("Arial", 11))
delay_entry.pack(pady=5)

# Typing speed input
tk.Label(root, text="Typing Speed (seconds per character):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
speed_entry = tk.Entry(root, font=("Arial", 11))
speed_entry.pack(pady=5)
speed_entry.insert(0, "0.05")  # default speed

# Countdown Label
countdown_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#e74c3c", bg="#f0f0f0")
countdown_label.pack(pady=10)

# -------------------------
# Buttons
# -------------------------
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", width=10, command=start_typing)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause/Resume", font=("Arial", 12, "bold"),
                         bg="#FFA500", fg="white", width=14, command=pause_typing)
pause_button.grid(row=0, column=1, padx=5)

stop_button = tk.Button(button_frame, text="Stop", font=("Arial", 12, "bold"),
                        bg="#f44336", fg="white", width=10, command=stop_typing)
stop_button.grid(row=0, column=2, padx=5)

restart_button = tk.Button(button_frame, text="Restart", font=("Arial", 12, "bold"),
                           bg="#2196F3", fg="white", width=10, command=restart_gui)
restart_button.grid(row=0, column=3, padx=5)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"),
                        bg="#555555", fg="white", width=10, command=exit_app)
exit_button.grid(row=0, column=4, padx=5)

# -------------------------
# Big Developer Credit at Bottom
# -------------------------
developer_label = tk.Label(root, text="Developed by santhosh.s", font=("Helvetica", 18, "bold"), fg="#34495e", bg="#f0f0f0")
developer_label.pack(side="bottom", pady=15)

root.mainloop()
