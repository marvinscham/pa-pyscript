# pa-pyscript

Projektarbeit RWU: Python im Browser mit PyScript

## Verwendung

**Hinweis:** Das bloße Aufrufen der `html`-Dateien ist aufgrund von Sicherheitsbeschränkungen des Browsers beim `file`-Protokoll nicht ausreichend zur Ausführung von PyScript.

Lösung des Problems ist das Aufsetzen eines lokalen Servers, beispielsweise über [XAMPP](https://www.apachefriends.org/de/index.html) oder direkt per Python 3:

```sh
python -m http.server
```

Alternativ können auch die unten stehenden Links unter meiner Domain `checksch.de` verwendet werden, auf welche stündlich der aktuelle Stand des `main`-Branches gespielt wird.

## Aufrufbare Beispiele

- [Grundlegendes Beispiel](https://checksch.de/pa-pyscript/basic-example/javascript.html)

  - D3/JavaScript

- [Grundlegendes Beispiel](https://checksch.de/pa-pyscript/basic-example/pyscript.html)

  - D3/PyScript

![JS Demo](https://raw.githubusercontent.com/marvinscham/pa-pyscript/main/basic-example/basic-example.png)

- [REPL mit Matplotlib](https://checksch.de/pa-pyscript/repl/repl.html)

  - [Beispielcode zum Copypasten](https://raw.githubusercontent.com/marvinscham/pa-pyscript/main/repl/matplotlib-example.py)

![REPL](https://raw.githubusercontent.com/marvinscham/pa-pyscript/main/repl/repl.png)

- [PLZ-Karte Deutschland](https://checksch.de/pa-pyscript/map/map.html) (_Achtung, lädt lang_)

  - Folium

![Map](https://raw.githubusercontent.com/marvinscham/pa-pyscript/main/map/map.png)

- [Schwebung](https://checksch.de/pa-pyscript/wave/wave.html)

  - NumPy/Chart.js

![Wave](https://raw.githubusercontent.com/marvinscham/pa-pyscript/main/wave/wave.png)
