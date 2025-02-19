import re


file = open("./obras(1).csv", "r", encoding="utf-8")
cleanheader = file.readline()

compositores = []
numeroDeObrasPorPeriodo = {}
obrasPorPeriodo = {}

count = 0
while line := file.readline():
    reg = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    while len(reg) <7:
        newLine = file.readline().strip()
        if not newLine:
            break
        line += " " + newLine
        reg = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)

    count += 1
    nome = f"{reg[4]}"
    compositores.append(nome)
    periodo = f"{reg[3]}"
    numeroDeObrasPorPeriodo[periodo] = numeroDeObrasPorPeriodo.get(periodo, 0) + 1
    titulo = f"{reg[0]}"
    obrasPorPeriodo[periodo] = obrasPorPeriodo.get(periodo, []) + [titulo]



compositores.sort()
for periodo in obrasPorPeriodo:
    obrasPorPeriodo[periodo].sort()

print(count)
print(compositores)
print(numeroDeObrasPorPeriodo)
print(obrasPorPeriodo)


