szoveg="""Ha itt a nyár, ugye komám, a szív a víznek szalutál
és vígan lépked, akár a tornász
így megy a nagy ho-ho-ho horgász.
Bátran rikkant, puhányok ho-ho-ho-ho-ho,
megint csak ho-ho-ho-ho.
Van itt csali és egy két horog, az eszem pedig jól forog,
cselt a cselre kiválón sorjáz, ravasz a nagy ho-ho-ho horgász.
Városbéli puhányok, nyavalyások ha gyötör a láz,
fületek nyissátok gyorsan, hallgassátok,
amit most néktek, hallgassátok,
amit most néktek eldalol a ho-ho-ho nagy horgász.
Ha itt a nyár, ugye komám, a szív a víznek szalutál,
és vígan lépked, akár a tornász így megy a nagy ho-ho-ho horgász.
Bátran rikkant, puhányok ho-ho-ho-ho-ho,
megint csak ho-ho-ho-ho.
Van itt csali és egy két horog,
az eszem pedig jól forog,
cselt a cselre kiválón sorjáz,
ravasz a nagy ho-ho-ho horgász.
Városbéli puhányok, nyavalyások ha gyötör a láz,
fületek nyissátok gyorsan, hallgassátok, ű
amit most néktek, hallgassátok,
amit most néktek eldalol a ho-ho-ho nagy horgász.
"""

#1
szo=len(szoveg.split())
print("A horgász szó előfordulása a szövegben: ",szo)
#2
print("A horgász szó előfordulásainak száma: ",szoveg.count("horgász"))

#3
ho= szoveg.replace("ho-ho-ho","HO-HO-HO")
print(ho)

#4
szamok=['0','1','2','3','4','5','6','7','8','9']
szam=0
for sz in szoveg:
    if sz in szamok:
        szam +=1
            
print("Szövegben megtalálható számok száma: ", szam,"db")

#5

