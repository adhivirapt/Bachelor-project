window.onload = function () {
    if (navigator.getUserMedia) {
        getPicture(1)
        setTimeout(function () {
            console.log("STARTME---" + new Date().getTime())
           {
                getPicture(10000)
            }
            console.log("STOPME---" + new Date().getTime())
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
            for (i = 0; i < numPics; i++) {
                video.addEventListener("canplay", function (e) {
                    console.log(video.readyState)
                    canvas.getContext("2d").drawImage(video, 0, 0);
                    var img = canvas.toDataURL("image/png");
                    console.log(img)
                });
            }
        }

        ,
        function (err) {
            alert("there was an error ")
        })
}