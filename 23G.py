# Scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'è altra strada che quella
# di prevedere una traduzione semplice attraverso una tabella:
# 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilità di prevedere
# una "traduzione" della decina e demandare la "traduzione"
# dell'unità alla funzione che traduce fino a 20
# 25 -> decina = 2, unità = 5


def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unità di n
    return DECADES[decade-2] + translate_to_20(unit)

def translate_to_1000(n):
    if n < 100:
        return translate_to_100(n)
    if n > 99:
        return "Out of range"
    DECADES = ["cento", "duec", "trec", "qc", "5c",
               "6c", "7c", "8c"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unità di n
    return DECADES[decade-2] + translate_to_100(unit)

def translate_number(n):
    return translate_to_1000(n)

for x in range(1, 1001):
    print(translate_number(x))