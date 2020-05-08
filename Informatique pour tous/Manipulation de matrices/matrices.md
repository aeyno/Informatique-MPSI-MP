# Manipulation de matrices

## Creation d'une matrice de taille n,p

```python
def matrice(n,p):
    L=[]
    for _ in range(p):
        L1=[]
        for _ in range(n):
            L1.append(0)
        L.append(L1)
    return L
```

## Creation d'une matrice carré de taille n

```python
def matrice_carre(n):
    return matrice(n,n)
```
## Produit matriciel de a par b

```python
def aux_a_i_j(a,b,i,j):
    a1,a2=dimension_matrice(a)
    b1,b2=dimension_matrice(b)
    s=0
    for k in range(a2):
        s+=a[k][i]*b[j][k]
    return s
    
    
def produit_matriciel(a,b):
    a1,a2=dimension_matrice(a)
    b1,b2=dimension_matrice(b)
    if a1==b2:
        L=matrice(a1,b2)
        for i in range(a1):
            for j in range(a1):
                L[j][i]=aux_a_i_j(a,b,i,j)
        return L
    else :
        print("incompatible")
```

## Trace d'une matrice carré

```python
def trace(a):
    a1,a2=dimension_matrice(a)
    s=0
    for i in range(a1):
        s+=a[i][i]
    return s 
```

## Multiplication par un scalaire d'une matrice

```python
def multiplication_ligne(n,a,i):
    a1,a2=dimension_matrice(a)
    for k in range(a2):
        a[k][i]*=n
    return a
        
def multiplication_matrice(n,a):
    a1,a2=dimension_matrice(a)
    for i in range(a1):
        multiplication_ligne(n,a,i)
    return a
```

