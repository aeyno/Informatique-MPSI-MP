# Algorithme du pivot de Gauss pour la résolution d'un système d'équations linéaire


## Sans Numpy

Une matrice est un tableau de vecteurs colonnes M = [C1, C2, C3...] avec Ci un tableau de nombres

```python
def transvection(M, i, j, c):
    '''Ajoute c fois la ligne j à la ligne i'''
    for k in range(len(M)):
        # On fait varier la colonne dont on manipule les coefficients
        M[k][i] = M[k][i] + c*M[k][j]


def dilatation(M, i, c):
    '''Multiplie la ligne i d'une matrice M par un scalaire c'''
    for k in range(len(M)):
        # On fait varier la colonne dont on multiplie les coefficients
        M[k][i] = c*M[k][i]


def echange(M, i, j):
    '''Échange les lignes i et j d'une matrice M'''
    for k in range(len(M)):
        # On fait varier la colonne dont on échange les coefficients
        M[k][i], M[k][j] = M[k][j], M[k][i]


def choixpivot(M, j):
    '''Choisit le pivot sur la colonne j. Choisit le plus grand nombre en valeur absolue.'''
    ij, maxi = (0, 0), 0

    for i in range(j, len(M[0])):
        # On se déplace sur la colonne j pour trouver le plus grand coefficient
        if(abs(M[j][i]) > maxi):
            ij, maxi = (j, i), abs(M[j][i])
    if (maxi == 0):
        return -1
    else:
        return ij[1]


def pivot_gauss(A, B):
    '''Résoud le système AX = B où A est une matrice nxn et B un vecteur colonne de taille nx1.'''
    # On concatène les deux matrices A et B en une matrice de dimension nx(n+1)
    C = A[:]
    C.append(B)

    for j in range(len(A[0])):
        # On transforme la matrice en matrice triangulaire supérieure
        i = choixpivot(C, j)
        if i == -1:
            raise ValueError("La matrice A n'est pas inversible")
        echange(C, i, j)
        for k in range(j+1, len(A[0])):
            c = -C[j][k]/C[j][j]
            transvection(C, k, j, c)

    for i in range(len(A[0])):
        # On met des 1 sur la diagonale
        dilatation(C, i, 1/C[i][i])

    for i in range(len(A[0])-1, -1, -1):
        # On laisse uniquement la diagonale en remontant ligne par ligne
        for k in range(i-1, -1, -1):
            c = -C[i][k]
            transvection(C, k, i, c)

    return C
```

## Avec Numpy

Les matrices sont des tableaux numpy bidimensionnels

```python
import numpy as np

def np_transvection(C, i, j, c):
    C[i] = C[i] + c*C[j]


def np_dilatation(C, i, c):
    C[i] = c*C[i]


def np_echange(C, i, j):
    for k in range(np.shape(C)[1]):
        C[i, k], C[j, k] = C[j, k], C[i, k]


def np_choixpivot(C, j):
    ij, maxi = (0, 0), 0

    for i in range(j, len(C)):
        if(abs(C[i, j]) > maxi):
            ij, maxi = (i, j), abs(C[i, j])
    if (maxi == 0):
        return -1
    else:
        return ij[0]


def np_pivot(A, B):
    C = np.hstack((A, np.array([B]).transpose()))

    for j in range(len(A)):
        i = choixpivot(A, j)
        if (i == -1):
            raise ValueError("La matrice A n'est pas inversible")
        echange(C, i, j)
        for k in range(j+1, len(A)):
            c = -C[k, j]/C[j, j]
            transvection(C, k, j, c)

    for j in range(len(A)):
        dilatation(C, j, 1/C[j, j])

    for j in range(len(A)-1, -1, -1):
        # On laisse uniquement la diagonale en remontant ligne par ligne
        for k in range(j-1, -1, -1):
            c = -C[j][k]
            transvection(C, k, j, c)

    return C
```