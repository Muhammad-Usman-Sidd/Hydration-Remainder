import pyttsx3
import tkinter as tk
from tkinter import messagebox
import time
repeating_time = 50  # this will repeat after 50 seconds
a = input("Enter your name :")

while True:

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    speak(f"hey {a} , drink water!")

    def display_alert(title, message):
        b = tk.Tk()
        b.withdraw()
        messagebox.showinfo(title, message)
    display_alert(f"For {a}", "Drink water!")
    time.sleep(repeating_time)
