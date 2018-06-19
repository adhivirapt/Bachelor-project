window.onload = function () {
    var counter = 2000
    var xmlHttp = new XMLHttpRequest();
    setTimeout(function () {
        console.log("STARTME---" + new Date().getTime())
        while (counter > 0) {
            // xmlHttp.onreadystatechange = function () {
            // }
            xmlHttp.open("GET", "http://localhost:8081/api/simpleExample", false); // true for asynchronous 
            xmlHttp.send(null);
            counter = counter - 1;
            console.log(counter)
        }
        console.log("STOPME---" + new Date().getTime())
    }, 25000);;
    // ksajgdajsgjk
}