class Kifejezes:
    muvelet = {
        "+":   lambda x,y: x+y,
        "-":   lambda x,y: x-y,
        "*":   lambda x,y: x*y,
        "/":   lambda x,y: x/y,
        "div": lambda x,y: x/y,
        "mod": lambda x,y: x%y
        }
    def __init__(self, sor):
        parameterek = sor.split(" ")
        self.elso     = int(parameterek[0])
        self.operator = parameterek[1]
        self.masodik  = int(parameterek[2])
        
    def sor(self):
        return f"{self.elso} {self.operator} {self.masodik}"
    
    def eredmeny(self):
        try:
            if self.operator in self.muvelet.keys():
                return self.muvelet[self.operator](self.elso,self.masodik)
            return "Hibás operátor!"
        except:
            return "Egyéb hiba!"

def keressTizzelOszthatot(kifejezesek):
    for kifejezes in kifejezesek:
        if kifejezes.elso % 10 == 0 and kifejezes.masodik % 10 == 0: return True

# Beolvasas
bemenet = open("kifejezesek.txt", "r", encoding="latin2").read().strip().split("\n")
kifejezesek = [Kifejezes(i) for i in bemenet]


#statisztika
statisztika = {
    "mod": 0,
    "/": 0,
    "div": 0,
    "-": 0,
    "*": 0,
    "+": 0
}
for kifejezes in kifejezesek:
    if kifejezes.operator in statisztika.keys():
        statisztika[kifejezes.operator] += 1

#feladatok
print(f"2. feladat: Kifejezések száma: {len(kifejezesek)}")
print(f"3. feladat: Kifejezések maradékos osztással: {statisztika['mod']}")
print("4. feladat: " + "Van ilyen kifejezés!" if keressTizzelOszthatot(kifejezesek) else "Nincs ilyen kifejezés!")
print("5. feladat: Statisztika")
for key in statisztika.keys():
    spaces = " "*(8-(len(key)-1))
    print(f"{spaces}{key} -> {statisztika[key]}")
    
loop = True
while loop:
    fhBemenet = input("7. feladat: Kérek egy kifejezést (pl.: 1 + 1): ")
    if fhBemenet == "vége":
        loop = False
        continue
    print(Kifejezes(fhBemenet).eredmeny())

print("8. feladat: eredmenyek.txt")
eredmenyek = open("eredmenyek.txt", "w")
for kifejezes in kifejezesek:
    eredmenyek.write(f"{kifejezes.sor()} = {kifejezes.eredmeny()}\n")
