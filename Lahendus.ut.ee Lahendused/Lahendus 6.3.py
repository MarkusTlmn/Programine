x = int(input("Mitu inimest on kutsutud? "))
y = int(input("Mitu inimest tuleb? "))

def eelarve(eelarvemax):
    eelarve = (eelarvemax * 10 + 55)
    return(eelarve)
print (str(eelarve(x)) + " eurot")
print (str(eelarve(y)) + " eurot")
