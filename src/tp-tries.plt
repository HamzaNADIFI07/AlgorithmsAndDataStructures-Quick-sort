set term png
set xlabel 'Taille du tableau'
set ylabel 'Nombre moyen de comparaisons'

#######################
# Graphique 1 : Données Aléatoires
#######################
set title 'Comparaison des Algorithmes de Tri (Données Aléatoires)'
set output 'comparaison_random.png'
plot 'random_100.dat' index 0 using 1:2 w lp t 'MergeSort (aléatoire)', \
     '' index 0 using 1:3 w lp t 'QuickSort (pivot naïf, aléatoire)', \
     '' index 0 using 1:4 w lp t 'QuickSort (pivot aléatoire)'

#######################
# Graphique 2 : Données Triées (Croissantes)
#######################
set title 'Comparaison des Algorithmes de Tri (Données Triées)'
set output 'comparaison_increasing.png'
plot 'increasing_100.dat' index 0 using 1:2 w lp t 'MergeSort (croissant)', \
     '' index 0 using 1:3 w lp t 'QuickSort (pivot naïf, croissant)', \
     '' index 0 using 1:4 w lp t 'QuickSort (pivot aléatoire, croissant)'

#######################
# Graphique 3 : QuickSort avec Pivot Optimal
#######################
set title 'Performance de QuickSort avec Pivot Optimal'
set output 'comparaison_optimal.png'
plot 'optimal_100.dat' index 0 using 1:2 w lp t 'QuickSort (pivot optimal)'
