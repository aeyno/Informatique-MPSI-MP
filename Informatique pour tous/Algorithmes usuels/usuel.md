# Les algorithmes usuels

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

    - Itérative