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

## Chiffrement de César

```python
def chiffrement_cesar(message, p):
    s = []
    for i in range(len(message)):
        s.append((message[i] + p)%256)
    return s


def dechiffrement_cesar(message, p):
    return chiffrement_cesar(message, -p)
```

## Code de Vigenère

```python
def chiffrement_vigenere(msg, cle):
    s = []
    for i in range(len(msg)):
        s.append((msg[i] + cle[i%len(cle)])%256)
    return s

def dechiffrement_vigenere(msg, cle):
    a = [-x for x in cle]
    return chiffrement_vigenere(msg, a)
```