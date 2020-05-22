# Les syntaxes courantes et utiles du langage OCaml

## Déclarer une variable

```ocaml
let a = 5;;
```

## Déclarer une fonction

- Fonction non récursive
  
    ```ocaml
    let fonction param1 param2 = param1 + param2;;
    ```

- Fonction récursive

    Exemple de la fonction factorielle

    ```ocaml
    let rec factorielle n = match n with
        | 0 -> 1
        | _ -> n * (factorielle (n-1));;
    ```

## Structures conditionnelles

- Boucle for (i variant de a (inclu) à b (inclu))

    ```ocaml
    for i=a to b do
        traitement i
    done;;
    ```

- Boucle while (tant que la condition est vraie : faire)
  
    ```ocaml
    while condition do
        traitement
    done;;
    ```

- If/Else
  
    ```ocaml
    if condition
    then traitement1
    else traitement2
    ```
