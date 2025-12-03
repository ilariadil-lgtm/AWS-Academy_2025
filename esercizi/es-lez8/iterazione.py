utenti: dict[str, str] = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest",
}

for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")

chiave_esistente = "bob"
if chiave_esistente in utenti:
    print(f"{chiave_esistente} True")
else:
    print(f"{chiave_esistente} False")

for username in utenti.keys():
    print(username)
for ruolo in utenti.values():
        print(ruolo)