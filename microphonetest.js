
window.onload = function () {
    if (navigator.getUserMedia) {
        console.log("getusermedia present")
    } else {
        console.log("error")
    }
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        // store streaming data chunks in array
        const chunks = [];
        var counter = 0;
        // create media recorder instance to initialize recording
        const recorder = new MediaRecorder(stream);
        // function to be called when data is received
        recorder.ondataavailable = e => {
            if (counter == 9) {
                recorder.stop();
            }
            // add stream data to chunks
            chunks.push(e.data);
            // if recorder is 'inactive' then recording has finished
            // if (recorder.state == 'inactive') {
            // convert stream data chunks to a 'webm' audios format as a blob
            // const blob = new Blob(chunks, { type: 'audio/webm' });
            // convert blob to URL so it can be assigned to a audio src attribute
            // createAudioElement(URL.createObjectURL(blob));
            counter ++;
            console.log(chunks)
            console.log(counter)
            // }

        };
        // start recording with 1 second time between receiving 'ondataavailable' events
        this.console.log(recorder.state)
        recorder.start(1000)
        this.console.log(recorder.state)
        // setTimeout to stop recording after 4 seconds

    }).catch(console.error);

}