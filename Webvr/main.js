;(function (d3) {

    var url = "http://192.168.0.19:1440/youplaboum"

    d3.json(url, function(error, jsonData) {
        if (error) throw error;
        //console.log(jsonData)
        update(jsonData);

    });

    function update (jsonData) {
         //console.log(jsonData);
        //console.log(d3.values(jsonData['postes'][0]));
        var dataLength =  jsonData['postes'].length;
        var occurency = [];
        var town = [];
        var label = [];
        var data = d3.range(dataLength).map(function (d, i) {
            return {v: Math.random()}
        })
        // adding an entity as holder for each box
        var entities = d3.select('a-scene')
            .selectAll('a-entity')
            .data(data)


        var newobj = entities.enter()
            .append('a-entity')
            .attr('rotation', function (d, i) {
                var a = 360 / data.length
                return '0 ' + a * i + ' 0'
            })

        for (var i = 0; i < dataLength; i++ )
        {
            //console.log(d3.values(jsonData['postes'][i]));
            arrayKey = d3.values(jsonData['postes'][i]);
           //arrayValue = d3.values(jsonData['postes'][i]);

           // console.log(arrayKey[1]);

            //console.log(arrayKey[0]);
            occurency.push(arrayKey[1]);
            town.push(arrayKey[0]);
            label.push(arrayKey[0] + " : " + arrayKey[1] )


        }
        //console.log(occurency);
        //console.log(town);

        //for (k in arrayValue) value.push(k);


            // appending a box within each entity
        console.log(label);
            newobj.append('a-box')
                .attr('color', 'red')
                .attr('width', 1)
                .attr('depth', 0.5)
                .attr('position', function (d, i) {
                    return '0 ' + d.v / 2 + ' -5'
                })
        d3.selectAll("a-box")
            .data(occurency)
            .attr('height', function(d) { return d  });

            newobj.append('a-text')
                .attr('color', 'black')
                .attr('position', function (d) {
                    return '-0.1 1.5 -2'
                })
                .attr('visible', false)

        d3.selectAll("a-text")
            .data(label)
            .attr('value', function(d) { return d  });

        newobj.on('mouseenter', function () {
            d3.select(this)
                .select('a-text')
                .attr('visible', true)
        })

        newobj.on('mouseleave', function () {
            d3.select(this)
                .select('a-text')
                .attr('visible', false)
        })

    }

})(window.d3)

//https://github.com/fabiofranchino/aframe-d3js-first-steps