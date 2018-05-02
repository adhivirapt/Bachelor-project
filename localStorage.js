window.onload = function () {
    if (typeof (Storage) !== "undefined") {
        for(var i = 0;i<10000;i++){
            localStorage.setItem(i, "Smith");
            // console.log(localStorage.getItem(i));
        }
    } else {
        console.log("error")
    }

}