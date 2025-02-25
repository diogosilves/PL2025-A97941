import re

file = open("./teste.md", "r", encoding="utf-8")

while line := file.read():
    #Header
    line = re.sub(r'### (.*)', r'<h3>\1</h3>', line)
    line = re.sub(r'## (.*)', r'<h2>\1</h2>', line)
    line = re.sub(r'# (.*)', r'<h1>\1</h1>', line)

    #Italic
    line = re.sub(r'(.*) \*(.*)\*', r'\1 <i>\2</i>', line)

    #List
    line = re.sub(r'((?:^\d+\.\s.*\n?)+)',
                     lambda m: '<ol>\n' + ''.join(f'  <li>{item.strip()}</li>\n'
                     for item in
                        re.findall(r'^\d+\.\s*(.*)', m.group(0), re.MULTILINE)) + '</ol>\n',
                     line, flags=re.MULTILINE)

    # Image path
    line = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1">', line)

    #Link
    line = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', line)

    print(line)

    file1 = open("./output.html", "w+", encoding="utf-8")
    file1.write("<!DOCTYPE html>\n<html>\n<body>\n")
    file1.write(line)
    file1.write("\n</body>\n</html>")
