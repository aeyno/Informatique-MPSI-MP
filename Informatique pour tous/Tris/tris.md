# Algorithmes de tri


Le site [bigocheatsheet.com](https://www.bigocheatsheet.com/) répertorie les algorithmes de tri les plus courants ainsi que leurs complexités respectives.

## Tri insertion

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
            L[j] = L[j-1]
            j = j-1
        L[j] = v
    return L
```


## Tri rapide

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n^2)

```python
def échange(L,i,j):
    '''Échange 2 cases i et j d'un tableau'''
    L[i], L[j] = L[j], L[i]

def partitition(L,g,d):
    pivot = L[randrange(g,d)]
    m = g
    for i in range(g+1,d):
        if L[i] < pivot:
            m = m+1
            échange(L,i,m)
    échange(L,g,m)
    return m

def aux_rapide(L,g,d):
    if g < d-1:
        m = partitition(L,g,d)
        aux_rapide(L,g,m)
        aux_rapide(L,m+1,d)

def tri_rapide(L):
    aux_rapide(L,0,len(L))
```

## Tri fusion

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n log(n))

```python
def fusion(L1,L2,g,m,d):
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