from pyodide import create_proxy, to_js
import numpy as np
import js

# Auslenkung -> ω * t = 2πft
def deflection(frequency, time):
    return np.sin(2 * np.pi * frequency * time)


# Schwebung -> y(t) = y^(sin(2πft) + sin(2πft)); Annahme gleicher Amplitude (1), keine Phasenverschiebung
def beat(freq1, freq2, time):
    return deflection(freq1, time) + deflection(freq2, time)


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

sampling_frequency = 1920 / 10 * 4
seconds = 2
time = np.linspace(0, seconds, int(seconds * sampling_frequency))


plot()
