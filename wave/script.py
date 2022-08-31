from pyodide import create_proxy, to_js
import numpy as np
import js

# Kreisfrequenz -> ω = 2πf
def angfreq(frequency):
    return 2 * np.pi * frequency


# Schwebung -> y(t) = y^(sin(ωt) + sin(ωt))
def beat(freq1, freq2, time):
    return np.sin(angfreq(freq1) * time) + np.sin(angfreq(freq2) * time)


def inp_update(event):
    document.querySelector("#freqlabel").innerText = freq2.value
    plot()


def scroll_update(event):
    js.checkScrollDirection(event)
    inp_update(event)


def plot():
    beat_deflection = beat(freq1, float(freq2.value), time)
    js.update(to_js(time), to_js(beat_deflection))


freq1 = 440
freq2 = document.querySelector("#freq")

freq2.addEventListener("input", create_proxy(inp_update))
document.body.addEventListener("wheel", create_proxy(scroll_update))

sampling_frequency = 140
seconds = 2
time = np.linspace(0, seconds, int(seconds * sampling_frequency))


plot()
