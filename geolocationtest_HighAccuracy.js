window.onload = function () {
    var options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };

    function success(pos) {}

    function error(err) {}
    
    for (i = 0; i < 50000; i++) {
        navigator.geolocation.getCurrentPosition(success, error, options);
    }
}