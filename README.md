# High speed scanning in human memory

Lien vers l'article: https://sdrive.cnrs.fr/s/wkBw2son3BYGLsw?dir=undefined&path=%2Fresources%2FArticles&openfile=326432908
Lien vers le github: https://github.com/juliettemr/high-speed-scanning-in-human-memory/

## Description générale

Dans cet article, Saul Sternberg cherche à déterminer comment nous retrouvons un item stocké en mémoire à court terme:

-> Parcourons-nous mentalement chaque élément un à un ?

-> Comparons-nous tous les éléments en parallèle ?

Pour répondre à ces questions, il mesure le temps de réaction nécessaire pour décider si un chiffre présenté appartient ou non à un ensemble de chiffres mémorisés juste avant, à l'aide de deux expériences.

## Expérience 1

### Objectif

Mesurer le temps de réaction lors d’une tâche de reconnaissance d’un chiffre appartenant ou non à une liste précédemment mémorisée.



## Expérience 2

## Résultats

Les résultats indiquent que le temps de réaction est proportionnel au nombre d'éléments dans la liste. Sternberg en conclut que la mémoire à court terme est explorée par un mécanisme séquentiel exhaustif impliquant une comparaison système par système, à vitesse constante.

## Test it yourself

To do the experience by yourself, use the following commands :

```
git clone git@github.com/juliettemr/high-speed-scanning-in-human-memory.git
cd high-speed-scanning-in-human-memory
python -m .venv venv
.venv\Scripts\activate.bat sur windows .venv/bin/activate sur linux/mac
pip install -r requirements.txt
python high-speed-scanning.py
```

To change the number of series for training and tests of each experiment, you can change `l7`, `l8`, `l12` and `l13` of the file `high-speed-scanning.py`.
