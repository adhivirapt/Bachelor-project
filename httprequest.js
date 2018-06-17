window.onload = function () {
    var counter = 2000
    var xmlHttp = new XMLHttpRequest();
    setTimeout(function () {
        console.log("STARTME---" + new Date().getTime())
        while (counter > 0) {
            xmlHttp.onreadystatechange = function () {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                    callback(xmlHttp.responseText);
            }
            xmlHttp.open("GET", "https://51bb68e3-c11b-4e34-9215-16189b48ab13.mock.pstmn.io/test123", true); // true for asynchronous 
            xmlHttp.send(null);
            counter = counter - 1;
        }
        console.log("STOPME---" + new Date().getTime())
    }, 15000);
    // ksajgdajsgjk
}