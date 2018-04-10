window.onload = function () {
    var counter = 20
    while (counter > 0) {
        var xmlHttp = new XMLHttpRequest();
        var theUrl = "https://51bb68e3-c11b-4e34-9215-16189b48ab13.mock.pstmn.io/test123"
        xmlHttp.open("GET", theUrl, false); // false for synchronous request
        xmlHttp.send(null);
        console.log(xmlHttp.status)
        counter -- ;
        // return xmlHttp.responseText;
    }

}