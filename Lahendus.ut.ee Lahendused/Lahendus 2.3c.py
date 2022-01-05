inimesed = int(input("Inimeste arv: "))
kohad = int(input("Kohtade arv = "))
esimene = ("Busse vaja: ")
teine = ("Viimases bussis inimesi: ")
viimane = inimesed % kohad
if viimane == 0 and inimesed > kohad:
   bussid = inimesed // kohad
   bussid = bussid 
   print ((esimene) + str(bussid))
   arv = 20
   print ((teine) + str(arv))
elif inimesed > kohad:
   bussid = inimesed // kohad
   bussid = bussid + 1
   print ((esimene) + str(bussid))
   viimane = inimesed % kohad
   print ((teine) + str(viimane))
elif inimesed == kohad:
   bussid = inimesed // kohad
   print ((esimene) + str(bussid))
   viimane = inimesed
   print ((teine) + str(viimane))
elif inimesed < kohad:
   bussid = 1
   print ((esimene) + str(bussid))
   viimane = inimesed
   print ((teine) + str(viimane))


