# 07/02/2025

# Autor
* A97941
* Diogo Filipe Oliveira da Silva

## TPC1: Somador on/off: criar um programa em Python

1. Proibido o uso de expressões regulares;
2. Um programa que some todas as sequências de digitos que encontre num texto
    * Sempre que encontrar a string "Off" ou "On" em qualquer combinação de maiusculas ou minusculas, o comportamento é desligado ou ligado;
    * Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.



### Solução Adquirida
Para a resolução deste problema, optei por ler todo o conteúdo do arquivo de uma vez, armazenando-o em uma string. 
Esta é convertida para minúsculas para garantir que as verificações de "on" e "off" sejam *case-insensitive*. 
Para controlar o estado da soma (ON ou OFF), uso uma variável booleana. Quando encontro a string "off", desativo a soma, e ao encontrar "on", ativo novamente. 
Caso encontre o caractere "=", é apresentado o valor acumulado até aquele momento.
A extração dos números ocorre percorrendo caractere por caractere. 
Quando um número é encontrado, ele é acumulado em uma string temporária (atual). Assim que um caractere que não seja um número aparece, 
a sequência acumulada é convertida em um inteiro e somada ao total, caso o estado da soma esteja ativado (ON).