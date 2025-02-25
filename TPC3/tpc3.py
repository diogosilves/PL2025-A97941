import re

file = open("./teste.md", "r", encoding="utf-8")

while line := file.readline():
    line = re.sub(r'### (.*)', r'<h3>\1</h3>', line)
    line = re.sub(r'## (.*)', r'<h2>\1</h2>', line)
    line = re.sub(r'# (.*)', r'<h1>\1</h1>', line)

    line = re.sub(r'(.*) \*(.*)\*', r'\1 <i>\2</i>', line)


    print(line, end="")