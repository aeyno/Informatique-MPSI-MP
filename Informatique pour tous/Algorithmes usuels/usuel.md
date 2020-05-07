# Les algorithmes usuels

## Exponentiation

- Récursive

```python
def exp_recursive(x,n):
    if n==0:
        return 1
    else:
        return x*exp_recursive(x,n-1)
 ```
 
 - Itérative
 
 ```python
 def exp_iterative(x,n):
    if n==0:
        return 1
    else:
        r=1
        for _ in range(n):
            r*=x
        return r
   ```
    
## Exponentiation rapide
    
Calcule x^n en log(n) opérations

```python
def exp_rapide(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2==0:
        exp_rapide(n**2, n//2)
    else:
        x*exp_rapide(n**2, n//2)
```

## Fonction factorielle

- Récursive

```python
def factorielle_rec(n):
    if n==0:
        return 1
    else:
        return n*factorielle_rec(n-1)
```

- Itérative

```python
def factorielle_ite(n):
    r=1
    for i in range(n):
        r*=i+1
    return r
``` 

## Suite de Fibonacci

- Récursive

```python
def fibo_rec(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibo_rec(n-1)+fibo_rec(n-2)
```

- Itérative

```python
def fibo_ite(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
```

## Echange de deux éléments d'une liste

```python
def echange(L,i,j):
    L[i],L[j]=L[j],L[i]
```

## Fonction partie entière

```python
int(x)
```    

## Fonction valeur absolue 

en python elle existe sous la forme 

```python
abs(x)
```

on peut la coder sous cette forme

```python
def absolue(x):
    if x<0:
        return -x
    return x 
```

## Plus grand commun diviseur (PGCD)

```python
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
```

## Algorithme d'Euclide étendu 

```python
def euclide_etendu(x,y):
    (r1,u1,v1,r2,u2,v2)=(x,1,0,y,0,1)
    while r2!=0:
         q=r1//r2
         (r1,u1,v1,r2,u2,v2)=(r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2)
    return r1,u1,v1
```
