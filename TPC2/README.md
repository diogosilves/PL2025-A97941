# 14/02/2025

# TPC2: Análise de um dataset de obras musicais

1. Proibido o uso do módulo CSV do Python;
2. Um programa que leia o dataset, processe-o e crie os seguintes resultados:
   * Lista ordenada alfabeticamente dos compositores musicais;
   * Distribuição das obras por período: quantas obras catalogadas em cada período;
   * Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

## Autor
* A97941
* Diogo Filipe Oliveira da Silva

### Solução Adquirida

Para a resolução deste problema, comecei por abrir o ficheiro CSV e li a primeira linha para ignorar o cabeçalho, que contém os nomes das colunas.

A seguir, percorri o ficheiro linha a linha, utilizando uma expressão regular para separar os dados corretamente. 
Esta expressão assegura que a função *split* ignore os pontos e vírgulas (;) dentro de aspas, garantindo que os campos não sejam divididos incorretamente.

Durante esta travessia:
   * Os nomes dos compositores foram extraídos e armazenados numa lista.
   * Utilizei um dicionário (numeroDeObrasPorPeriodo) para contar o número de obras catalogadas em cada período.
   * Para armazenar os títulos das obras associadas a cada período, usei um dicionário (obrasPorPeriodo), onde cada período serve como chave e a respetiva lista de títulos como valor.

Por fim, ordenei a lista de compositores e também as listas de títulos de obras dentro de cada período para manter os dados organizados.