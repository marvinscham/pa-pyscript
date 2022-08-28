import pandas as pd
import folium
import json
import random
from pyodide.http import open_url

data = "./data.json"
geo_json = json.loads(open_url(data).read())

m = folium.Map(location=[50.4, 9.6], zoom_start=6)


def style(x):
    match (x["properties"]["plz"]):
        case "0": return {"color": "yellow"}
        case "1": return {"color": "orange"}
        case "2": return {"color": "tomato"}
        case "3": return {"color": "violet"}
        case "4": return {"color": "dodgerblue"}
        case "5": return {"color": "blue"}
        case "6": return {"color": "gold"}
        case "7": return {"color": "green"}
        case "8": return {"color": "mediumseagreen"}
        case "9": return {"color": "slateblue"}
    return {"color": "black"}


folium.GeoJson(geo_json, name="Postleitzahl", style_function=lambda x: style(x)).add_to(
    m
)

m
