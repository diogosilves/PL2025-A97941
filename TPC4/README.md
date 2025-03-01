# 01/03/2025

## TPC4: Analisador Léxico

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:
```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```


### Solução Adquirida

* A97941
* Diogo Filipe Oliveira da Silva