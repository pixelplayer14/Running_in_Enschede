var map = L.map('map').setView([52.2391482,6.8565761],13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

L.geoJSON(AllStreets,{style:{"color":"red"}}).addTo(map);
 
new L.GPX("/test.gpx" ,{
    polyline_options: {
      color: 'green'
    }, async: true}).addTo(map);