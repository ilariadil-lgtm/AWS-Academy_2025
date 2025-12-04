#!/usr/bin/env python3
server: list[str] = ["web01", "db01", "cache01"]

server.append("backup01")
server.insert(0,"proxy01")
server.remove("cache01")

print(server)
print(lunghezza := len(server))

#esercizio corretto

