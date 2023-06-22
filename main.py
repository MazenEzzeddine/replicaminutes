from datetime import datetime



def readTextFile():
    with open('myfile.txt') as f:
        lines = f.readlines()
    print(type(lines))
    values = []
    for idx, i in enumerate(lines):

        j = i.split()
        values.append(j[1])
        values.append(j[6])
    return values




def createReplicas(values):
    s = set()
    replicas = []
    for idx, i in enumerate(values):
        if idx % 2 == 0 :
            continue
        replicas.append(i)
        s= set(replicas)
    return replicas, s


def replicaMinutes(replica, values):
    startTime = values[values.index(replica) -1]
    datetime_obj1 = datetime.strptime(
        startTime, '%Y-%m-%dT%H:%M:%SZ')
    tmp = values[values.index(replica)+1:]
    endTime = tmp[tmp.index(replica) -1]
    datetime_obj2 = datetime.strptime(
        endTime, '%Y-%m-%dT%H:%M:%SZ')
    if datetime_obj2 > datetime_obj1 :
        t = datetime_obj2 - datetime_obj1
    else:
        t = datetime_obj1 - datetime_obj2

    print(t.seconds )
    return t.seconds;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    values = readTextFile()
    replicas, replicaset = createReplicas(values)
    print(replicas)
    print(replicaset)
    totalreplicaminutes = 0;
    for replica in replicaset:
        totalreplicaminutes += replicaMinutes(replica, values)
    print(totalreplicaminutes/60)




