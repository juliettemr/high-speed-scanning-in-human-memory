# High speed scanning in human memory

Lien vers l'article: https://sdrive.cnrs.fr/s/wkBw2son3BYGLsw?dir=undefined&path=%2Fresources%2FArticles&openfile=326432908
Lien vers le github: https://github.com/juliettemr/high-speed-scanning-in-human-memory/

## Description générale

Dans cet article, Saul Sternberg cherche à déterminer comment nous retrouvons un item stocké en mémoire à court terme:

-> Parcourons-nous mentalement chaque élément un à un ?

-> Comparons-nous tous les éléments en parallèle ?

Pour répondre à ces questions, il mesure le temps de réaction nécessaire pour décider si un chiffre présenté appartient ou non à un ensemble de chiffres mémorisés juste avant, à l'aide de deux expériences.

## Expérience n°1

### Objectif

Mesurer le temps de réaction lors d’une tâche de reconnaissance d’un chiffre appartenant ou non à une liste précédemment mémorisée.

### Structure

L'expérience comporte 24 séries d'entraînement et 144 séries test.

### Déroulé d'une série

1 à 6 chiffres apparaissent un par un à l'écran.

Après deux secondes de pause, un signal sonore indique l'apparition d'un chiffre test. Le sujet doit déterminer si ce chiffre appartenait à la liste, les deux possibilités étant équiprobables.

Le temps de réaction du sujet est enregistré.

Un système de feedback encourage le sujet à donner des réponses exactes.

## Expérience n°2

### Objectif

Tester la recherche en mémoire pour des ensembles fixes, en comparant des tailles d’ensemble différentes.

### Structure

L’expérience comporte trois parties, correspondant à trois tailles d’ensemble :

| Partie | Taille de l'ensemble | Exemple d’ensemble |
| ------ | ---------------------| ------------------ |
| 1      | 1                    | {1}                |
| 2      | 2                    | {2, 3}             |
| 3      | 4                    | {4, 5, 6, 7}       |

### Déroulement d’une partie

Annonce des chiffres à mémoriser.

60 séries d’entraînement.

120 séries de test.

### Déroulement d'une série

Un signal sonore indique l'apparition d'un chiffre test. Le sujet doit déterminer si ce chiffre appartenait à la liste, le OUI étant de probabilité fixe (4/15) entre les trois parties.

Le temps de réaction du sujet est enregistré.

Un système de feedback encourage le sujet à donner des réponses exactes.

## Résultats

Les résultats indiquent que le temps de réaction est proportionnel au nombre d'éléments dans la liste. Sternberg en conclut que la mémoire à court terme est explorée par un mécanisme séquentiel exhaustif impliquant une comparaison système par système, à vitesse constante.

## À vous !

Pour tester l'expérience, vous pouvez utiliser les commandes suivantes :

```
git clone git@github.com/juliettemr/high-speed-scanning-in-human-memory.git
cd high-speed-scanning-in-human-memory
python -m .venv venv
.venv\Scripts\activate.bat sur windows .venv/bin/activate sur linux/mac
pip install -r requirements.txt
python high-speed-scanning.py
```

Le nombre de séries étant conséquent dans l'expérience, il est conseillé de modifier les lignes `l7`, `l8`, `l12` et `l13` de `high-speed-scanning.py` pour une démonstration.
