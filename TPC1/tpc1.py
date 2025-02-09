ON = True
OFF = False

file = open("./text.txt","r",encoding="utf-8")
texto = file.read()
file.close()

count = 0
switch = ON
atual = ""

texto = texto.lower()

i = 0
while i < len(texto):
    char = texto[i]

    if char.isdigit():
        atual += char
    else:
        if atual:
            if switch == ON:
                count += int(atual)
            atual = ""

        if texto[i:i+2] == "on":
            switch = ON
            i += 1
        elif texto[i:i+3] == "off":
            switch = OFF
            i += 2
        elif char == "=":
            print(f"Valor acumulado: {count}")

    i += 1

if atual and switch == ON:
    count += int(atual)
    atual = ""
