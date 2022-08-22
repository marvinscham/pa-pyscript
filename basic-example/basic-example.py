from pyodide import create_proxy, to_js, open_url
import d3
import json

url = f"https://duolingo.checksch.de/duo_user_info.json"
res = open_url(url)
lang_info = json.loads(res.read())["lang_data"]
lang_info_prepped = []

for lang in lang_info:
    item = dict(name=lang_info[lang]["learningLanguage"], count=lang_info[lang]["xp"])

    # Filter irrelevant items
    if lang_info[lang]["xp"] > 500:
        lang_info_prepped.append(item)

fn = create_proxy(lambda d, *_: d["count"])
data = d3.pie().value(fn)(to_js(lang_info_prepped))

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
    .attr("width", "400")
    .attr("height", "400")
)

for d in data:
    d_py = d.to_py()

    (svg.append("path").style("fill", "rebeccapurple").attr("d", arc(d)))

    text = (
        svg.append("text")
        .style("fill", "white")
        .attr("transform", f"translate({arc.centroid(d).join(',')})")
        .attr("text-anchor", "middle")
    )

    (
        text.append("tspan")
        .style("font-size", "24")
        .attr("x", "0")
        .text(d_py["data"]["name"])
    )

    (
        text.append("tspan")
        .style("font-size", "18")
        .attr("x", "0")
        .attr("dy", "1.3em")
        .text(d_py["value"])
    )
