from pyodide.http import open_url
import folium, json
# import geopandas as gpd

def style(feature):
    match (feature["properties"]["plz"][0]):
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

# geo_json = json.loads(gpd.read_file("./plz-2stellig.shp", dtype={"plz": str}).to_json())
geo_json = json.loads(open_url("./plz-2stellig.geojson").read())

m = folium.Map(
    height=937, 
    width=1920, 
    location=[51.16, 10.45], 
    zoom_start=6
)

folium.GeoJson(
    geo_json, 
    name="PLZ 2-stellig", 
    style_function=style, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['plz'], 
        aliases=["PLZ-Ziffern"]),
    ).add_to(m)
folium.LayerControl().add_to(m)

m
