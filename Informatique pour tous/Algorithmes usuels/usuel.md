# Les algorithmes usuels

## Exponentiation

- Récursive

```python
def exp_recursive(x,n):
    if n==0:
        return 1
    else:
        x*exp_recursive(x,n-1)
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
