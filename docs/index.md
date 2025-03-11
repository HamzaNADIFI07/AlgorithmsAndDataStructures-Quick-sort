# TP tri rapide


## État du TP

Décrivez ici l'état d'avancement du TP.

## Réponses aux questions

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous indiquerez :

### À propos des tableaux NumPy

Après avoir lancer **l'interpréteur Python** avec la commande `python3`, j'ai pu me familiariser avec les tableaux **NumPy**, avec les instructions suivantes:

```python
>>> import numpy as np
>>> tab = np.array([i for i in range(10)])
>>> tab
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> tab[0]
0
>>> tab[-1]
9
>>> len(tab)
10
>>> for i in tab:
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
```

### Rappels sur le tri rapide

#### Q1:

Parmi les algorithmes de tris qui opte une approche de tri sur place, on a:

- Tri à bulles.
- Tri par insertion.
- Tri par sélection.
- Tri par tas.

#### Q2:

Pour partitionner un tableau sans avoir à utiliser de l'espace mémoire supplémentaire, il faut faire des **échanges** d'éléments.

#### Q3:

Afin de déterminer que le partitionnement est correctement réalisé, il faut que:

- La longueur des deux partitions soit égale à celle du tableau initial passé en paramètre.

- Le premier élément `(le pivot)` du deuxième tableau partitionné soit **strictement supérieur** à tous ceux du première tableau, mais aussi **inférieur ou égal** aux éléments du second tableau.

#### Q4:

Après avoir tester nos exemples implémentés dans la **doctest** de la fonction `partition`, avec la commande 
```bash
python3 sorting.py
```
On constate que tous les tests ont réussi avec succès.

#### Q9:

Le tri rapide est un algorithme récursif, donc la mémoire supplémentaire utilisée est due à la pile des appels récursifs, ainsi que le nombre de ces appels récursifs est influencé par le choix du pivot.

##### La complexité asymptotique en espace dans le meilleur des cas **(log n)**:
Dans le meilleur des cas, le **pivot** est au milieu du tableau, donc à chaque étape, le tableau est divisé en deux moitiés,

Ce qui nous donne une **complexité asymptotique en espace** de:

```math
O(log n)
```

##### La complexité asymptotique en espace dans le pire des cas **(n)**:
Dans le pire des cas, le **pivot** est toujours le plus petit ou le plus grand élément, car dans ce cas à chaque étape de résursion, on ne tri qu'un seul élement du tableau, donc chaque appel ne réduit la taille du tableau que d’un seul élément.

Ce qui nous donne une **complexité asymptotique en espace** de:

```math
n
```
