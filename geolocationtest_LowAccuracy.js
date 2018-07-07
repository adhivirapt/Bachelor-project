window.onload = function () {
    var options = {
        enableHighAccuracy: false,
        timeout: 10000,
        maximumAge: 0
    };
    i = 0;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successTrivial, error, options);
        setTimeout(function () {
            console.log("STARTME---" + new Date().getTime())
            navigator.geolocation.getCurrentPosition(success, error, options);

        }, 15000);

    }

    function successTrivial() {}

    function success() {
        i++;
        console.log(i)
        call()
    }

    function error(err) {
        console.log(err)
        i++;
        call()
    }
    function call() {
        if (i == 10) {
            console.log("STOPME---" + new Date().getTime())
        } else {
            navigator.geolocation.getCurrentPosition(success, error, options);
        }
    }
}