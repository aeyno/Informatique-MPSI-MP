# Méthodes de résolutions d'équations différentielles

def euler(f,a,b,y0,n):
    '''Méthode d'Euler (ou Euler-Cauchy, ou méthode de la tangente) de résolution d'équations différentielles du premier ordre.
    On cherche à trouver une fonction y vérifiant y'=F(t,y) et y(t0) = y0
    La fonction retourne un tableau de n couples de points par lesquels passe la fonction sur l'intervalle [a,b].'''
    T = b-a
    h = T/n
    Yk = [0]*n
    Yk[0] = y0
    tk = [a + h*k for k in range(n)]
    for k in range(1,n):
        Yk[k] = Yk[k-1] + h*f(Yk[k-1], tk[k-1])
    return (Yk,tk)

def point_milieu():
    pass