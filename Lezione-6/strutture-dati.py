"""Liste in Python"""
"""
stringhe: list[str | int] = ["Pippo", 10, "Paperino", 20, "Minnie"]

stringhe.append("Pluto")
stringhe.append("Topolino")
stringhe.pop(2)
stringhe.remove("Pippo")

deleted_values: list[str] = []  

value_to_check_and_delete: str = "Pluto"

is_value_in_the_list: bool = value_to_check_and_delete in stringhe

if is_value_in_the_list == True:
        index_Value_to_delete = stringhe.index(value_to_check_and_delete)
        deleted_value = stringhe.pop(index_Value_to_delete)
        deleted_values.append(deleted_value)
else:
        print(f"{value_to_check_and_delete} Il valore non è presente nella lista {stringhe}")


#index_Value_to_delete = stringhe.index(value_to_check_and_delete)

#deleted_value = stringhe.pop(index_Value_to_delete)

#deleted_values.append(deleted_value)

print("*"*30)
print(stringhe)
print(deleted_values)
#print(index_Value_to_delete)
#print(is_value_in_the_list)

"""


"""Dizionari in Python"""

personaggio1: dict[str, str ] = {
    "Nome": "Pippo",
    "tipo": "cane",
    "email": "pippo@disney.com"
}

personaggio2: dict[str, str ] = {
    "Nome": "Paperino",
    "tipo": "anatra",
    "email": "paperino@disney.com"
}

personaggi:list [dict[str, str]] = [personaggio1, personaggio2]

print(personaggi[1].get("tipo"))

del personaggio1["tipo"]

for x in personaggi:
    if x.get("tipo") == "anatra":
        x["tipo"] = "papero"

print(x)
""""
print(personaggio1["email"])

personaggio1["telefono"] = "0922 33183"
personaggio1["telefono"] = "0922 - 33183"

personaggio1["Nome"]= "Minnie"

print(personaggio1.get("telefono"))

for chiave,valore in personaggio1.items():
    print(f"{chiave} : {valore})")
"""