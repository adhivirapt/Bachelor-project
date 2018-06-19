window.onload = function () {
    console.log("STARTME---" + new Date().getTime())
    for (i = 0; i < 300000; i++) {
        Date.now()
    }
    console.log("STOPME---" + new Date().getTime())
}