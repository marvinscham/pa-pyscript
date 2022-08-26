# Benchmarks

## Konfiguration

_Angelehnt an Pierre Quentels [Brython Benchmarking 2015](https://brythonista.wordpress.com/2015/03/28/comparing-the-speed-of-cpython-brython-skulpt-and-pypy-js/)_

- Windows 10 64-bit
- Firefox 104.0 64-bit
- Neuste Version des jeweiligen Frameworks
- 5 Läufe pro Framework
- Neustart und Leerung jeglicher Caches nach jedem Lauf
- Geometrisches Mittel der 5 Versuche

## Ergebnisse

- CPython 3.10.6
- [Skulpt 1.3.0 @ Python 2.6(ish)](https://skulpt.org/)
- [PyPy.js v0.4.0 @ Python 2.7.9](https://pypyjs.org/)
- [Brython 3.10.0 @ Python 3.10.6](https://brython.info/console.html)
- [Pyodide 0.21.1 @ Python 3.10.2](https://pyodide.org/en/stable/console.html)
- [PyScript 2022.06.1 @ Python 3.10.2](https://pyscript.net/examples/repl.html)

_Alle Messergebnisse inkl. Berechnung sind in `Benchmarks.xlsx` zu finden._

```text
                               Ausführungszeit (ms)                 |          x-mal langsamer als CPython
                    CPython Skulpt PyPy.js Brython Pyodide PyScript |  Skulpt PyPy.js Brython Pyodide PyScript
assignment.py            47   1711    1602    1242     221      194 |    36.4   34.1     26.4     4.7      4.1
augm_assign.py           97   2919    1828    2116     378      325 |    30.1   18.8     21.8     3.9      3.4
assignment_float.py      44   1707    1505    1306     234      195 |    38.8   34.2     29.7     5.3      4.4
build_dict.py           112   2301    2142    2071     466      437 |    20.5   19.1     18.5     4.2      3.9
set_dict_item.py         67   1824    2182    1455     347      320 |    27.2   32.6     21.7     5.2      4.8
build_list.py            84   1924    1527    1302     440      412 |    22.9   18.2     15.5     5.2      4.9
set_list_item.py         73   2264    1455    1432     342      307 |    31.0   19.9     19.6     4.7      4.2
add_integers.py         106   4232    1743    2298     436      381 |    39.9   16.4     21.7     4.1      3.6
add_strings.py          154   3155    1760    3440     627      575 |    20.5   11.4     22.3     4.1      3.7
str_of_int.py            23    553     189     131     104      103 |    24.0    8.2      5.7     4.5      4.5
create_function.py      114   2862    1521    2047     526      479 |    25.1   13.3     18.0     4.6      4.2
function_call.py        117   2363    1387    2090     457      385 |    20.2   11.9     11.9     3.9      3.3
```
