# 25/02/2025

## TPC3: Conversor de MarkDown para HTML

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic
Syntax" da Cheat Sheet:
   - **Cabeçalhos:** linhas iniciadas por "# texto", ou "## texto" ou "### texto" In: # Exemplo Out: < h1 > Exemplo < /h1 >
   - **Bold:** pedaços de texto entre "**": In: Este é um exemplo ... Out: Este é um exemplo ... 
   - **Itálico:** pedaços de texto entre "*": In: Este é um exemplo ... Out: Este é um exemplo ... 
   - **Lista numerada:**

     In:
     1. Primeiro item
     2. Segundo item
     3. Terceiro item
     
     Out: < ol > < li >Primeiro item< /li> < li >Segundo item< /li> < li >Terceiro item< /li> < /ol>
   - **Link:** \[texto](endereço URL) In: Como pode ser consultado em página da UC Out: Como pode ser consultado em página da UC 
   - **Imagem:** !\[texto alternativo](path para a imagem) 

     In: Como se vê na imagem seguinte: ! \[imagem dum coelho] (http://www.coellho.com) ... 

     Out: Como se vê na imagem seguinte: < img src="http://www.coellho.com" alt="imagem dum coelho"/> ...

### Solução Adquirida
Esta solução foi implementada utilizando expressões regulares para identificar e converter as linhas escritas em markdown.
Foram aplicadas as regras de conversão:
- **Cabeçalhos:** Foram definidas expressões regulares para os diferentes níveis de cabeçalhos ("# ", "## ", "### "), convertendo-os nas respetivas tags HTML \<h1>, \<h2> e \<h3>.
- **Texto em Itálico:** (\*exemplo*), foi convertido para a tag \<i> no HTML. 
- **Listas Numeradas:** Utilizando uma expressão regular e uma função lambda, cada item numerado foi encapsulado na tag \<li> e o conjunto dentro de \<ol>. 
- **Imagens:** Os padrões de imagem no Markdown (!\[alt](path)) foram transformados na tag \<img> correspondente, mantendo o texto alternativo e o caminho da imagem. 
- **Links:** Da mesma forma, os links no formato Markdown (\[texto](URL)) foram convertidos em tags \<a> no HTML.

Para cada uma das regras de conversão foi utilizado o re.sub() para substituir os padrões identificados pelo respetivo código HTML.
# Autor
* A97941
* Diogo Filipe Oliveira da Silva