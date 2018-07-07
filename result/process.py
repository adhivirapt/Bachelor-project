import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import pylab
# from statistics import mean
from scipy.signal import find_peaks_cwt
from scipy.stats import linregress
import seaborn as sns
from scipy.stats import normaltest
from scipy.stats import describe
from scipy.stats import probplot
from scipy.stats import levene


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def get_cpu(dir, startStamp, stopStamp):
    csv = pd.read_csv(dir, skiprows=3)
    index = csv['Battery Power* [uW]'].index[csv['Battery Power* [uW]'].apply(
        pd.isnull)]
    csv = csv[:index[0]].astype(str).astype(float)
    csv = np.asarray(csv)
    index1 = find_nearest(csv[:, 0], startStamp)
    index2 = find_nearest(csv[:, 0], stopStamp)
    cpuList = csv[index1:index2, 5]
   
    averageCPU = cpuList.sum() / len(cpuList)
    return averageCPU


def get_averageEnergy(dir, startStamp, stopStamp):
    csv = pd.read_csv(dir, skiprows=3)
    index = csv['Battery Power* [uW]'].index[csv['Battery Power* [uW]'].apply(
        pd.isnull)]
    csv = csv[:index[0]].astype(str).astype(float)
    csv = np.asarray(csv)
    index1 = find_nearest(csv[:, 0], startStamp)
    index2 = find_nearest(csv[:, 0], stopStamp)
    powerList = csv[index1:index2, 3]
    powerList = powerList[np.nonzero(powerList)]
    powerList = powerList[~np.isnan(powerList)]
    cpuList = csv[index1:index2, 5]
    averageEnergy = (powerList.sum()/len(powerList) *
                     (stopStamp-startStamp))/(1000000 * 1000)
    return averageEnergy


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def aggregate_data(folder, stamplog, adblog):
    path = folder  # use your path
    aggregated = []
    counter = 0
    with open(stamplog, "r") as text_file:
        content = text_file.readlines()
        content = [x.strip() for x in content]
    with open(adblog, 'r') as myfile:
        data = myfile.read().replace('\n', '')

    regex1 = r"STARTME---(\d+)"
    regex2 = r"STOPME---(\d+)"
    startTime = re.findall(regex1, data)
    stopTime = re.findall(regex2, data)
    i = 0
    for file_ in listdir_nohidden(path):
        count = 0
        while float(startTime[count]) < float(content[i])*1000:
            print(count)
            count = count + 1
        startStamp = float(startTime[count]) - float(content[i])*1000
        stopStamp = float(stopTime[count]) - float(content[i])*1000
        dir = path+'/'+file_
        aggregated.append(get_averagePower(dir, startStamp, stopStamp))
        i = i + 1
    
    aggregated = [x for x in aggregated if str(x) != 'nan']
    return aggregated


def aggregate_data_cpu(folder, stamplog, adblog):
    path = folder  # use your path
    aggregated = []
    counter = 0
    with open(stamplog, "r") as text_file:
        content = text_file.readlines()
        content = [x.strip() for x in content]
    with open(adblog, 'r') as myfile:
        data = myfile.read().replace('\n', '')

    regex1 = r"STARTME---(\d+)"
    regex2 = r"STOPME---(\d+)"
    startTime = re.findall(regex1, data)
    stopTime = re.findall(regex2, data)
    diff = len(startTime) - len(stopTime)
    i = 0
    for file_ in listdir_nohidden(path):
        count = 0
        while float(startTime[count]) < float(content[i])*1000:
            print(count)
            count = count + 1
        startStamp = float(startTime[count]) - float(content[i])*1000
        stopStamp = float(stopTime[count-diff]) - float(content[i])*1000
        dir = path+'/'+file_
        aggregated.append(get_cpu(dir, startStamp, stopStamp))
        i = i + 1
    aggregated = [x for x in aggregated if str(x) != 'nan']
    return aggregated


def aggregate_data_duration(folder, stamplog, adblog):
    path = folder  # use your path
    aggregated = []
    counter = 0
    with open(stamplog, "r") as text_file:
        content = text_file.readlines()
        content = [x.strip() for x in content]
    with open(adblog, 'r') as myfile:
        data = myfile.read().replace('\n', '')

    regex1 = r"STARTME---(\d+)"
    regex2 = r"STOPME---(\d+)"
    startTime = re.findall(regex1, data)
    stopTime = re.findall(regex2, data)
    diff = len(startTime) - len(stopTime)
    i = 0
    for file_ in listdir_nohidden(path):
        count = 0
        while float(startTime[count]) < float(content[i])*1000:
            print(count)
            count = count + 1
        startStamp = float(startTime[count]) - float(content[i])*1000
        stopStamp = float(stopTime[count-diff]) - float(content[i])*1000
        dir = path+'/'+file_
        aggregated.append(stopStamp-startStamp)
        i = i + 1
    aggregated = [x for x in aggregated if str(x) != 'nan']
    return aggregated


def Average(lst):
    return sum(lst) / len(lst)


def description(data):
    data = np.asarray(data)
    median = np.median(data)
    upper_quartile = np.percentile(data, 75)
    lower_quartile = np.percentile(data, 25)

    iqr = upper_quartile - lower_quartile
    upper_whisker = data[data<=upper_quartile+1.5*iqr].max()
    lower_whisker = data[data>=lower_quartile-1.5*iqr].min()
    print(round(median,2))
    print(round(upper_quartile,2))
    print(round(lower_quartile,2))
    print(round(iqr,2))
    print(round(upper_whisker,2))
    print(round(lower_whisker,4))

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
#         './2018.06.20_133136/data/nexus7/httpfewvunlktn470androidindex8html/comandroidchrome/trepn', 'timestampsort/timestampsort50k.txt', 'timestampsort/logsort50k.txt'),
#         aggregate_data(
#         './2018.06.20_184624/data/nexus7/httpfewvunlktn470androidindex9html/comandroidchrome/trepn', 'timestampsort/timestampsort100k.txt', 'logsort100k.txt'),
#         aggregate_data(
#         './2018.06.20_184624/data/nexus7/httpfewvunlktn470androidindex10html/comandroidchrome/trepn', 'timestampsort/timestampsort200k.txt', 'logsort100k.txt')]

# Get http request
# data = [aggregate_data('./2018.06.24_212100/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestamphttprequest200.txt', 'loghttprequest200.txt'),
#         aggregate_data('./2018.06.24_235013/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestamphttprequest500.txt', 'loghttprequest500.txt'),
#         aggregate_data('./2018.06.25_080146/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestamphttprequest1k.txt', 'loghttprequest1k.txt')]

# # date
# data = [aggregate_data('./2018.06.23_192048/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampdate100k.txt', 'logdate.txt'),
#         aggregate_data('./2018.06.23_192048/data/nexus7/httpsadhiviraptgithubioblah/comandroidchrome/trepn', 'timestampdate200k.txt', 'logdate.txt'),
#         aggregate_data('./2018.06.23_192048/data/nexus7/httpsadhiviraptgithubioblah2/comandroidchrome/trepn', 'timestampdate300k.txt', 'logdate.txt')]

# localstoragemain
# data = [aggregate_data('./2018.06.21_200130/data/nexus7/httpsfewvunlktn470androidindex11html/comandroidchrome/trepn','./timestamplocalstorage/timestamplocalstorage100k.txt', './timestamplocalstorage/loglocalstorage100k.txt'),
#          aggregate_data('./2018.06.19_213356/data/nexus7/httpfewvunlktn470androidindex2html/comandroidchrome/trepn','./timestamplocalstorage/timestamplocalstorage200k.txt', './timestamplocalstorage/loglocalstorage200k.txt'),
#          aggregate_data('./2018.06.19_192126/data/nexus7/httpfewvunlktn470androidindex3html/comandroidchrome/trepn','./timestamplocalstorage/timestamplocalstorage300k.txt', './timestamplocalstorage/loglocalstorage300k.txt')]

# mic
# data = [aggregate_data('./2018.06.22_100331/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampmic.txt', 'logmic.txt'),
#         aggregate_data('./2018.06.22_140614/data/nexus7/httpsadhiviraptgithubioblah/comandroidchrome/trepn', 'timestampmic2.txt', 'logmic2.txt'),
#         aggregate_data('./2018.06.22_202621/data/nexus7/httpsadhiviraptgithubioblah2/comandroidchrome/trepn', 'timestampmic3.txt', 'logmic3.txt')]

# camera
# data = [aggregate_data('./2018.06.24_010830/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampcamera10k.txt', 'logcamera.txt'),
#         aggregate_data('./2018.06.24_134030/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampcamera30k.txt', 'logcamera30.txt'),
#         aggregate_data('./2018.06.24_174457/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampcamera60k.txt', 'logcamera60k.txt')]



# camera test
# data = [aggregate_data('./2018.06.17_154840/data/nexus7/localhost8000/comandroidchrome/trepn', 'timestampcamera5k.txt', 'logcamera5k.txt'),
#         aggregate_data('./2018.06.17_154840/data/nexus7/localhost8000/comandroidchrome/trepn',
#                        'timestampcamera10k.txt', 'logcamera10k.txt'),
#         aggregate_data('./2018.06.17_170430/data/nexus7/localhost8000/comandroidchrome/trepn',
#                        'timestampcamera20k.txt', 'logcamera20k.txt')]

# session storage
# data = [aggregate_data('./2018.06.25_130041/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn', 'timestampsessionstorage100k.txt', 'sessionrequest100k.txt'),
#         aggregate_data('./2018.06.25_150837/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn',
#                     'timestampsessionstorage200k.txt', 'sessionrequest200k.txt'),
#         aggregate_data('./2018.06.25_233647/data/nexus7/httpsadhiviraptgithubio/comandroidchrome/trepn',
                    # 'timestampsessionstorage300k.txt', 'sessionrequest300k.txt')]


# Show plot
plt.ylabel("Energy in Joule", size=15)
plt.title('Session storage test', size=19, fontweight='bold')
plt.boxplot(data, 0, '', showmeans=True)
plt.xticks([1, 2, 3], ['100000 calls',
                       '200000 calls', '300000 calls'], size=15)
plt.figure(figsize=(2, 1), dpi=120)
plt.show()
