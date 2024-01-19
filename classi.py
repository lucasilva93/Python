class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età
    def stampare(self):
        print(f"nome: {self.nome}, cognome: {self.cognome}, età: {self.età}")   #f = f-string

PersonaA = Persona("Luca", "Silva", 30)     
PersonaA.stampare()   

class Libri:
    def __init__(self, titolo, autore, DataPubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.DataPubblicazione = DataPubblicazione
    
    def pubb(self):
        print(f"Il libro è:  {self.titolo}, di {self.autore}, pubblicato {self.DataPubblicazione}")
 
    def recente(self):
        AnnoP = int(self.DataPubblicazione.split("/")[-1])
        oggi = 2024
        return oggi - AnnoP < 5

libroA = Libri("Zanna Bianca", "White Fang" , "01/05/1906")         
recente = libroA.recente()
stmp =  libroA.pubb()
print(f"Il libro ha meno di 5 anni? {'Sì' if recente else 'No'}")


class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def circonferenza(self):
        diametro = self.raggio *2
        cc = diametro*3.14
        return cc

    
    def area(self):
        aa = 3.14*((self.raggio)**2)
        return aa
    
        
cerchio1 = Cerchio(50)
ccc = cerchio1.circonferenza()
aaa = cerchio1.area()
print(f"La Circonferenza del cerchio è : {ccc}")
print(f"L'Area del cerchio è: {aaa}")



class Conto_Bancario:
    def __init__(self, saldo, deposito):
        self.saldo = saldo
        self.deposito = deposito
    def depositare(self):
        tot = self.saldo + self.deposito
        return tot
    def prelievo(self):
        totale = self.saldo - self.deposito
        return totale

depositato = Conto_Bancario(5000,350)
prelevato = Conto_Bancario(3000,1200)
dep = depositato.depositare()
pre = prelevato.prelievo()
print(f"Il saldo del tuo c/c dopo il versamento è: {dep}")
print(f"Il saldo del tuo C/C dopo il prelievo è:  {pre}")



class Prodotto:
    def __init__(self, nome, prezzo, quantità):
        self.nome = nome
        self.prezzo = prezzo
        self.quantità = quantità

    def totale(self):
        costo_totale = self.prezzo*self.quantità
        return costo_totale
    
    def verifica_qtà(self):
        v = self.quantità
        if v != 0:
          return v
        else: 
             print("Prodotto non Disponibile")
    
prodotto1 = Prodotto("Lavatrice", 450, 5)
prodotto2 = Prodotto("Lavastovigle", 350, 7)
prodotto3 = Prodotto("Aspirapolvere", 400, 0)
pr1 = prodotto1.totale()
pr2 = prodotto2.totale()
pr3 = prodotto3.verifica_qtà()
pr4 = prodotto3.totale()
print(f"Il costo totale delle Lavatrici è: {pr1}")
print(f"Il costo totale delle Lavastoviglie è: {pr2}")
if pr3 is not None: 
     print(f"Il costo totale degli Aspirapolveri è: {pr3}")
if pr3 is not None:
    print(f"La disponibilità del prodotto è: {pr3}")


class Edifici:
    def __init__(self, metratura, piani, price):
        self.metratura = metratura
        self.piani = piani
        self.price = price
    def totA(self):
        areatot = self.metratura * self.piani
        return areatot
palazzo1 = Edifici(300, 4, 200000)
palazzo2 = Edifici(100, 2, 130000)
palazzo3 = Edifici(400, 6, 500000)    
pal1 = palazzo1.totA()
pal2 = palazzo2.totA()
pal3 = palazzo3.totA()
print(f"L'area dell'immobile totale è: {pal1}")
print(f"L'area dell'immobile totale è: {pal2}")
print(f"L'area dell'immobile totale è: {pal3}")

        


