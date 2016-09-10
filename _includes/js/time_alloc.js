"use strict"

var data = Array();
var raw = {% include  data/time_alloc.json %};
for (var x in raw){
    // var trace = {};
    // trace['type'] = 'box';
    // trace['name'] = x;
    // trace['y'] = raw[x];
    data.push({
        name: x,
        y: raw[x],
        type: 'box'
    });
}
var layout = {
    // autosize: false,
    // width: 600,
    // height: 400,
    margin: {
        l: 50,
        r: 50,
        b: 100,
        t: 50,
        pad: 4
    },
    showlegend: false,
    yaxis: {
        title: 'Percent time',
        range: [0, 100]
    }
};
Plotly.newPlot('boxplot', data, layout, {displayModeBar: false});
