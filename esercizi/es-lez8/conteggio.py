voti: list[str] = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
conteggio: dict[str, int] = {}

for v in voti:              
    if v in conteggio:
        conteggio[v] += 1
    else:
        conteggio[v] = 1

print(conteggio)          
