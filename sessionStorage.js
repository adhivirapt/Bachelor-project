window.onload = function () {
    console.log("STARTME---" + new Date().getTime())
    for (var i = 0; i < 300000; i++) {
        sessionStorage.setItem(i, "");
        }
    console.log("STOPME---" + new Date().getTime())


}