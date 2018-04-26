window.onload = function () {
    if (typeof (Storage) !== "undefined") {
        localStorage.setItem("lastname", "Smith");
    } else {
       console.log("error")
    }

}