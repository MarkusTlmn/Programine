ring = int(input("Sisesta ringide arv: "))
if ring <= 0:
    print ("vale arv!")
i = 0
por = 0
for i in range(0, ring+1, 2):
    por += i
    
print(por)    

