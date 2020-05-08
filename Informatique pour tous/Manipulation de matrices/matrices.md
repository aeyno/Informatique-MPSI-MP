# Manipulation de matrices


Dans les programmes suivants, les matrices sont des tableaux de vecteurs (tableaux de colonnes).


## Affichage d'une matrice 

```python
def printMat(M):
    '''Affiche une matrice'''
    for i in range(0, len(M[0])):
        for j in range(0, len(M)):
            print(M[j][i], end='\t')
        print()
```


## Passage d'une matrice numpy à une matrice avec des listes et inversement

```python
def numpy2list(M):
    '''Transforme une matrice définie commme un tableau de vecteurs en matrice numpy'''
    A = []
    for i in range(np.shape(M)[0]):
        C = []
        for j in range(np.shape(M)[1]):
            C.append(M[j, i])
        A.append(C)
    return A


def list2numpy(M):
    '''Transforme une matrice numpy en matrice définie commme un tableau de vecteurs'''
    return np.array(M).transpose()
```


## Creation d'une matrice de taille n,p

```python
def matrice(n,p,v=0):
    '''Créé une matrice de taille nxp remplie avec la valeur v'''
    L=[]
    for _ in range(p):
        L1=[]
        for _ in range(n):
            L1.append(v)
        L.append(L1)
    return L
```

## Creation d'une matrice carré de taille n

```python
def matrice_carre(n,v=0):
    return matrice(n,n,v)
```
## Matrice identité 

```python
def identite(n):
    L=matrice_carre(n)
    for i in range(n):
        L[i][i]=1
    return L
``` 
## Dimension d'une matrice quelconque

```python
def dimension_matrice(A):
    return len(A[0]),len(A)
```

## Produit matriciel de a par b

```python
def aux_a_i_j(A,B,i,j):
    '''Somme des A_i,k B_k,j'''
    a1,a2=dimension_matrice(A)
    b1,b2=dimension_matrice(B)
    s=0
    for k in range(a2):
        s+=A[k][i]*B[j][k]
    return s
    
    
def produit_matriciel(A,B):
    a1,a2=dimension_matrice(A)
    b1,b2=dimension_matrice(B)
    if a1==b2:
        L=matrice(a1,b2)
        for i in range(a1):
            for j in range(a1):
                L[j][i]=aux_a_i_j(A,B,i,j)
        return L
    else :
        print("incompatible")
```

## Addition de deux matrices de même taille

```python
def addition_matrices(A,B):
    a1,a2=dimension_matrice(A)
    L=matrice(a1,a2)
    for i in range(a2):
        for j in range(a1):
            L[i][j]=A[i][j]+B[i][j]
    return L 
```

## Multiplication par un scalaire d'une matrice

```python
def multiplication_ligne(n,A,i):
    a1,a2=dimension_matrice(A)
    for k in range(a2):
        A[k][i]*=n
    return A
        
def multiplication_matrice(n,A):
    a1,a2=dimension_matrice(A)
    for i in range(a1):
        multiplication_ligne(n,A,i)
    return A
```


## Transposé d'une matrice carré 

```python
def transpose(A):
    a1,a2=dimension_matrice(A)
    for i in range(a1):
        for j in range(i):
            A[i][j],A[j][i]=A[j][i],A[i][j]
    return A
```

## Trace d'une matrice carré

```python
def trace(A):
    a1,a2=dimension_matrice(A)
    s=0
    for i in range(a1):
        s+=A[i][i]
    return s 
```



