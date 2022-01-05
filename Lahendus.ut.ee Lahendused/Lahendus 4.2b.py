from tkinter import *
raam = Tk()
raam.title("Liiklusmärk")

tahvel = Canvas(raam, width=600, height = 600)
tahvel.create_oval(100,100,500,500, fill="red", outline="red")
tahvel.create_oval(140,140,460,460, fill="white", outline="red")

tahvel.pack()

raam.mainloop()
