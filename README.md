# Machine Learning

## Rendu du 04/02/24

Le problème lié au merge a été corrigé. Nous avons aussi implémenté la dernière fonction, dans laquelle nous avons choisi la validation de type hold-out.

Pour ce qui est des tests, nous avons pu les implémenter dans le fichier test.

### Comment tester ? 

Avant de tester la fonction en elle-même, il faut renseigner le chemin relatif du fichier contenant les images que nous allons tester dans la fonction architecture.load_transform_label_train_dataset, associée à la variable data. Par exemple, on a :

`architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice])` avec comme chemin relatif "./data/Data/". La représentation souhaitée ("GC" ou "HC") , l'algorithme utilisé, et le nombre de pli utilisés dans notre vérification se font après le lancement du test.

### Résultats des tests : 

Les méthodes n'ont pas eu de bugs majeurs sauf une : learn_model_from_dataset avec le mode "PX", le tenseur de pixels. En effet, le tenseur retourne la liste des pixels de notre image sous forme d'une liste de tuples de trois éléments, incompatibles avec la fonction `fit` qui ne prend que des éléments de taille maximale 2. Donc nos tuples de taille 3 sont inutilissables avec cette fonction.  

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels dans l'objectif d'avoir des éléments de taille adéquate, utilisable avec la fonction `fit`.  


## Rendu du 04/02/24

Le problème lié au merge a été corrigé. Nous avons aussi implémenté la dernière fonction, dans laquelle nous avons choisi la validation de type hold-out.

Pour ce qui est des tests, nous avons pu les implémenter dans le fichier test.

### Comment tester ? 

Avant de tester la fonction en elle-même, il faut renseigner le chemin relatif du fichier contenant les images que nous allons tester dans la fonction architecture.load_transform_label_train_dataset, associée à la variable data. Par exemple, on a :

`architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice])` avec comme chemin relatif "./data/Data/". La représentation souhaitée ("GC" ou "HC") , l'algorithme utilisé, et le nombre de pli utilisés dans notre vérification se font après le lancement du test.

### Résultats des tests : 

Les méthodes n'ont pas eu de bugs majeurs sauf une : learn_model_from_dataset avec le mode "PX", le tenseur de pixels. En effet, le tenseur retourne la liste des pixels de notre image sous forme d'une liste de tuples de trois éléments, incompatibles avec la fonction `fit` qui ne prend que des éléments de taille maximale 2. Donc nos tuples de taille 3 sont inutilissables avec cette fonction.  

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels dans l'objectif d'avoir des éléments de taille adéquate, utilisable avec la fonction `fit`.  

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels. 
