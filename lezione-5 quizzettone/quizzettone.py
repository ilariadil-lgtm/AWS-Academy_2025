"""
mostra_domanda() (senza return)
    * Non prende parametri
    * Stampa la domanda e le 4 opzioni
    * Non restituisce nulla

raccogli_risposta() (con return)
    * Non prende parametri
    * Chiede l'input all'utente
    * Converte in int
    * Restituisce l'opzione scelta

valida_scelta(scelta) (con return)
    * prende come parametro il numero scelto
    * Verifica se è tra A,b,c d usando if
    * Restituisce True se valida, False altrimenti
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

mostra_domanda()

risposta_da_validare: str = raccogli_risposta()
risposta_validata: bool= valida_scelta(risposta_da_validare)

print(risposta_validata)