// Initialize the platform object:
var platform = new H.service.Platform({
    'apikey': '27GqiDFIL_Oji2U1b1fIR6YXeKmoJs-v1EFvnU-u8qY'
});

const lat = 22.719568;
const long = 75.857727;

// Obtain the default map types from the platform object
const mapTypes = platform.createDefaultLayers();

// Initialize a map:
const map = new H.Map(
    document.getElementById('mapContainer'),
    mapTypes.raster.terrain.map,
    {
        zoom: 10,
        center: {lat: lat, lng: long}
    });

// Enable the event system on the map instance:
const mapEvents = new H.mapevents.MapEvents(map);

// Add event listener:
map.addEventListener('tap', function (evt) {
    // Log 'tap' and 'mouse' events:
    console.log(evt.type, evt.currentPointer.type);
});

// Instantiate the default behavior, providing the mapEvents object:
const behavior = new H.mapevents.Behavior(mapEvents);

//window.addEventListener('resize',()=> get.ViewProt().resize())
const marker = new H.map.Marker({lat: lat, lng: long});

// Add the marker to the map:
map.addObject(marker);

// Create the default UI:
const ui = H.ui.UI.createDefault(map, mapTypes);

// Create an info bubble object at a specific geographic location:
const bubble = new H.ui.InfoBubble({lng: 76.0534, lat: 22.9676}, {
    content: '<b>Dewas</b>'
});

// Add info bubble to the UI:
ui.addBubble(bubble);