# Benchmarks

## Systemumgebung

### OS/Browser

- Windows 10 64-bit
- Firefox 104.0 64-bit

### Browser-Python Projekte

_Neuste Version des jeweiligen Frameworks:_

- CPython 3.10.6
- [Skulpt 1.3.0 @ Python 2.6(ish)](https://skulpt.org/)
- [Brython 3.10.0 @ Python 3.10.6](https://brython.info/console.html)
- [PyPy.js v0.4.0 @ Python 2.7.9](https://pypyjs.org/)
- [Pyodide 0.21.1 @ Python 3.10.2](https://pyodide.org/en/stable/console.html)
- [PyScript 2022.06.1 @ Python 3.10.2](https://pyscript.net/examples/repl.html)

## Ausführungsgeschwindigkeit

### Konfiguration

_Angelehnt an Pierre Quentels [Brython Benchmarking 2015](https://brythonista.wordpress.com/2015/03/28/comparing-the-speed-of-cpython-brython-skulpt-and-pypy-js/)_

**Hinweis:** Pierre Quentel ist der Ersteller von Brython (→ Bias möglich)

- 5 Läufe pro Framework
- Neustart und Leerung jeglicher Caches nach jedem Lauf
- Geometrisches Mittel der 5 Läufe

### Ergebnisse

_Alle Messergebnisse inkl. Berechnung sind in `Benchmarks.xlsx` zu finden._

```text
                                  Ausführungszeit (ms)
                    CPython Skulpt Brython PyPy.js Pyodide PyScript
assignment.py            47   1711    1242    1602     221      194
augm_assign.py           97   2919    2116    1828     378      325
assignment_float.py      44   1707    1306    1505     234      195
build_dict.py           112   2301    2071    2142     466      437
set_dict_item.py         67   1824    1455    2182     347      320
build_list.py            84   1924    1302    1527     440      412
set_list_item.py         73   2264    1432    1455     342      307
add_integers.py         106   4232    2298    1743     436      381
add_strings.py          154   3155    3440    1760     627      575
str_of_int.py            23    553     131     189     104      103
create_function.py      114   2862    2047    1521     526      479
function_call.py        117   2363    2090    1387     457      385
```

```text

                         x-mal langsamer als CPython
                     Skulpt Brython PyPy.js Pyodide PyScript
assignment.py          36.4    26.4    34.1     4.7      4.1
augm_assign.py         30.1    21.8    18.8     3.9      3.4
assignment_float.py    38.8    29.7    34.2     5.3      4.4
build_dict.py          20.5    18.5    19.1     4.2      3.9
set_dict_item.py       27.2    21.7    32.6     5.2      4.8
build_list.py          22.9    15.5    18.2     5.2      4.9
set_list_item.py       31.0    19.6    19.9     4.7      4.2
add_integers.py        39.9    21.7    16.4     4.1      3.6
add_strings.py         20.5    22.3    11.4     4.1      3.7
str_of_int.py          24.0     5.7     8.2     4.5      4.5
create_function.py     25.1    18.0    13.3     4.6      4.2
function_call.py       20.2    11.9    11.9     3.9      3.3
```

**Notiz:** nach Quentels Angaben konnte Brython zum Zeitpunkt der Erstellung seiner eigenen Messung Ergebnisse erzielen, bei denen Brython bei manchen Tests _schneller_ als CPython war. Dies konnte an dieser Stelle auch in anderen Browsern nicht repliziert werden und scheint [kein Einzelfall](https://github.com/QQuick/Transcrypt/issues/661#issuecomment-539999058) zu sein.

## Downloadgröße / "Gewicht"

### Konfiguration

Es handelt sich bei den Größenangaben nicht um die vollständige, entpackte Größe, sondern um den verursachten Traffic, den das Endgerät des Nutzers tatsächlich stemmen muss.

Serverseitige Kompression (z.B. gzip) und Asset-Minification sind also bei den gemessenen Größen bereits einbezogen.

### Ergebnisse

```text
Skulpt       0.2MB
Brython      1.2MB
PyPy.js      4.3MB
Pyodide      7.6MB + externe Pakete
PyScript     8.3MB + externe Pakete
PyScript*   25.3MB (mit Matplotlib)
```

## Nutzerfreundlichkeit

### Konfiguration

- Aufruf über [JS](https://checksch.de/pa-pyscript/basic-example/javascript.html)/[PY](https://checksch.de/pa-pyscript/basic-example/pyscript.html).
- Kein Caching
- 5 Läufe

### Ergebnisse

```text
             (MB)  (s)    (s)
             Load Finish  TTI
JavaScript    0.2   1.17  0.8
PyScript     12.9   8.57  9.6
-----------------------------
Faktor       64.5   7.32 12.0
```
