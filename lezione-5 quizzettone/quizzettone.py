






def valida_scelta(scelta: str) -> bool:

    scelta_tmp = scwelta.upper()
    if scelta_tmp == "A" or scelta_tmp =="B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else:
        return False
    
def mostra_domanda() -> None:
    print( 
        
        """
          
          Chi parteciperà a Sanremo 2026?
          
          A. Nayt
          B. La nina
          C. Nilla Pizzi
          D. Rocco Papaleo
          
          """)