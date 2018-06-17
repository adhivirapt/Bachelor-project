window.onload = function () {
    console.log("STARTME---" + new Date().getTime())
    multiply(matrix500x500, matrix500x500)
    console.log("STOPME---" + new Date().getTime())
    
    function multiply(a, b) {
        var aNumRows = a.length
        var aNumCols = a[0].length
        var bNumCols = b[0].length
        m = new Array(aNumRows); // initialize array of rows
        for (var r = 0; r < aNumRows; ++r) {
            m[r] = new Array(bNumCols); // initialize the current row
            for (var c = 0; c < bNumCols; ++c) {
                m[r][c] = 0; // init ialize the current cell
                for (var i = 0; i < aNumCols; ++i) {
                    m[r][c] += a[r][i] * b[i][c];
                }
            }
        }
    }
}