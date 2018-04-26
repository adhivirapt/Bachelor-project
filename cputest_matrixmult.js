window.onload = function () {
    var a = createMatrix()
    var b = createMatrix()
    console.log(a[0].length)
    console.log(multiply(a, b))

    function createMatrix() {
        var matrix = []
        for (var i = 0; i < 9; i++) {
            matrix[i] = [];
            for (var j = 0; j < 9; j++) {
                matrix[i].push(Math.random())
            }
        }
        return matrix
    }

    function multiply(a, b) {
        var aNumRows = a.length
        var aNumCols = a[0].length
        var bNumRows = b.length
        var bNumCols = b[0].length

        m = new Array(aNumRows);  // initialize array of rows
        for (var r = 0; r < aNumRows; ++r) {
            m[r] = new Array(bNumCols); // initialize the current row
            for (var c = 0; c < bNumCols; ++c) {
                m[r][c] = 0;             // initialize the current cell
                for (var i = 0; i < aNumCols; ++i) {
                    m[r][c] += a[r][i] * b[i][c];
                }
            }
        }
        return m;
    }
}