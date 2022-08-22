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
            item["count"] = el[1].xp;

            // Filter irrelevant items
            if (item["count"] > 500) {
                langInfoPrepped.push(item);
            }
        });

        const fn = (d) => d.count;
        const data = d3.pie().value(fn)(langInfoPrepped);

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
            .attr("width", "400")
            .attr("height", "400");

        for (const d of data) {
            svg.append("path").style("fill", "rebeccapurple").attr("d", arc(d));

            const text = svg
                .append("text")
                .style("fill", "white")
                .attr("transform", `translate(${arc.centroid(d).join(",")})`)
                .attr("text-anchor", "middle");

            text
                .append("tspan")
                .style("font-size", "24")
                .attr("x", "0")
                .text(d.data.name);

            text
                .append("tspan")
                .style("font-size", "18")
                .attr("x", "0")
                .attr("dy", "1.3em")
                .text(d.value);
        }
    })
    .catch((err) => console.log(err));