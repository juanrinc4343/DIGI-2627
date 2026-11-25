resposta_p_defecte = "desconegut"

cotxe = {
"marca": "SEAT",
"model": "Ibiza",
"any": "2019",
}

cotxe["color"] = "vermell"
cotxe.pop("model")

print(cotxe.get("model", resposta_p_defecte))
print(cotxe["color"])




