# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
from datetime import datetime

import matplotlib.pyplot as plt



def readFile():
    with open('logs.csv', 'r') as f:
        return f.readlines()


def plot(latencies):
    plt.plot(latencies)
    #plt.axis([0, 30000, 0, 1500])
    plt.show()

def printTimeLatency(latencies, time):
    print ("idx \t\t time \t\t\t\t\t\t\t  latency")
    print("0 \t\t\t" + str(time[0]) + "\t\t\t" + str(latencies[0]))
    for idx in reversed(range(len(latencies))):
        print(str(idx) + "\t\t\t" + str(time[idx]) + "\t\t\t" + str(latencies[idx]))


if __name__ == '__main__':
    counter = 0
    latencies = []
    time = []
    lines = readFile()
    # for line in lines:
    #     print(line)
    for line in lines:
        words = line.split(',')

        lat= re.findall(r'\d+', words[15])
        latencies.append(int(lat[7]))
        temp = str(words[16])
        temp= temp.replace('\n', '')
        datetime_obj2 = datetime.strptime(
            temp[:-4], '%Y-%m-%dT%H:%M:%S.%f')
        time.append(datetime_obj2)
        if int(lat[7]) > 500:
            counter +=1



    print(time[0])
    print(time[len(time) - 200])
    print(time[len(time)-1])
    print((time[0]- time[len(time)-1]).seconds)
    plot(latencies)
    print ((1 - (counter / len(latencies)))*100)
    printTimeLatency(latencies, time)







