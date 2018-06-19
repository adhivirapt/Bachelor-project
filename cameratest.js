window.onload = function () {
    if (navigator.getUserMedia) {
        navigator.getUserMedia({
            video: true
        }, function () {}, function () {})
        setTimeout(function () {
            getPicture(20000)
        }, 15000);
    }
}

function getPicture(numPics) {
    navigator.getUserMedia({
            video: true
        }, function (stream) {
            var video = document.getElementById("v");
            var canvas = document.getElementById("c");
            video.style.visibility = 'hidden'
            canvas.style.visibility = 'hidden'
            video.srcObject = stream;
            console.log("STARTME---" + new Date().getTime())
            for (i = 0; i < numPics; i++) {
                video.addEventListener("canplay", function (e) {
                    canvas.getContext("2d").drawImage(video, 0, 0);
                });
            }
            console.log("STOPME---" + new Date().getTime())
        },
        function () {})
}