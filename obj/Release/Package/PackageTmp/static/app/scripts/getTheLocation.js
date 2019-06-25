var x = null;
// these next two numbers are the thing we want to know if we're close to the ticketbooth
var longToCompareWith = -119.8226407; //ticketbooth location
var latToCompareWith = 36.7524107

// these variables get set below later.
var yourLong = null;
var yourLat = null;
var distance = null;


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showLocation);
    }
};



function showLocation(position) {
    yourLong = position.coords.longitude;
    yourLat = position.coords.latitude;
    distance = getDistance(latToCompareWith, longToCompareWith, yourLat, yourLong);

    // sends a popup if we're within 10 feet of a location!
    if (distance < 30655) {
        Push.create("Thanks for stopping by!", {
            body: "We would love to hear about your experience at the zoo",
            icon: '/icon.png',
            timeout: 4000,
            onClick: function () {
                window.open('feedback/');
                this.close();
            }
        });
    }
};
// math calculation to get your current distance and compare it to the set lat and lon
function getDistance(lat1, lon1, lat2, lon2) {
    var deg2rad = function (deg) {
        return deg * (Math.PI / 180)
    }


    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2 - lat1);  // deg2rad below
    var dLon = deg2rad(lon2 - lon1);
    var a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2)
        ;
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = R * c; // Distance in km
    return d * 3280.84; // distance in feet. - johnny
};