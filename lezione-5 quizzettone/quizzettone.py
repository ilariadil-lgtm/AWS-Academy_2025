"""
mostra_domanda() (senza return)
- Non prende parametri
- Stampa la domanda e le 4 opzioni
- Non restituisce nulla

raccogli_risposta() (con return)
- Non prende parametri
- Chiede l'input all'utente
- Converte in int
- Restituisce l'opzione scelta

valida_scelta(scelta) (con return)
- prende come parametro il numero scelto
- Verifica se è tra A,b,c d usando if
- Restituisce True se valida, False altrimenti

genera_feedback(scelta) (con return)
- Prende come parametro la lettera che è stata scelta 
- Usa if/elif/else per determinare il messaggio
- Restituisce la stringa con il feedback personalizzato

mostra_feedback(messaggio) (senza return)
- Prende come parametro una stringa
- Stampa il feedback in modo formattato
- Non restituisce nulla
"""
    
def mostra_domanda(domanda: str) -> None:
    """Stampa la domanda e le opzioni di risposta."""
 
    print( domanda)
    
def leggi_file() -> None:
    with open("domande.txt", "r") as file:
        content = file.read()
        return content      

def estrai_index(content: str) -> int:
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    return  content[0:index]
    
def estrai_risposta(content: str, index: int) -> str:
    return content[index+1:]

def raccogli_risposta() -> str:
        """Chiede all'utente di inserire la proprio scelta e la restituisce."""
        return input("Inserisci la tua scelta:")

def valida_scelta(scelta: str) -> bool:
    """ Verifica se la scelta è valida (A,B,C,D) e restituisce True o False."""
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp =="B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else:
        return False
    
def genera_feedback(scelta:str, is_risposta_corretta: bool) -> str:
     """Restituisce il messaggio che indica all'utente se ha indovinato o meno. Questa funzione viene eseguita solo se la funzione di validazione restituisce True. """
     if scelta.upper() == "A":
          return "Hai indovinato!"
     else:
          return "Non hai indovinato, peccato ritenta"
     
def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False

is_risposta_corretta = False     
def mostra_feedback(messaggio: str) -> None:
    """Stampa il messaggio di feedback in modo formattato."""
    simbol: str = "*"*30
    print(f"""
          {simbol}
          {messaggio}
          {simbol}
        """)
    
def main():
    content: str = leggi_file()
    index: int = estrai_index(content)
    domanda: str = estrai_domanda(content, index)
    risposta: str = estrai_risposta(content, index)

    is_risposta_corretta: bool = False
    while True:
        mostra_domanda(domanda)
        risposta_da_validare: str = raccogli_risposta()
        risposta_validata: bool = valida_scelta(risposta_da_validare)
        feedback: str = ""

        if risposta_validata == True:
            print(f"sono qui: {risposta}")
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, risposta)
            feedback = genera_feedback(risposta_da_validare, is_risposta_corretta)
        else: 
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
        if is_risposta_corretta == True: 
            break

# Entry point del programma
main()