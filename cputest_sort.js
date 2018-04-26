window.onload = function () {
    var array = []
    for (i = 0; i < 100000; i++) {
        array.push(Math.random())
    }
    array.sort()
    // for (i = 0; i < 10000; i++) {
    //     console.log(array[i].toString())
    // }
}