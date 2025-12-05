"""
Modifica la funzione mostra_domanda o il ciclo main affinché, 
prima del testo della domanda, venga stampato il numero della domanda corrente e il numero totale delle domande.

"""

def mostra_domanda(domanda: str) -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    
    print(domanda)

def raccogli_risposta() -> str:
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente. 
    Il controllo di tale valore avverrà attraverso una funzione dedicata.
    """ 
    return input("Inserisci la tua scelta: ")

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else: 
        return False
    
def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione di validazione restituisce true. 
    """
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato."
    
def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata.
    """
    simbol: str = "*"*30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")
    
def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    """Verifica se la risposta scelta dall'utente è corretta confrontandola con la risposta esatta."""
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False
    
def leggi_file(file_path: str) -> str:
    """Legge il contenuto di un file e lo restituisce come stringa."""
    with open(file_path, "r") as file:
        content = file.read()
        return content

def estrai_index(content: str) -> int: 
    """Estrae l'indice del carattere speciale '£' all'interno del contenuto."""
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    """Estrae la domanda dal contenuto fino all'indice specificato."""
    return content[0:index]

def estrai_risposta(content: str, index: int) -> str:
    """Estrae la risposta dal contenuto a partire dall'indice specificato."""
    return content[index+1:]

def estrai_lista_domande(file_path: str) -> list[str]:
    """
    Estrae la lista delle domande da un file di testo.
    Restituisce una lista di stringhe, ciascuna rappresentante il nome di un file di domanda.
    """
    lista_domande: list[str] = []
    with open(file_path, "r") as f:
        for i in f:
            lista_domande.append(i.strip())
    return lista_domande 

def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
    """
    Genera le statistiche finali basate sui risultati ottenuti.
    Restituisce un dizionario con il conteggio delle risposte esatte e non esatte.
    """
    statistica: dict[str, int] = {}

    risposte_esatte: int = 0
    risposte_non_esatte: int = 0

    for i in risultato_finale: 
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1

    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_non_esatte"] = risposte_non_esatte
    return statistica

def main():
    """
    Funzione principale che gestisce il flusso del quiz.
    Questa funzione coordina l'estrazione delle domande, la raccolta delle risposte,
    la validazione, il feedback e la generazione delle statistiche finali.
    """
    lista_domande: list[str] = []
    risultato_finale: list[dict[str, str | bool]] = []
    domanda_e_risposta: dict[str, str] = {"domanda" : None, "risposta" : None}
    lista_domande = estrai_lista_domande("domande.txt")

    counter_domanda_corrente: int = 0

    lista_domande_length: int = len(lista_domande)

    while counter_domanda_corrente < lista_domande_length:
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index: int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        mostra_domanda(domanda_e_risposta["domanda"])

        risposta_utente: str = raccogli_risposta()

        is_risposta_valid: bool = valida_scelta(risposta_utente)

        feedback: str = ""

        if is_risposta_valid:
            risultato: dict[str, str | bool] = {}
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])
            feedback = genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            risultato_finale.append(risultato)
            counter_domanda_corrente += 1
        else: 
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)

    statistiche: dict[str, int] = genera_statistiche(risultato_finale)

    print(statistiche["risposte_esatte"])
    print(statistiche["risposte_non_esatte"])   


# Entry point del nostro programma
main()