# Files et piles

## Files

> En informatique, une file dite aussi file d'attente (en anglais queue) est une structure de données basée sur le principe du premier entré, premier sorti ou PEPS, désigné en anglais par l'acroynyme FIFO (first in, first out) : les premiers éléments ajoutés à la file seront les premiers à en être retirés.
> -- Source: [Wikipédia](https://fr.wikipedia.org/wiki/File_(structure_de_donn%C3%A9es))

### Objet file

```ocaml
type 'a file = {
    mutable debut: 'a list;
    mutable fin: 'a list
};;

let file_vide = {
    debut = [];
    fin = []
};;
```

### Opérations sur les files

```ocaml
let enfile e f = f.fin <-  e :: f.fin;;

let est_vide f = match f.debut, f.fin with
    | [], [] -> true
    | _, _ -> false;;

let rec defile f = match f.debut, f.fin with
    | []   , [] -> failwith "file vide"
    | t::q , _  -> f.debut <- q
    | [], _     -> f.debut <- List.rev f.fin; f.fin <- []; defile f;;

let rec premier f = match f.debut, f.fin with
    | []   , [] -> failwith "file vide"
    | t::q , _  -> t
    | [], _     -> f.debut <- List.rev f.fin; f.fin <- []; List.hd f.debut;;
```

## Piles

> En informatique, une pile (en anglais stack) est une structure de données fondée sur le principe « dernier arrivé, premier sorti » (en anglais LIFO pour last in, first out), ce qui veut dire, qu'en général, le dernier élément, ajouté à la pile, sera le premier à en sortir.
> -- Source: [Wikipédia](https://fr.wikipedia.org/wiki/Pile_(informatique))

### Objet pile

En OCaml les piles sont tout simplement des listes.

```ocaml
let pile_vide () = [];;
```

### Opérations sur les piles

```ocaml
let empile v p = v :: p;;

let est_vide p = match p with
    | [] -> true
    | _  -> false;;

let depile p = match p with
    | t::q -> (t,q)
    | [] -> failwith "pile vide";;
```
