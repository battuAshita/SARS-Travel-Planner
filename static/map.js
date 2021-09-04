// Initialize and add the map
function initMap() {
    // The location of India
    const India = {lat: 20.119888548797277, lng: 79.17323631682544};
    // The map, centered at India
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: India,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: India,
        map: map,
    });
}