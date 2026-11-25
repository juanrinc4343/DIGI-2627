resposta_p_defecte = "desconegut"

cotxe = {
"marca": "SEAT",
"model": "Ibiza",
"any": "1990",
}

print(cotxe["marca"])
print(cotxe.get("potencia", resposta_p_defecte))


