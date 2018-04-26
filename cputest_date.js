window.onload = function () {
var date = Date.now()
this.console.log(date)
for (i=0;i<1500;i++){
    console.log(Date.now()-date)
}
}