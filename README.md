# gordon-ramsay


Projet de TATIA par **ALESSANDRO Kévin** et **DENOS Alexandre**

*Concept : un programme capable de générer des phrases Gordon Ramsay-esque (chef culinaire britannique)*

Le style de phrase est *principalement* basé sur des phrases de Gordon dans la série **Cauchemar en Cuisine**(https://en.wikipedia.org/wiki/Kitchen_Nightmares).
Les citations sont en anglais et non-exaustives.


# Implémentation

A l'aide d'une chaîne de Markov de mémoire m = 2, le programme sélectionne aléatoirement des mots utilisés par Gordon avec une probabilité basée sur le taux d'apparition. 

Une mémoire de taille 2 ici signifie que le mot n est généré en fonction des mots n-1 et n-2.

# Guide d'utilisation

Il suffit de lancer main.py avec python.
Spécifiez le nombre de messages et c'est printé!

Il est possible de taper "debug" (sans les guillemets), et ensuite le nombre de messages, pour accéder à l'algorithme détaillé.
Générer des messages en mode débug affiche le nombre de situations où l'algorithme a eu la possibilité de choisir parmi plusieurs sources pour la génération d'un mot, ainsi que les mots qui étaient disponibles à ce moment avec leur probabilité!

# Background technique

main.py contient le code principal pour la génération de message.
Mais il a besoin du fichier parserOutput.in, qui contient les données pour générer ces messages.

parserOutput.in existe déjà dans le projet, mais vous pouvez le recréer vous-même en exeeécutant tout simplement le fichier parser.py.

parser.py utilise des jeux de données dans data/dataSets dits sous forme "brute", et il écrit dans parserOutput.in des données utilisables.

# Panthéon

Quelque pépites générées à partir de ce projet :

![hallOfFame1](/res/hof1.png)



![hallOfFame2](/res/hof2.png)



![hallOfFame3](/res/hof3.png)



![hallOfFame4](/res/hof4.png)



![hallOfFame5](/res/hof5.png)



![hallOfFame6](/res/hof6.png)



![hallOfFame7](/res/hof7.png)




