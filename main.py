import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk() 
root.title("Save Whales")
root.geometry("1000x650")
bluecolor = "#c1dce4"
root.config(bg=bluecolor)


frame = tk.Frame(root, width=500, height=300, bg=bluecolor)

# Title
title = tk.Label(text="Save the Whales", font=('Helvetica', 48), bg=bluecolor)
paragraph = tk.Label(frame, text="Donate today to ensure a safe future to our magnificent creatures.", font=('Helvetica', 17), justify='left', wraplength=245, bg=bluecolor)
email_label = tk.Label(frame, text="Enter email:", font=('Helvetica', 22), bg=bluecolor)
email = tk.Entry(frame, width=30, font=('Helvetica', 16))
password_label = tk.Label(frame, text="Enter password:", font=('Helvetica', 22), bg=bluecolor)
password = tk.Entry(frame, width=30, show='●', font=('Helvetica', 16))
button = tk.Button(frame, text="Register", width=8, height=1, font=('Helvetica', 18))
button.config(background='#0b1c3c', foreground='#000')

frame.place(x=50, y=200)

# Image
image = ImageTk.PhotoImage(Image.open("whale.jpg"))
canvas = tk.Canvas(root, width=560, height=650, highlightthickness=0)
canvas.create_image(250, 350, image=image)

title.grid(row=0, column=0 , padx=40, pady=80, sticky='w')
paragraph.grid(row=0, column=0, sticky='w', pady=(0,24))
email_label.grid(row=2, column=0, sticky='w')
email.grid(row=3, column=0, sticky='w', pady=(4, 0))
password_label.grid(row=4, column=0, sticky='w', pady=(12, 2))
password.grid(row=5, column=0, sticky='w', pady=(4, 0))
button.grid(row=6, column=0, sticky='w', pady=(12, 0))

canvas.grid(row=0, rowspan=9, column=1)

root.mainloop() 
