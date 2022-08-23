from pyodide import create_proxy, to_js, open_url
import d3
import json
import js

url = f"https://duolingo.checksch.de/duo_user_info.json"
res = open_url(url)
lang_info = json.loads(res.read())["lang_data"]
lang_info_prepped = []

lang_names = {
    "eo": "Esperanto",
    "en": "Englisch",
    "ru": "Russisch",
    "ja": "Japanisch",
    "es": "Spanisch",
}

for lang in lang_info:
    item = {
        "name": lang_names.get(lang_info[lang]["learningLanguage"]),
        "shortcode": lang_info[lang]["learningLanguage"],
        "count": lang_info[lang]["xp"],
    }

    # Filter irrelevant items
    if lang_info[lang]["xp"] > 500:
        lang_info_prepped.append(item)

fn = create_proxy(lambda d, *_: d["count"])
data = d3.pie().value(fn)(to_js(lang_info_prepped))
max_val = max(lang_info_prepped, key=lambda d: d["count"])["count"]
color_scale = d3.scaleLinear().domain([0, max_val]).range(["#fafafa", "rebeccapurple"])
js.console.log(to_js(max_val))

arc = (
    d3.arc()
    .innerRadius(210)
    .outerRadius(310)
    .padRadius(300)
    .padAngle(2 / 300)
    .cornerRadius(8)
)

py = d3.select("#py")
py.select(".loading").remove()

svg = (
    py.append("svg")
    .attr("viewBox", "-320 -320 640 640")
    .attr("width", 400)
    .attr("height", 400)
)

image_size = 42

for d in data:
    d_py = d.to_py()
    tooltip = d_py["data"]["name"] + "\n" + str(d_py["value"]) + " XP"

    (
        svg.append("path")
        .style("fill", color_scale(d_py["value"]))
        .attr("d", arc(d))
        .append("svg:title")
        .text(tooltip)
    )

    image = (
        svg.append("image")
        .attr(
            "xlink:href",
            "https://marvinscham.de/assets/img/lang/"
            + d_py["data"]["shortcode"]
            + ".png",
        )
        .attr("x", -1 * image_size / 2)
        .attr("y", -1 * image_size / 2)
        .attr("width", image_size)
        .attr("height", image_size)
        .attr("transform", f"translate({arc.centroid(d).join(',')})")
        .attr("text-anchor", "middle")
    )

    (image.append("svg:title").text(tooltip))
