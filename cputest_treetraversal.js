window.onload = function () {
    function Node() {
        // this.data = "data";
        this.parent = null;
        this.children = new Array();
    }

    function Tree() {
        var node = new Node();
        this._root = node;
    }
    Tree.prototype.traverseDF = function(callback) {
 
        // this is a recurse and immediately-invoking function 
        (function recurse(currentNode) {
            // step 2
            for (var i = 0, length = currentNode.children.length; i < length; i++) {
                // step 3
                recurse(currentNode.children[i]);
            }
     
            // step 4
            callback(currentNode);
             
            // step 1
        })(this._root);
     
    };

    var tree = new Tree();
    var child = tree._root.children;
    for (var i = 0; i<1000; i++){
        child.push(new Node());
        for(var j = 0; j<1000;j++)
        child = child[0].children;

    }
    tree.traverseDF(function(node) {
        console.log(node)
    });
    // tree.children.push(new Node());
    // console.log(tree);
    
}