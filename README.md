# Goodreads_Prog1
Projektna naloga za Programiranje 1

Najbolje ocenjene knjige
------------------------

Analiziral bom 10.000 najbolje ocenjenih knjig s strani Goodreads (https://www.goodreads.com/list/show/1.Best_Books_Ever).
Za vsako knjigo bom zajel:

- Naslov knjige in leto izdaje
- Avtorja (kjer bo na voljo)
- Oceno knjige in število glasov
- Opis in dolžino knjige
- Žanre (in število glasov za vsak žanr)

Delovne hipoteze:
- Kateri avtor je napisal največ uspešnih knjig?
- Kateri žanri so najpopularnejši?
- Ali ocene knjig ponazarjajo Gaussovo krivuljo?
- Kater avtor je napisal največ uspešnic, če analiziramo najboljših 10.000 knjig?
- Kater avtor je najboljši, če analiziramo le najbolj uspešnih 100 knjig?
- Ali avtorja najbolj uspešni 10.000 knjig in najbolj uspešnih 100 knjig sovpadata?
- Ali so najboljše knjige v angleščini?

V mapi obdelani-podatki so CSV datoteke, ki jih bom analiziral. autorji.csv vsebujejo avtorje knjig in njihove ID-je, ocene.csv vsebuje ocene ter število glasov, vsi_podatki.csv vsebuje vse podatke, ki jih lahko dobimo iz začetne strani, genre.csv vsebuje število glasov za posamezen žanr. Ker sem za genre.csv moral pobrati podatke še za vsako podstran, sem lahko zbral podatke samo za 100 knjig, saj bi prenos 10.000 spletnih strani trajal predolgo časa.
