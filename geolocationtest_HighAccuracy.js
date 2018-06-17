window.onload = function () {
    var options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };
    // navigator.permissions.query({name:'geolocation'}).then(function(result) {
    //     if (result.state === 'granted') {
    //       console.log("haha")
    //     } else if (result.state === 'prompt') {
    //       console.log("hahah")
    //     }
    //     // Don't do anything if the permission was denied.
    //   });
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error, options);
        setTimeout(function () {
            console.log("STARTME---" + new Date().getTime())
            for (i = 0; i < 200000; i++) {
                navigator.geolocation.getCurrentPosition(success, error, options);
            }
            console.log("STOPME---" + new Date().getTime())
        }, 15000);

    }

    function success() {}

    function error() {}

}