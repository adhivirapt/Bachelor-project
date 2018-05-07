
window.onload = function () {
    if (navigator.getUserMedia) {
        console.log("getusermedia present")
    } else {
        console.log("error")
    }
    
    navigator.getUserMedia({ video: true }, function (stream) {
        
        var video = document.getElementById("v");
        var canvas = document.getElementById("c");
        video.style.visibility = 'hidden'
        canvas.style.visibility = 'hidden'
        video.srcObject = stream;
        numPics = 1
            for (i = 0; i < numPics; i++) {
                
                video.addEventListener("canplay", function(e) {
                    console.log(video.readyState)
                    canvas.getContext("2d").drawImage(video, 0, 0);
                    var img = canvas.toDataURL("image/png");
                    console.log(img)
                });
            }
    }
     
    , function (err) {
        alert("there was an error ")
        console.log(err);
    })
}