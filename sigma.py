#!/usr/bin/python3

#Indexes
density = -3
population = 5
region = 1
area = 11

#Data manipulation
data = open("canada.tsv", "r", encoding="latin1")
data = data.readlines()
header = data[0]
canada = data[1]
data = data[2:]
data = list(map(lambda x: x.split("\t"), data))
data = sorted(data, key=lambda x: float(x[density]), reverse=True)
print("Entries: " + str(len(data)))


#consts
total_population = 35151728
total_area = 8965588.85

def sigma(percent):
    print("To get " + str(percent * 100) + "% of the population you need")
    running_total = 0
    count = 0
    running_area_total = 0
    while running_total < total_population * percent:
        region_name = data[count][region]
        region_population = data[count][population]
        running_total += int(data[count][population])
        running_area_total += float(data[count][area])
        #print(data[count][population])
        print(region_name + ": " + region_population)
        count += 1
    print(str((running_area_total * 100)/total_area) + "% of the area")
    print(count)
#Jamerais subbed for margarite
#sigma(0.5)
#sigma(0.6827)
sigma(0.9545)
#sigma(0.9973)
