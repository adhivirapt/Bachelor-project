
window.onload = function () {
    if (navigator.mediaDevices) {
        navigator.mediaDevices.getUserMedia({ audio: true })
        setTimeout(function () {
            navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
                var counter = 0;
                const recorder = new MediaRecorder(stream);
                recorder.ondataavailable = e => {
                    if (counter == 100) {
                        recorder.stop();
                        console.log("STOPME---" + new Date().getTime())
                    }
                    counter ++;
        
                };
                console.log("STARTME---" + new Date().getTime())
                recorder.start(200)
                
            }).catch(console.error);
        }, 20000);

    }

}