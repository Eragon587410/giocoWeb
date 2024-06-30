from ast import While
from timeit import repeat


print("Benvenuto")
print("Inserire nome giocatore")
nome_giocatore = input()
print("Player: "+nome_giocatore)
print("Digita start per iniziare")
if input() == "start":
    print("Caricamento dati di gioco")
    print("Seleziona la difficoltà : difficile, media, facile")
    difficoltà = input()
    # Difficoltà Facile
    # Difficoltà Media
    if difficoltà == "media":
        print("Hai selezionato la difficoltà media")
    # Difficoltà Difficile
    if difficoltà == "difficile":
        print("Hai selezionato la difficoltà difficile")
       


