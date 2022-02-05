
import os
import qrcode

print("This is a simple QR-Code generator!")
directorys = os.listdir() #Creo una lista con dentro i valori di tutte le directory


if not "qr-codes" in directorys: #Se nella lista dei file non è presenta una cartella chiamata "qr-codes":
    os.makedirs("qr-codes") #Creala
    os.chdir(os.getcwd()+'\qr-codes') #Mi sposto di directory tramite la funziona os.chdir() , con il parametro os.getcwd() ottengo la directory attuale e aggiungo la cartella qrcode
else: #Se nella lista directorys è già presente la cartella qr-codes:
    os.chdir(os.getcwd()+'\qr-codes') #Spostati

while True:
    link = str(input("Inserire il link --> ")) #Prendo l'input del link che l'utente vuole convertire:
    img = qrcode.make(link) #Convertisco l'input dell'utente in qrcode

    name = input("Salvare il qr-code come [Inserire un nome]--> ") #Chiedo all'utente con quale nome vuole salvare il qr-code
    print(f"Immagine salvata in {os.getcwd()}") # Comunico dove è stata salvata l'immagine
    img.save(name+".png") #Salvo l'immagine con l'estensione .png
        
    
    answer = input("Wanna continue ? Y or N --> ")
    if answer == "Y" or answer == "y":
        continue
    else:
        break
