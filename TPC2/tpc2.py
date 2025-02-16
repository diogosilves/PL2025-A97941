import re


file = open("./obras.csv", "r", encoding="utf-8")
cleanheader = file.readline()

compositores = []
numeroDeObrasPorPeriodo = {}
obrasPorPeriodo = {}


while line := file.readline():
    reg = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    nome = f"{reg[4]}"
    compositores.append(nome)
    periodo = f"{reg[3]}"
    numeroDeObrasPorPeriodo[periodo] = numeroDeObrasPorPeriodo.get(periodo, 0) + 1
    titulo = f"{reg[0]}"
    obrasPorPeriodo[periodo] = obrasPorPeriodo.get(periodo, []) + [titulo]


compositores.sort()
for periodo in obrasPorPeriodo:
    obrasPorPeriodo[periodo].sort()

print(compositores)
print(numeroDeObrasPorPeriodo)
print(obrasPorPeriodo)