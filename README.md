# PyViz 

A dataviz workflow built with python serverside and Aframe/D3 clientside.

## Serverside

The DataProcess file connect to the api with proper parameters and insert results in Mysql tables.
The DataApi file formats data as json object and  serves it through http.

## Clientside

Javascript file use d3.json request to get json from python api, then display bars as in [Fabio Francino](https://fabiofranchino.com/blog/aframe-d3js-first-steps/) example.
