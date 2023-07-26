import pyttsx3
import tkinter
from tkinter import messagebox
import time
a = input("Enter your name :")
seconds = int(input("After how many seconds you want this application to send remainder again ? "))
repeating_time = seconds
while True:

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    speak(f"hey {a} , drink water!")

    def display_alert(title, message):
        b = tkinter.Tk()
        b.withdraw()
        messagebox.showinfo(title, message)
    display_alert(f"For {a}", "Drink water!")
    time.sleep(repeating_time)
