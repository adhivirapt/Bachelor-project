## Web Applications for Energy Benchmarking

## Motivation
9 web benchmark applications developed to test energy efficiency of JavaScript functionalities. This experiment is conducted with the help of Trepn profiler and Android Runner Python framework.

## Index HTML
```
<html>

<head>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body onload="init();">
    <!-- <video id="v" width="0" height="0" display = "none" controls autoplay ></video> -->
    <!-- <input id="b" type="button" disabled="true" value="Take Picture"></input> -->
    <!-- <canvas id="c" width="300" height="300" display="none"></canvas> -->
    <!-- <script type="text/javascript" src="loadvariablehere.js"></script> -->
    <script src="cputest_date.js"></script>
</body>

</html>
```
Uncomment the tags only if its needed. Specify directory of the desired web app in script tag ( with its preinitiated variable for cputest_sort) 

## Result
To see experiment result, go to ./result/process.py and uncomment desired web application section.
```

# geolocation true
# data =  [aggregate_data('./2018.06.26_100915/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeohigh10.txt', 'loggeohigh10.txt'),
#         aggregate_data('./2018.06.26_100915/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeohigh20.txt', 'loggeohigh20.txt'), 
#         aggregate_data('./2018.06.26_212757/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeohigh40.txt', 'loggeohigh40.txt')]

#geolocation false
# data = [aggregate_data('./2018.06.30_133604/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeolow10.2.txt', './loggeolow10.2.txt'), 
#         aggregate_data('./2018.06.29_095013/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeolow20.txt', 'loggeolow20.txt'), 
#         aggregate_data('./2018.06.28_024502/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampgeolow40.txt', 'loggeolow40.txt')]

# sort
# data = [aggregate_data(

```
For example, from this **process.py** snippet, uncomment **geolocation true** section with its corresponding lines to aggregate the data points and run 
```
python process.py
```

## Credits
https://github.com/KungPaoChicken/android-runner



