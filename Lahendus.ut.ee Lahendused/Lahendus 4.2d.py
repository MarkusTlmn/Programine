from tkinter import *
raam = Tk()
raam.title("Malelaud")

tahvel = Canvas(raam, width=600, height = 600)

suurus = 30

tahvel.pack()

color = 'white'

for y in range(8):

    for x in range(8):
        x1 = x*suurus
        y1 = y*suurus
        x2 = x1 + suurus
        y2 = y1 + suurus
        tahvel.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'

    if color == 'white':
        color = 'black'
    else:    
        color = 'white'

raam.mainloop()
