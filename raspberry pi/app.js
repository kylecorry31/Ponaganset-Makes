var http = require('http');
var url = require('url');
var fs = require('fs');
var output = require('./output');

function getSensorValue(sensor) {
    var values = JSON.parse(fs.readFileSync('test.json'));
    if (sensor === 1)
        return {
            'temp': values.temp
        };
    else if (sensor === 2)
        return {
            "light": values.light
        };
    else if (sensor === 3)
        return {
            "light": values.light,
            "temp": values.temp
        };
    else if (sensor === 4){
        var motor = output();
        motor.on(18);
        return {};
    }
    else if (sensor === 5){
        var led = output();
        led.on(16);
    } else if (sensor === 6){
        output().destroy();
    }
    return null;
}

http.createServer(function (req, res) {

    var info = url.parse(req.url, true);
    var sensor = Number(info.query.sensor);
    var path = info.pathname;
    var result = getSensorValue(sensor);
    if (result && path === "/api/sensors") {
        res.writeHead(200, {
            'content-type': 'application/json'
        });
        res.end(JSON.stringify(result));
    } else if (path === "/") {
        res.writeHead(200, {
            'content-type': 'text/html'
        });
        res.end(fs.readFileSync('index.html'));
    } else {
        res.writeHead(404, {
            "content-type": "text/plain"
        });
        res.end("404 not found");
    }
}).listen(8000);