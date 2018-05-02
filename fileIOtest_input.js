window.onload = function () {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    document.getElementById('files').addEventListener('change', handleFileSelect, false);
  } else {
    alert('The File APIs are not fully supported in this browser.');
  }
}

function handleFileSelect(evt) {
  var files = evt.target.files; 

  console.log(files)
}