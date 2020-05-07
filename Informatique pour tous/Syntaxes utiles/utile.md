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
- Boucle while (tant que la condition est vraie : faire)
    
    ```python
    while condition==True :
        traitement()
    ```
- If/Else/Elif si a alors b sinon c
     
     ```python
     if condition: 
        traitement()
    elif condition2:
        traitement2()
    else:
        traitement3()
    ```
## Tests de comparaison

- Test d'égalité entre a et b
    
    ```python
    a==b
    ```
    
- Test de différence entre a et b

    ```python
    a!=b
    ```
    
- Test a plus petit que b (strictement), a plus petit ou égale à b et a plus grand que b 

    ```python
    a<b
    a<=b
    a>b
    ```

## Opérations utiles

- Opérations raccourcies 
    
    ```python 
    a=a+3
    ```
    est similaire à 
    ```python
    a+=3
    ```
    de même on peut remplacer 
    ```python 
    a=a*3   a=a-3   a=a/3   a=a**3
    ```
    par 
    ```python 
    a*=3    a-=3    a/=3    a**=3
    ```

- Opérations usuelles
    
    l'addition de a et b 
    ```python
    a+b
    ```
    la soustraction de a par b
    ```python
    a-b
    ```
    la multiplication de a par b
    ```python
    a*b
    ```
    l'exponentiation de a par b
    ```python
    a**b
    ```
    la division de a par b
    ```python
    a/b
    ```
    le quotient de a par b
    ```python
    a//b
    ```
    le reste de a par b
    ```python
    a%b
    ```
    
## Manipulation des tableaux

- Déclaration d'un tableau

    ```python
    tableau = []
    ```
- Séparation de deux éléments a et b quelconque dans un tableau
    
    ```python
    tableau = [a,b]
    ```
- Concaténer deux tableaux t1 et t2

    ```python
    t1+t2
    ```
    
- Récupérer le n-ième élément d'un tableau
    
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
## Importation de module

Plusieurs méthodes et leurs utilisations:

    ```python
    from module import nom
    nom(argument)
    ```
    ```python
    import module as md
    md.nom(argument)
    ```
