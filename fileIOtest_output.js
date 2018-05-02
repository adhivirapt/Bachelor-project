
window.onload = function () {
    var obj_url = window.URL.createObjectURL(blob);
    var iframe = document.getElementById('viewer');
    iframe.setAttribute('src', obj_url);
    window.URL.revokeObjectURL(obj_url);

}