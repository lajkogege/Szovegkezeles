def szepnapvan():
    szoveg: str = "Szép nap van!"
    #Írd ki a szöveg első karakterét!
    print("1. ",szoveg[0])
    #Írd ki a szöveg masodik karakterét!
    print("2." ,szoveg[1])
    #Írd ki a szöveg hosszát karakterét!
    print("A hossz: " ,len(szoveg))
    #Írd ki a szöveg utolsó karakterét!
    print("utolsó", szoveg[len(szoveg)-1] )

    """ Ird ki a szöveg karaktereit egymás alá betünként"""

    i: int= 0
    while i < len(szoveg):
        print(szoveg[i])
        i+=1

def szovegkezeles():
    szoveg:str="Ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper())

    #Van-e a szövegben teszt szöveg?
    x:int= szoveg.find("teszt")
    if x> 0:
        print("Igaz")
    else:
        print("Hamis")

    #A SZOVEG változoban hol szerepel elöször a s betű?
    print(szoveg.index("s"), "helyen szerepel a betű")

    #Alakitsd át minden szó kezdöbetüjét nagybetüssé
    print(szoveg.title())

    #Cseréld ki a teszt szót probálra
    print(szoveg.replace("teszt", "próba"))

def aszoveg_visszafele(szoveg:str):
    #paraméterben kapott szöveg visszafelé kiírva egymás mellé a betű
    szoveg:str="Ez egy vissza felé irt szöveg"
    #print(szoveg[::-1]) csak pythonban müködik
    i:int = len(szoveg)
    while i!= 0: #i>=0
        print(szoveg[i-1], end ="")
        i-=1
def a_betuk_szama(szoveg:str):
    #Hány "a" betű van a szövegben?
    szoveg: str = "Ez egy rövid szöveg"
    #print(szoveg.count("a")) ---fügvénnyel
    i:int=0
    a_szamlalo:int=0
    while i < len(szoveg):
        if szoveg[i] == 'a':
            a_szamlalo +=1
        i+=1
    print("A betűk száma: ", a_szamlalo)

