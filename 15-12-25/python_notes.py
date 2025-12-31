"""

input -> programma -> generiamo un output

Tipi di intput:
- file che si trovano nel file system (sono già dentro il computer);
    open("nomefile", "r")
- input da parte dell'utente;
- dati che vengono da altri computer sulla rete

Tipi di output:
- file che si trovano nel file system (sono già dentro il computer);
    open("nomefile", "w")
- output UI;
- dati che vengono mandati ad altri computer

programma == set di instruzioni

"""

""" === PROGRAMMA PER FARE LA PIZZA ===
- Obiettivo
Realizzare un programma che prenda gli ingredienti per fare la pizza dall'utente, attraverso input testuale e restituisce il risultato finale a schermo. 
Il computer non sa fare la pizza, quindi dobbiamo istruirlo noi. 

- Passi:
1. prendi gli ingredienti da utente (interagisci con l'utente) (input) -> if/else per controllare input -> output
2. - prendi farina
3. - prendi acqua 
4. - prendi lievito 

-- Cosa mi serve:
- input  
    - perchè voglio prendere gl ingredienti dall'utente
- lista ingredienti ricetta
- lista ingredienti inseriti dall'utente
- if/else
    - input è vuoto?
    - caretteri piccoli
    - controllo che l'ingrediente sia nella lista degli ingredienti
    - controllo che l'ingrediente non sia già stato inserito
    - se l'ingrediente passa i controlli aggiungu alla lista
    - altrimenti restituisce errore e poi input
- if/else 
    - se la lista degli ingredienti ricetta == alla lista degli ingredienti inserita dall'utente allora impasti 
        - gli ingredienti sono tre?
        - controllo con un ciclo for quali sono gli ingredienti che mancano
    - altrimenti riproponi input con messaggui degli ingredienti che mancano
    
    
------ qui qualcosa potrebbe andare storto perchè l'utente probabilmente protrebbe inserire gli ingredienti sbagliati ------

5. impasta la pizza
6. prendi la pallina
7. prendi pomodoro 
8. prendi mozzarella 
9. metti pomodoro 
10. metti mozzarella 
11. metti in forno la pizza
12. esci la pizza

"""
def main():
    return