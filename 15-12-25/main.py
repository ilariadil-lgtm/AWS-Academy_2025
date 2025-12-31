
def is_lista_utente_filled(lista_utente: list[str]) -> bool: # controllo se la lista è piena
    if len(lista_utente) < 3: # la ricetta ha 3 ingredienti
        return True #   continua a chiedere
    else: # la lista è piena
        return False #   esci dal ciclo
    
def get_ingrediente_formattato(ingrediente: str) -> str: # formatta l'ingrediente
    if not ingrediente: #       controllo se è vuoto
        print("l'ingrediente non deve essere vuoto") #       messaggio di errore
        
    return ingrediente.lower().strip() #       ritorna l'ingrediente formattato
      
def get_input_from_utente(text: str) -> str: # prendi input dall'utente
    if not text: #   controllo se il messaggio è vuoto
        print("il non messaggio non deve essere vuoto") #   messaggio di errore
    print("*"*30) #   separatore
    return input(text) #   ritorna l'input dell'utente

def log_message(text: str, type: str) -> None: # logga un messaggio
   icon = None #    inizializza icona
   match type:  #   seleziona il tipo di messaggio
       case "ALERT":   #        messaggio di allerta
            icon = "⚠️" #        icona di allerta
       case "INFO": #        messaggio informativo
            icon = "✅" #        icona di informazione
   print(f"{icon} - {text}") #   stampa il messaggio con l'icona

def main() -> None: # programma principale
    log_message("Start del programma", "INFO") # logga l'inizio del programma

    lista_ricetta: list[str] = ["farina", "acqua", "lievito"] # lista degli ingredienti della ricetta
    lista_utente: list[str] = [] # lista degli ingredienti inseriti dall'utente
    
    while is_lista_utente_filled(lista_utente): # ciclo finchè la lista dell'utente non è piena
        ingrediente = get_input_from_utente("inserisci un ingrediente:") # prendi l'ingrediente dall'utente
        if not ingrediente: # controllo se l'ingrediente è vuoto
            log_message("l'ingrediente non deve essere vuoto", "ALERT") # messaggio di errore

        ingrediente_formattato: str = get_ingrediente_formattato(ingrediente) # formatta l'ingrediente

        if ingrediente_formattato in lista_ricetta: # controllo se l'ingrediente è nella ricetta

            if ingrediente_formattato in lista_utente: # controllo se l'ingrediente è già stato inserito
                print("ingrediente è nella ricetta") # messaggio di errore
            else: # l'ingrediente non è stato inserito
                lista_utente.append(ingrediente_formattato) # aggiungi l'ingrediente alla lista dell'utente


        else: # l'ingrediente non è nella ricetta
            print("ingrediente non valido") # messaggio di errore

    print("impasta e fai la pizza") # messaggio di successo
    print("end del programma") # logga la fine del programma

  

main() # esegui il programma principale