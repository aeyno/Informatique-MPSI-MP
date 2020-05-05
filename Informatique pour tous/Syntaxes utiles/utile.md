# Les syntaxes courantes et utiles du langage Python



## Déclarer des fonctions

- Fonctions classiques
    
    ```python
    def nomDeLaFonction(parametre1, parametre2):
        resultat = traitement(parametre1, parametre2)
        return resultat
    ```

- Fonctions anonymes

    Exemple: f(x) = x + 1 et g(x,y) = 2x - 3y
    ```python
    f = lambda x: x + 1
    g = lambda x,y: 2*x - 3*y
    ```

## Structures conditionnelles

- Boucle for (i variant de a (inclu) à b (exclu))

    ```python
    for i in range(a,b):
        traitement(i)
    ```


## Manipulation des tableaux

- Déclaration d'un tableau

    ```python
    tableau = []
    ```

- Récupérer le (n+1)-ième élément d'un tableau
    
    ```python
    x = tableau[n]
    ```

- Récupérer les éléments d'un tableau entre l'indice a (inclu) et l'indice b (exclu)
    
    ```python
    sousTableau = tableau[a:b]
    ```

- Inverser les éléments d'un tableau
    
    ```python
    tableauInverse = tableau[::-1]
    ```


- Ajouter un élément à un tableau

    ```python
    tableau.append(x)
    ```

- Supprimer le dernier élément d'un tableau (et le récupèrer)

    ```python
    x = tableau.pop()
    ```

- Supprimer le n-ième élément d'un tableau (et le récupèrer)

    ```python
    x = tableau.pop(n)
    ```
