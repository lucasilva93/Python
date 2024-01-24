
def menu() -> int:
    print("1. Aggiungi")
    print("2. Elenca")
    print("0. Esci")

    r = -1
    while r != 0 and r != 1 and r != 2:
        try:
            r = int(input("Scegli l'operazione: "))
        except:
            r = -1
    return r


# l'utente potrà aggiungere numeri alla rubrica
# quindi ci serve una rubrica!
rubrica = []

# l'aggiunta dei numeri dovrà prevedere la digitazione del nome
# e del numero di telefono associato


def inserisci():
    nome = input("Nome: ")  # chiede il nome all'utente
    telefono = input("Numero di telefono: ")  # chiede il numero di telefono
    return nome, telefono  # restituisce la tupla (nome, numero)

# la visualizzazione dovrà prevedere la stampa della rubrica
def visualizza():
    for i in rubrica:
        print("Nome:", i["nome"], "Telefono", i["telefono"])


# implementazione della persistenza su file
file_rubrica = "./rubrica.txt"  # nome del file

# salva le informazioni su un file di testo
def salva(nome_file: str):
    with open(nome_file, "w") as f:
        f.writelines([e["nome"] + ';' + e["telefono"] + '\n' for e in rubrica])

# legge le informazioni da un file di testo
def leggi(nome_file: str):
    with open(nome_file, "r") as f:
        lines = f.readlines()  # legge le righe per intero
    # divide ogni riga in base alla presenza di un carattere ;
    elab = [l.strip().split(';') for l in lines]
    #      trasforma le liste ottenute in precedenza creando per ogni riga un dict
    return [{'nome': l[0], 'telefono': l[1]} for l in elab]


rubrica = leggi(file_rubrica)
scelta = -1
while scelta != 0:
    scelta = menu() # l'utente sceglie una voce del menu
    if scelta == 1:
        nome, numero = inserisci()  # qui ottengo ciò che l'utente ha inserito
        # lo aggiungo alla rubrica
        rubrica.append({'nome': nome, 'telefono': numero})
        salva(file_rubrica)
    elif scelta == 2:
        visualizza()



# voglio leggere questo file
file_name = "./elenco-comuni.csv"


def load(fn: str):
    with open(fn, "r", encoding="latin-1") as f:
        lines = f.readlines()  # leggo tutte le linee dal file
        #         sesto campo        quindicesimo
    return [{'city': l[5], 'acronym': l[14]}
            # prendo tutte le liste create dall'istruzione successiva
            for l in
            # pulisco la stringa e creo
            # una lista considerando il
            # separatore ;
            #       |             a partire dalla quarta riga
            #       |             per saltare le intestazioni
            #       |                        |
            #       V                        V
            [s.strip().split(';') for s in lines[3:]]]


cities = load(file_name)
print(cities[:10]) # prime 10 città
print("Quante città in archivio?", len(cities))
print("Quante città in provincia di Roma?",
      len([x for x in cities if x['acronym'] == 'RM']))
print("Quante città il cui nome inizia per A?",
      len([x for x in cities if x['city'].startswith('A')]))
print("Tutte le città il cui nome inizia per 'bo':",
      [c for c in cities if c['city'].lower().startswith('bo')])


import numpy as np
mia_lista = np.array([1,2,3,4,5,6])
print(type(mia_lista))

print(np.arange(-10,10,2))
print(np.linspace(0,100,5))
print(mia_lista.argmin())
print(mia_lista.argmax())
print(mia_lista.reshape(3,2))

matrice = np.array([[10,11,12,13],[20,21,22,23],[30,31,32,33]])
print(matrice)
print(matrice[0][1])
print(matrice[:,1:])
print(matrice.size)
print(matrice + 6)
nn = [1, 2, 3, 5, 33, 40, 50, 75]
c = np.concatenate([mia_lista, nn])
print(c)
print(np.vstack(nn))
print(np.hstack(nn))
print(np.split(c, [6,10]))


import numpy as np
rivetti = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
lunghezza = 28.75
buchi = lunghezza/14
arrot = np.round(buchi,2)
print(np.arange(0,14,arrot))

linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3, 3, 3))
print(reshaped_data)



import numpy as nd
rows, cols = 3,4
matrix = nd.zeros((rows, cols), dtype = int)

matrix[0, 0] = 1
matrix[0, 1] = 1
matrix[0, 2] = 1
matrix[0, 3] = 1
matrix[1, 0] = 5
matrix[1, 1] = 1
matrix[1, 2] = 1
matrix[1, 3] = 1
matrix[2, 0] = 20
matrix[2, 1] = -4
matrix[2, 2] = 0
matrix[2, 3] = 42

print(matrix)





import numpy as np
tabella = np.array([[10,22,21,8,9],[9,42,3,18,11],[5,4,30,12,29],[37,31,7,2,26],[8,6,4,33,15]])
min = tabella.min()
max = tabella.max()
print(min)
print(max)
tabella1 = tabella - min
tabella2 = ((tabella1/max) - min)
tabella3 = np.round(tabella2, 3)
print(tabella1)
print(tabella3)

