def mostra_benvenuto(lista_spesa: list[str]) -> None:
    """Mostra il messaggio di benvenuto e la lista della spesa."""
    print("=== SUPERMERCATO DEL FUTURO 2050 ===")
    print("Carrello robotizzato attivo!")
    print(f"\nLista della spesa: {', '.join(lista_spesa)}")
    print(f"Numero di articoli da acquistare: {len(lista_spesa)}\n")


def chiedi_prodotto() -> str:
    """Chiede all'utente quale prodotto vuole prendere e restituisce l'input."""
    prodotto = input("Quale prodotto vuoi prendere? (scrivi 'esci' per uscire): ").strip().lower()
    return prodotto


def verifica_prodotto_in_lista(prodotto: str, lista_spesa: list[str], carrello: list[str]) -> bool:
    """
    Verifica se il prodotto può essere aggiunto al carrello.
    Restituisce True se il prodotto è stato aggiunto, False altrimenti.
    """
    if prodotto in lista_spesa:
        if prodotto in carrello:
            print(f"⚠️  ATTENZIONE: {prodotto} è già nel carrello!")
            return False
        else:
            carrello.append(prodotto)
            print(f"✅ CARRELLO APERTO! {prodotto} inserito nel carrello.")
            return True
    else:
        print(f"❌ CARRELLO BLOCCATO! {prodotto} non è nella tua lista della spesa!")
        print("Il carrello robotizzato si rifiuta di aprirsi.")
        return False


def trova_elementi_mancanti(lista_spesa: list[str], carrello: list[str]) -> list[str]:
    """Restituisce la lista degli elementi che mancano nel carrello."""
    return [item for item in lista_spesa if item not in carrello]


def verifica_spesa_completa(lista_spesa: list[str], carrello: list[str]) -> None:
    """Verifica se la spesa è completa e mostra il messaggio appropriato."""
    print("\n" + "="*50)
    
    if len(carrello) == len(lista_spesa):
        elementi_mancanti = trova_elementi_mancanti(lista_spesa, carrello)
        
        if not elementi_mancanti:
            print("🎉 PERFETTO! Hai preso tutti gli articoli della lista!")
            print(f"Carrello completo: {', '.join(carrello)}")
            print("\n🛒 CARRELLO APERTO - Puoi procedere alla cassa!")
        else:
            print("⚠️  Hai lo stesso numero di articoli ma qualcosa non va...")
            print(f"Mancano: {', '.join(elementi_mancanti)}")
    else:
        elementi_mancanti = trova_elementi_mancanti(lista_spesa, carrello)
        print("⚠️  Non hai completato la spesa!")
        print(f"Articoli nel carrello: {len(carrello)}/{len(lista_spesa)}")
        print(f"Mancano ancora: {', '.join(elementi_mancanti)}")
        print("\n🚫 CARRELLO BLOCCATO - Completa la lista per procedere!")


def main():
    # Lista della spesa - gli alimenti da acquistare
    lista_spesa: list[str] = ["pasta", "pane", "frutta", "verdura", "nutella"]
    carrello: list[str] = []
    
    # Mostra il benvenuto
    mostra_benvenuto(lista_spesa)
    
    # Ciclo per inserire gli elementi
    while len(carrello) < len(lista_spesa):
        print(f"\nArticoli nel carrello: {len(carrello)}/{len(lista_spesa)}")
        
        # Chiedi il prodotto all'utente
        prodotto = chiedi_prodotto()
        
        # Controllo input vuoto
        if not prodotto:
            print("❌ ERRORE: Non hai inserito nessun prodotto!")
            continue
        
        # Opzione per uscire
        if prodotto == "esci":
            print("\n🚪 Uscita dal programma...")
            break
        
        # Verifica e aggiungi il prodotto al carrello
        verifica_prodotto_in_lista(prodotto, lista_spesa, carrello)
    
    # Verifica finale della spesa
    verifica_spesa_completa(lista_spesa, carrello)
    
    print("\n👋 Grazie per aver usato il Supermercato del Futuro!")


if __name__ == "__main__":
    main()
