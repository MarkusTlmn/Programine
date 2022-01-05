from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height = 300)
kõrgus  = 100
# paigutame tahvli raami ja teeme nähtavaks
i = 0
while i < 3:
    if i == 0 or i == 2:
        tahvel.create_rectangle(0, i * kõrgus, 100, (i + 1) * kõrgus, fill="blue", outline="blue")
        # valge suur ristkülik
        tahvel.create_rectangle(200, i * kõrgus, 400, (i + 1) * kõrgus, fill="white", outline="white")
    # teine joon
    else:
        # valge väike ristkülik
        tahvel.create_rectangle(10, i * kõrgus, 600, (i + 1) * kõrgus, fill="white", outline="white")
        # sinine suur ristkülik
        tahvel.create_rectangle(200, i * kõrgus, 300, (i + 1) * kõrgus, fill="blue", outline="blue")
    # tsüklimuutuja suurendamine
    i += 1
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()