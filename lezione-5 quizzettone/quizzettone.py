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
    
def mostra_domanda() -> None:
    """Stampa la domanda e le opzioni di risposta."""
 
    print(  """
          Chi parteciperà a Sanremo 2026?
          
          A. Nayt
          B. La nina
          C. Nilla Pizzi
          D. Rocco Papaleo

          """)

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
    
def genera_feedback(scelta:str) -> str:
     """Restituisce il messaggio che indica all'utente se ha indovinato o meno. Questa funzione viene eseguita solo se la funzione di validazione restituisce True. """
     if scelta.upper == "A":
          return "Hai indovinato!"
     else:
          return "Non hai indovinato, peccato ritenta"
     
def mostra_feedback(messaggio: str) -> None:
    """Stampa il messaggio di feedback in modo formattato."""
    simbol: str = "*"*30
    print(f"""
          {simbol}
          {messaggio}
          {simbol}
        """)

def main():
    mostra_domanda()
    risposta_da_validare: str = raccogli_risposta()
    risposta_validata: bool= valida_scelta(risposta_da_validare)
    feedback: str = ""
    if risposta_validata == True:
     feedback = genera_feedback(risposta_da_validare)
    else:
     feedback = "Inserisci solo le opzioni elencate"

    mostra_feedback(feedback)

# Entry point del programma
main()