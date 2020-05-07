# Algorithmes de cryptographie

## Encodage et décodage d'un message

Pour pouvoir chiffrer un message il est souvent plus pratique de travailler avec des tableaux de nombres qu'avec des chaînes de caractères. Pour cela on encode les messages. Dans l'exemple suivant on utilise les fonctions `chr` et `ord` qui permettent respectivement de récuperer un caractère à partir de son numéro dans la table ASCII et de récupérer le numéro d'un caractère dans la table ASCII.

```python
def encode(msg):
    s = []
    for i in range(len(msg)):
        a = ord(msg[i])
        if a < 256: s.append(a)
    return s

def decode(l):
    msg = ""
    for i in range(len(l)):
        msg += chr(l[i])
    return msg
```