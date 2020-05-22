# Algorithmes de tri



Le site [bigocheatsheet.com](https://www.bigocheatsheet.com/) répertorie les algorithmes de tri les plus courants ainsi que leurs complexités respectives.


## Tri insertion

Description: on parcours le tableau en triant les éléments au fur et à mesure. Au i-éme élément, on le fait descendre jusqu'à sa place dans le début du tableau (qui est déjà trié).
Dans cet exemple, l'algorithme fonctionne par effet de bord.

Complexité:
- Meilleur cas : O(n)
- En moyenne : O(n^2)
- Pire cas : O(n^2)

```ocaml
let insere_element_tableau v i =
    let j = ref i and e=v.(i) in
        while (!j>0) && (v.(!j-1) > e) do
            v.(!j) <- v.(!j-1) ; j:=!j-1
    done;
    v.(!j) <- e;;

let tri_insertion_tableau v =
    for i=1 to (Array.length v)-1 do
        insere_element_tableau v i
    done ;;

let rec insere e l = match l with
    | [] -> [ e ]
    | x::reste -> if e <= x
        then e::x::reste
    else x::(insere e reste);;

let rec tri_insertion l = match l with
    | [] -> []
    | x::reste -> insere x (tri_insertion reste);;
```


## Tri rapide

Description: Tri récursif

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n^2)


```ocaml

```


## Tri à bulle

Description: On fait remonter les éléments du tableau en faisant des permutations des cases voisines.

Complexité:
- Meilleur cas : O(n)
- En moyenne : O(n^2)
- Pire cas : O(n^2)

### Tri à bulle sur les tableaux

```ocaml
let une_passe fin v =
    let echange = ref false in 
    for i = 1 to fin do
        if v.(i-1) > v.(i) then 
            let tmp = v.(i) in
            v.(i) <- v.(i-1);
            v.(i-1) <- tmp;
            echange := true;
    done;
    !echange;;

let tri_bulle_tableau t =
    let a = ((Array.length t)-1) in
    let i = ref 0 in
    while (une_passe (a - !i) t) do
        i := !i +1;
    done;;
```

### Tri à bulle sur les listes

```ocaml
let rec une_passe_liste l = match l with
    | [] -> failwith "erreur"
    | [a] -> [a]
    | t::q -> match une_passe_liste q with
                | t'::q' when t>t' -> t'::t::q'
                | l -> t::l ;;


let rec tri_bulle_liste = 
    | [] -> []
    | -> match une_passe_liste l with 
            | true, t::q -> t::(tri_bulle_liste q)
            | _ -> l;;
```


## Tri fusion

Description: On découpe le tableau en deux récusivement jusqu'à obtenir des tableaux d'un seul éléments que l'on fusionne en mettant leurs éléments dans l'ordre.

Complexité:
- Meilleur cas : O(n log(n))
- En moyenne : O(n log(n))
- Pire cas : O(n log(n))


```ocaml
let fusion_tableau v debut fin aux =
    let m = (debut+fin)/2 and i = ref debut in let j = ref (m+1) in
    for k=0 to (fin-debut) do
    if (!i<=m)
    then
        begin
            if (!j<=fin)
            then
                begin
                    if v.(!i)<=v.(!j)
                        then begin aux.(k) <- v.(!i) ; i:=!i+1 end
                        else begin aux.(k) <- v.(!j) ; j:=!j+1 end
                    end
            else
                begin aux.(k) <- v.(!i) ; i:=!i+1 end
        end
    else begin aux.(k) <- v.(!j) ; j:=!j+1 end
    done;
    for k = 0 to (fin-debut) do
        v.(debut+k) <- aux.(k)
    done;;

let tri_fusion_tableau v =
    let n = (Array.length v ) in
    let aux = Array.make n 0 in
    let rec tri v i j aux =
        if j>i then
            begin
                let m = (i+j)/2 in
                tri v i m aux;
                tri v (m+1) j aux;
                fusion_tableau v i j aux
            end
    in tri v 0 (n-1) aux ;;
```