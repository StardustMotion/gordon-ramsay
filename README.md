# gordon-ramsay


Projet de TATIA


Idée  : un programme capable de générer des phrases Gordon Ramsay-esque (chef culinaire britannique)

Le style de phrase est basé sur les phrases de Gordon dans la série Cauchemar en Cuisine (https://en.wikipedia.org/wiki/Kitchen_Nightmares)  et sont en anglais


# Implémentation

A l'aide d'une chaîne de Markov de mémoire m (à définir), le programme sélectionne aléatoirement des mots utilisés par Gordon, selon les m mots précédents et leur probabilité d'être sélectionnés.

# Guide d'utilisation

Il suffit de lancer main.py avec python.
Spécifiez le nombre de morceaux de texte à générer (environ 120 caractères chacun) et c'est printé.

# Background technique

main.py utilise le fichier parserOutput.in. C'est un fichier qui contient les données nécéssaires pour que l'algorithme puisse générer : les mots, leurs fréquences, les prochains mots etc.
Ce fichier (parserOutput.in) peut-être reproduit par vous même : il suffit d'executer parser.py.
parser.py utilise des données brutes dans data/dataSets, et les transforme en données utilisables dans parserOutput.in.
