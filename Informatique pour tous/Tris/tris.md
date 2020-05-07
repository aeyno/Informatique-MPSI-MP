# Algorithmes de tri


Le site [bigocheatsheet.com](https://www.bigocheatsheet.com/) répertorie les algorithmes de tri les plus courants ainsi que leurs complexités respectives.

## Tri insertion

Description: on parcours le tableau en triant les éléments au fur et à mesure. Au i-éme élément, on le fait descendre jusqu'à sa place dans le début du tableau (qui est déjà trié).
Dans cet exemple, l'algorithme fonctionne par effet de bord.

Complexité:
- Meilleur cas : O(n)
- En moyenne : O(n^2)
- Pire cas : O(n^2)

```python
def tri_insertion(L):
    for i in range(len(L)):
        v = L[i]
        j = i
        while (j > 0) and (v < L[j-1]):
            #Tant que l'élément est plus petit on le fait descendre
            L[j] = L[j-1]
            j = j-1
        L[j] = v
```


## Tri rapide

Description: 

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n^2)

```python
def echange(L,i,j):
    '''Échange 2 cases i et j d'un tableau'''
    L[i], L[j] = L[j], L[i]

def partitition(L,g,d):
    '''On choisit un pivot entre g et d dans L, et on tri tous les éléments de l'intervalle à droite ou à gauche du pivot selon qu'ils soient plus grands ou plus petit.'''
    pivot = L[randrange(g,d)]
    m = g
    for i in range(g+1,d):
        if L[i] < pivot:
            m = m+1
            échange(L,i,m)
    echange(L,g,m)
    return m

def aux_rapide(L,g,d):
    '''On partitionne récursivement les sous-tableaux du tableau à trier'''
    if g < d-1:
        m = partitition(L,g,d)
        aux_rapide(L,g,m)
        aux_rapide(L,m+1,d)

def tri_rapide(L):
    aux_rapide(L,0,len(L))
```

## Tri fusion

Description: On découpe le tableau en deux récusivement jusqu'à obtenir des tableaux d'un seul éléments que l'on fusionnent en mettant leurs éléments dans l'ordre.

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n log(n))

```python
def fusion(L1,L2,g,m,d):
    '''On fusionne deux tableaux triés L1 et L2'''
    i = g
    j = m
    for k in range(g,d):
        if (i < m) and ((j == d) or (L1[i] <= L2[j])):
            L2[k] = L1[i]
            i+=1
        else:
            L2[k] = L1[j]
            j+=1

def aux_fusion(g,d,L,tmp):
    '''On découpe le tableau récursivement'''
    if g < d-1:
        m = int((g+d)/2)
        aux_fusion(g,m,L,tmp)
        aux_fusion(m,d,L,tmp)
        tmp[g:d] = L[g:d]
        fusion(tmp,L,g,m,d)

def tri_fusion(L):
    n = len(L)
    aux_fusion(0,n,L,[None for _ in range(n)])
```
