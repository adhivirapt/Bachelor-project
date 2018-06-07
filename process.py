import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks_cwt


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def get_averagePower(dir, startStamp, stopStamp):
    csv = pd.read_csv(dir, skiprows=3)
    index = csv['Battery Power* [uW]'].index[csv['Battery Power* [uW]'].apply(
        pd.isnull)]
    csv = csv[:index[0]].astype(str).astype(float)
    print("imhere")
    print(startStamp)
    print(stopStamp)
    print(find_nearest(csv['Time  [ms]'], startStamp))
    print(find_nearest(csv['Time  [ms]'], stopStamp))
    print("imnothere")
    averagePower = ((csv['Battery Power* [uW]'].sum() /
                     index[0]) * csv.iloc[index[0]-1, 0])/(1000000 * 1000)

    print(averagePower)
    return averagePower


def find_nearest(array, value):
#     a = []
#     for row in array:
#         a.append(row)
#     print(value)
    array = np.asarray(array)
#     subs = array[:] = [x - value for x in array]
#     idx = subs.argmin()
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def aggregate_data(folder, startStamp, stopStamp):
    path = folder  # use your path
    data = []
    counter = 0
    for file_ in listdir_nohidden(path):
        dir = path+'/'+file_
        data.append(get_averagePower(dir, startStamp, stopStamp))
    return data


with open('log1.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

regex1 = r"STARTME---(\d+)"
regex2 = r"STOPME---(\d+)"
startTime = re.search(regex1, data).group(0)[10:23]
stopTime = re.search(regex2, data).group(0)[9:22]
# with open("timestamp.txt", "a") as text_file:
#     text_file.write(startTime.group(0)[10:23]+'\n')
#     text_file.write(stopTime.group(0)[9:22]+'\n')

with open("timestamp.txt", "r") as text_file:
    content = text_file.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

while float(content[0])<float(content[0])*100:
        
startStamp = float(content[1]) - float(content[0])*100
stopStamp = float(content[2]) - float(content[0])*100

aggregate_data(
    './example/web/output/2018.06.07_173525/data/nexus7/localhost8000/comandroidchrome/trepn', startStamp, stopStamp)


# font = {'family' : 'normal',
#         'weight' : 'bold',
#         'size'   : 18}

# plt.rc('font', **font)

# # fig, ax = plt.subplots()
# # data = [aggregate_data('./control3'),
# #         aggregate_data('./cpusort_50000'),
# #         # aggregate_data('./cpusort_50000'),
# #         aggregate_data('./cpusort_100000')]
# # ax.boxplot(data, 0, '', showmeans=True)

# # plt.ylabel('Energy (kJ)')
# # # plt.xticks([1, 2, 3, 4], ['Control', 'cpusort_1000',
# # #                           'cpusort_5000', 'cpusort_10000'])
# # plt.show()

# def graph(formula, x_range):
#     x = np.array(x_range)
#     y = eval(formula)
#     plt.plot(x, y)


# fig, ax = plt.subplots()
# data = [aggregate_data('/Users/AdhiviraTheodorus/Downloads/haha/example/web/output/2018.06.06_182452'),
#         aggregate_data('./cpusort_50000'),
#         aggregate_data('./cpusort_100000'),
#         aggregate_data('./cpusort_200000')]


#         # aggregate_data('./cpusort_200000')]
# # datamean = [aggregate_data('./control2'),
# #         aggregate_data('./cpudate_1000'),
# #         aggregate_data('./cpudate_5000'),
# #         aggregate_data('./cpudate_10000')]
# # ]
# print(np.corrcoef(data))
# ax.boxplot(data,0,'', showmeans=True)

# plt.ylabel('Energy (kJ)')
# # plt.xticks([1, 2, 3, 4], ['Control', 'cpusort_1000',
# #                           'cpusort_5000', 'cpusort_10000'])
# plt.show()
