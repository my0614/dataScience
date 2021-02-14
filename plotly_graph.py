import plotly

plotly.offline.init_notebook_mode()
plotly.offline.iplot({
"data": [{
    "x": [5, 4, 10],
    "y": [4, 2, 5]
}],
"layout": {
    "title": "random graph"
}
})
