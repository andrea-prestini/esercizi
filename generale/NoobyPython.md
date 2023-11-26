# Titolo principale della relazione


1. usare + invece delle f string
2. chiudere manualmente i file aperti al posto di utilizzare with
3. usare comandi manuali quando risorse e file devono essere chiusi, sempre meglio with
4. exept senza specificazioni
5. usare lista vuota come valore di default al posto di None
6. non usare list comprehensions
7. usare troppo list list comprehensions
8. usare == al posto di isistance per verificare la natura di un oggetto
9. usare == per verificare stato True o False

    `if x == True`

    `if x is True`
10. usare range(len(a)) al posto di accedere direttamente ad a:

    ```python
    a = [1,2,3]
    for val in a:
        pass```
        pass
11. iterare sulle chiavi di un dict non necessita di d.keys, possiamo scrivere
    `for key in d`
12. usare la forma unpacking per assegnazione multipla:

    ```python
    miatupla = 1,2
    x,y = miatupla
    ```

13. usare propria variabile i al posto di enumerate:

    ```python
    for i, x in enumerate(lista):
        pass
    ```

14. usare time start end al posto di time.perf_counter

    ```python
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter
    print(end-start)
    ```
15. Non usare numpy e pandas per calcoli matematici
16.  Usare import * perdendo lo scope delle variabili
17.  Non usare la forma cartella.modulo per importare elementi non presenti nel path principale
18.  Non usare PEP8

## Un poco di matematica

When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$ and they are 
$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$

$$\Sigma_{i=1}^k x_i \qquad \sum_{i=1}^k x_i$$

Read more [[]]
