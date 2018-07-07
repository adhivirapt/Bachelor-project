window.onload = function () {
    var counter = 1000
    var counter1 = 1

    setTimeout(function () {
        console.log("STARTME---" + new Date().getTime())
        var xmlHttp = new XMLHttpRequest();
        getRequest(xmlHttp)
        xmlHttp.onreadystatechange = function () {
            if (counter == 0 && counter1 == 1) {
                console.log("STOPME---" + new Date().getTime())
                counter1++;
            } else if (xmlHttp.status == 200 && counter1 == 1) {
                getRequest(xmlHttp)
                counter--;
            }
        }
    }, 15000);

    function getRequest(xmlHttp) {
        xmlHttp.open("GET", "https://adhivirapt.github.io/blah/", true); // true for asynchronous 
        xmlHttp.send(null);
    }
}