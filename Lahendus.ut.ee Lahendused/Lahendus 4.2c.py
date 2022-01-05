from tkinter import *
raam = Tk()
raam.title("Liiklusmärk")

tahvel = Canvas(raam, width=600, height = 600)
tahvel.create_rectangle(100,170,500,500, fill="green", outline="black")
tahvel.create_rectangle(470,300,350,500, fill="brown", outline="black")
tahvel.create_rectangle(375,400,355,405, fill="black", outline="black")
tahvel.create_rectangle(150,300,310,450, fill="aqua", outline="black")
tahvel.create_polygon(90,170,300,100,510,170,fill="gray", outline ="gray")
# laius paremale, ülevalt alla, laius vasakult, alla
tahvel.pack()

raam.mainloop()