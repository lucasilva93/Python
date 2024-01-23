def values(numbers, k):
    idonei = []
    for numero in numbers:
        if numero >= k:
            idonei.append(numero)
      
    if not idonei: 
        print("Nessun numero disponibile.")
        return None

    media = sum(idonei) / len(idonei)
    return media

nn = [1, 2, 3, 5, 33, 40, 50]
k = 55
ris = values(nn, k)

print("Media dei numeri maggiori o uguali a k:", ris)      