
window.onload = function () {
    window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;
    function onInitFs(fs) {
        fs.root.getFile('test.txt', { create: true }, function (fileEntry) {
            fileEntry.createWriter(function (fileWriter) {
                var blob = new Blob([text1], { type: 'text/plain' });
                fileWriter.write(blob);
            })
        });

    }
    window.requestFileSystem(window.TEMPORARY, 1024 * 1024, onInitFs);
}