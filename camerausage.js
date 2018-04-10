window.onload = function () {
    if (navigator.getUserMedia) {
        console.log("getusermedia present")
    } else {
        console.log("error")
    }
    navigator.getUserMedia({ video: true }, function (stream) {
        var video = document.getElementById("v");
        var canvas = document.getElementById("c");
        // var button = document.getElementById("b");
        // button.disabled = false;
        
        video.srcObject = stream;
        setTimeout(function () {
            for (i = 0; i < 5; i++) {
                canvas.getContext("2d").drawImage(video, 0, 0);
                var img = canvas.toDataURL("image/png");
                console.log(img)
            }
        }, 3000);
    }, function (err) {
        alert("there was an error ")
        console.log(err);
    })
}