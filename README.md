# Goodreads_Prog1
Projektna naloga za Programiranje 1

Najbolje ocenjene knjige
------------------------

Analiziral bom 10.000 najbolje ocenjenih knjig s strani Goodreads (https://www.goodreads.com/list/show/1.Best_Books_Ever).
Za vsako knjigo bom zajel:

- Naslov knjige in leto izdaje
- Avtorja, ilustratorja(kjer bo na voljo)
- Oceno knjige in število glasov
- Opis in dolžino knjige
- žanre (in število glasov za vsak žanr)

Delovne hipoteze:
- Kateri avtor je napisal največ uspešnih knjig?
- Ali avtor in ilustrator knjige pogosto sovpadata?
- Kateri žanri so najpopularnejši?

V mapi obdelani-podatki so CSV datoteke, katere bom analiziral. autorji.csv vsebujejo avtorje knjig in njihove ID-je, ocene.csv vsebuje ocene ter število glasov, vsi_podatki.csv vsebuje vse podatke, ki jih lahko dobimo iz začetne strani, genre.csv vsebuje število glasov za posamezen žanr, ilustratorji(top100knjig).csv vsebuje knjige, njihove avtore in ilustratorje. Ker sem za genre.csv in ilustratorji(top100knjig).csv moral pobrati podatke še za vsako podstran, sem lahko zbral podatke samo za 100 knjig, saj bi prenos 10.000 spletnih strani trajal predolgo časa.
