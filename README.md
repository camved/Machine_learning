# Machine_learning

## Rendu du 29/01/2024

## Rendu du 29/01/2024

Aujourd'hui, le 29/01/2024, nous avons réaliser les fonctions demandées lors du TP. 
Nous avons pour les fonctions load_transform_label_train_dataset et load_transform_label_test_dataset, qui renvoie une liste d'image de type Image2, une nouvelle classe que nous avons implémenté.
Elle contient une méthode str et représente les images avec leur "name", "label" et "representation".

Nous avons eu un problème technique de dernière minute lié au merge dans gitHub : Les deux fonctions ci-dessus ne marche que dans la branch Camille... Pour l'instant. 

Ce qu'il reste à faire avant le second rendu :
- Terminer la fonction estimate_model_score
- les tests (pour l'instant réalisés avec des "print", mais on souhaiterait le faire avec le module test.unit )
- Corriger le problème lié au Merge. 

## Rendu du 04/02/24

Le problème lié au merge a été corrigé. Nous avons aussi implémenté la dernière fonction, dans la quelle nous avons choisi la validation de type hold-out.

Pour ce qui est des tests, nous avons pu les implémenter dans le fichier test.

### Comment tester ? 

Avant de tester la fonction en elle-même, il faut renseigner la représentation souhaitée (entre "GC" et "HC") et le chemin absolu du fichier contenant les images que nous allons tester dans train.  

### Résultats des tests : 

Les méthodes n'ont pas eu de bugs majeurs sauf une : learn_model_from_dataset avec le mode "PX", le tenseur de pixels. En effet, le tenseur retourne une liste de tuples de trois éléments, incompatibles avec la fonction fit qui ne prend que des éléments de taille maximale 2. 

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels. 

## Rendu du 04/02/24

Le problème lié au merge a été corrigé. Nous avons aussi implémenté la dernière fonction, dans la quelle nous avons choisi la validation de type hold-out.

Pour ce qui est des tests, nous avons pu les implémenter dans le fichier test.

### Comment tester ? 

Avant de tester la fonction en elle-même, il faut renseigner la représentation souhaitée (entre "GC" et "HC") et le chemin absolu du fichier contenant les images que nous allons tester dans train.  

### Résultats des tests : 

Les méthodes n'ont pas eu de bugs majeurs sauf une : learn_model_from_dataset avec le mode "PX", le tenseur de pixels. En effet, le tenseur retourne une liste de tuples de trois éléments, incompatibles avec la fonction fit qui ne prend que des éléments de taille maximale 2. 

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels. 

## Rendu du 04/02/24

Le problème lié au merge a été corrigé. Nous avons aussi implémenté la dernière fonction, dans la quelle nous avons choisi la validation de type hold-out.

Pour ce qui est des tests, nous avons pu les implémenter dans le fichier test.

### Comment tester ? 

Avant de tester la fonction en elle-même, il faut renseigner la représentation souhaitée (entre "GC" et "HC") et le chemin absolu du fichier contenant les images que nous allons tester dans train.  

### Résultats des tests : 

Les méthodes n'ont pas eu de bugs majeurs sauf une : learn_model_from_dataset avec le mode "PX", le tenseur de pixels. En effet, le tenseur retourne une liste de tuples de trois éléments, incompatibles avec la fonction fit qui ne prend que des éléments de taille maximale 2. 

Nous avons donc essayé de chercher, sans succès, une fonction bijective de R^3 dans R pour modéliser nos pixels. 
