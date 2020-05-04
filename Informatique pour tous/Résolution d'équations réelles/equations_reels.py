# Méthodes de résolutions d'équations réelles

def dichotomie(f, a, b, epsilon):
    '''On recherche un réel l compris entre a et b tel que f(l)=0. Pour cela on réduit successivement l'intervalle de recherche, en le coupant en deux, jusqu'a ce qu'il soit plus petit que Epsilon.'''
    while b-a > 2*epsilon:
        m = (a+b/2)
        if f(a)*f(m) > 0:
            a = m
        else:
            b = m
    return (a+b)/2

def newton(f, f_prime, n):
    '''Méthode de Newton (ou Newton-Raphson), on approxime le graphe d'une fonction f grâce à la tangente en ce point si on possède sa dérivée f_prime pour trouver un point où la fonction s'annule'''
    for _ in range(n):
        a = a - f(a)/f_prime(a)
    return a