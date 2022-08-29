import * as d3 from "https://cdn.skypack.dev/d3@7";
const url = "https://duolingo.checksch.de/duo_user_info.json";

fetch(url)
    .then((res) => res.json())
    .then((out) => {
        const langInfo = out.lang_data;

        const langNames = new Map([
            ["eo", "Esperanto"],
            ["en", "Englisch"],
            ["ru", "Russisch"],
            ["ja", "Japanisch"],
            ["es", "Spanisch"]
        ]);

        let langInfoPrepped = [];
        Object.entries(langInfo).forEach((el) => {
            let item = {};
            item["name"] = langNames.get(el[1].learningLanguage);
            item["shortcode"] = el[1].learningLanguage;
            item["count"] = el[1].xp;

            // Filter irrelevant items
            if (item["count"] > 500) {
                langInfoPrepped.push(item);
            }
        });

        const fn = d => d.count;
        const data = d3.pie().value(fn)(langInfoPrepped);
        const maxVal = d3.max(langInfoPrepped, fn);
        const colorScale = d3.scaleLinear().domain([0, maxVal]).range(["azure", "teal"]);

        const arc = d3
            .arc()
            .innerRadius(210)
            .outerRadius(310)
            .padRadius(300)
            .padAngle(2 / 300)
            .cornerRadius(8);

        const js = d3.select("#js");
        js.select(".loading").remove();

        const svg = js
            .append("svg")
            .attr("viewBox", "-320 -320 640 640")
            .attr("width", 400)
            .attr("height", 400);

        const imageSize = 42

        for (const d of data) {
            const tooltip = d.data.name + "\n" + d.value + " XP"
            svg.append("path").style("fill", colorScale(d.value)).attr("d", arc(d)).append("svg:title").text(tooltip);

            const image = svg
                .append("image")
                .attr("xlink:href", "https://marvinscham.de/assets/img/lang/" + d.data.shortcode + ".png")
                .attr("x", -1 * imageSize / 2)
                .attr("y", -1 * imageSize / 2)
                .attr("width", imageSize)
                .attr("height", imageSize)
                .attr("transform", `translate(${arc.centroid(d).join(",")})`)
                .attr("text-anchor", "middle")

            image
                .append("svg:title")
                .text(tooltip)

        }
    })
    .catch((err) => console.log(err));