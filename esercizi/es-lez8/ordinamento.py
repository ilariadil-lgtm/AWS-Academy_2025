from typing import List

prezzi: List[float] = [45.5, 12.0, 78.3, 23.1, 56.7]

prezzi_originali = [45.5, 12.0, 78.3, 23.1, 56.7]
prezzi_ordinati = sorted(prezzi_originali)

massimo_valore = max(prezzi)
minimo_valore = min(prezzi)
presente = 23.1 in prezzi
"""contare prezzi maggiori di 50"""
prezzi_maggiori_50 = sum(1 for prezzo in prezzi if prezzo > 50)

print(prezzi_originali)
print(prezzi_ordinati)
print("Massimo valore:", massimo_valore)
print("Minimo valore:", minimo_valore)
print("23.1 è presente nella lista:", presente)
print("Numero di prezzi maggiori di 50:", prezzi_maggiori_50)