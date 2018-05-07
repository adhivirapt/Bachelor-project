window.onload = function () {
    var LZW = {
        decompress: function (compressed) {
            "use strict";
            var i,
                dictionary = [],
                w,
                result,
                k,
                entry = "",
                dictSize = 256;
            for (i = 0; i < 256; i += 1) {
                dictionary[i] = String.fromCharCode(i);
            }

            w = String.fromCharCode(compressed[0]);
            result = w;
            console.log(compressed.length);
            for (i = 1; i < compressed.length; i += 1) {
                k = compressed[i];
                if (dictionary[k]) {
                    entry = dictionary[k];
                } else {
                    if (k === dictSize) {
                        entry = w + w.charAt(0);
                    } else {
                        entry =w + null;
                    }
                }

                result += entry;

                // Add w+entry[0] to the dictionary.
                dictionary[dictSize++] = w + entry.charAt(0);

                w = entry;
                console.log(i)
            }

            console.log(result)
            return result
        }
    } // For Test Purposes
    decomp = LZW.decompress(compressed1);
    document.getElementById("demo").innerHTML= decomp
    // debugger;

}