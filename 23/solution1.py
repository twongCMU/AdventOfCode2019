#!/usr/bin/python3

from intcode import intcode
import numpy as np
import sys
import math
import os

data = [3,62,1001,62,11,10,109,2221,105,1,0,2025,915,1295,1165,2161,1130,1095,1697,1922,1889,777,1037,1994,740,645,1464,977,1730,886,1392,1264,1557,2190,610,711,1066,1526,1326,571,1823,1357,1957,1860,1429,1623,1008,855,1656,814,946,1792,1588,1495,1196,2066,2130,1233,2095,682,1763,0,0,0,0,0,0,0,0,0,0,0,0,3,64,1008,64,-1,62,1006,62,88,1006,61,170,1106,0,73,3,65,21001,64,0,1,20102,1,66,2,21101,105,0,0,1106,0,436,1201,1,-1,64,1007,64,0,62,1005,62,73,7,64,67,62,1006,62,73,1002,64,2,133,1,133,68,133,102,1,0,62,1001,133,1,140,8,0,65,63,2,63,62,62,1005,62,73,1002,64,2,161,1,161,68,161,1101,0,1,0,1001,161,1,169,102,1,65,0,1101,0,1,61,1102,0,1,63,7,63,67,62,1006,62,203,1002,63,2,194,1,68,194,194,1006,0,73,1001,63,1,63,1105,1,178,21102,1,210,0,105,1,69,1202,1,1,70,1101,0,0,63,7,63,71,62,1006,62,250,1002,63,2,234,1,72,234,234,4,0,101,1,234,240,4,0,4,70,1001,63,1,63,1106,0,218,1105,1,73,109,4,21102,1,0,-3,21101,0,0,-2,20207,-2,67,-1,1206,-1,293,1202,-2,2,283,101,1,283,283,1,68,283,283,22001,0,-3,-3,21201,-2,1,-2,1106,0,263,22102,1,-3,-3,109,-4,2106,0,0,109,4,21101,1,0,-3,21102,1,0,-2,20207,-2,67,-1,1206,-1,342,1202,-2,2,332,101,1,332,332,1,68,332,332,22002,0,-3,-3,21201,-2,1,-2,1105,1,312,21201,-3,0,-3,109,-4,2105,1,0,109,1,101,1,68,358,21001,0,0,1,101,3,68,366,21002,0,1,2,21101,376,0,0,1106,0,436,21202,1,1,0,109,-1,2105,1,0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776,2199023255552,4398046511104,8796093022208,17592186044416,35184372088832,70368744177664,140737488355328,281474976710656,562949953421312,1125899906842624,109,8,21202,-6,10,-5,22207,-7,-5,-5,1205,-5,521,21101,0,0,-4,21102,0,1,-3,21102,51,1,-2,21201,-2,-1,-2,1201,-2,385,470,21001,0,0,-1,21202,-3,2,-3,22207,-7,-1,-5,1205,-5,496,21201,-3,1,-3,22102,-1,-1,-5,22201,-7,-5,-7,22207,-3,-6,-5,1205,-5,515,22102,-1,-6,-5,22201,-3,-5,-3,22201,-1,-4,-4,1205,-2,461,1105,1,547,21101,0,-1,-4,21202,-6,-1,-6,21207,-7,0,-5,1205,-5,547,22201,-7,-6,-7,21201,-4,1,-4,1106,0,529,21201,-4,0,-7,109,-8,2106,0,0,109,1,101,1,68,564,20102,1,0,0,109,-1,2106,0,0,1101,97859,0,66,1101,0,5,67,1101,0,598,68,1102,302,1,69,1102,1,1,71,1102,1,608,72,1105,1,73,0,0,0,0,0,0,0,0,0,0,14,137828,1102,19753,1,66,1102,1,3,67,1102,637,1,68,1101,0,302,69,1102,1,1,71,1102,1,643,72,1106,0,73,0,0,0,0,0,0,14,103371,1101,34457,0,66,1102,1,4,67,1102,1,672,68,1101,253,0,69,1101,1,0,71,1102,1,680,72,1106,0,73,0,0,0,0,0,0,0,0,7,15767,1102,1,72077,66,1102,1,1,67,1102,709,1,68,1101,556,0,69,1101,0,0,71,1101,711,0,72,1105,1,73,1,1361,1102,1,99689,66,1102,1,1,67,1101,0,738,68,1102,1,556,69,1101,0,0,71,1101,740,0,72,1105,1,73,1,1236,1101,0,59453,66,1101,4,0,67,1102,767,1,68,1102,253,1,69,1101,0,1,71,1101,775,0,72,1105,1,73,0,0,0,0,0,0,0,0,34,55073,1102,1,92567,66,1102,1,1,67,1101,0,804,68,1102,1,556,69,1102,1,4,71,1101,0,806,72,1105,1,73,1,5,28,97859,19,96797,19,387188,38,153346,1102,76673,1,66,1101,0,6,67,1102,841,1,68,1102,1,302,69,1101,0,1,71,1102,1,853,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,34,110146,1101,20681,0,66,1101,1,0,67,1101,0,882,68,1101,0,556,69,1101,1,0,71,1102,884,1,72,1105,1,73,1,1213,29,303172,1101,101869,0,66,1102,1,1,67,1101,0,913,68,1101,0,556,69,1102,0,1,71,1101,0,915,72,1106,0,73,1,1247,1101,53887,0,66,1101,0,1,67,1102,942,1,68,1102,556,1,69,1102,1,1,71,1102,944,1,72,1105,1,73,1,125,19,193594,1101,0,33569,66,1102,1,1,67,1101,0,973,68,1102,556,1,69,1101,0,1,71,1101,0,975,72,1106,0,73,1,101,28,489295,1101,0,58567,66,1101,0,1,67,1101,0,1004,68,1101,0,556,69,1101,0,1,71,1102,1006,1,72,1105,1,73,1,81,47,64453,1101,0,81563,66,1101,1,0,67,1101,1035,0,68,1101,556,0,69,1102,1,0,71,1102,1037,1,72,1106,0,73,1,1220,1102,53359,1,66,1102,1,1,67,1101,1064,0,68,1102,556,1,69,1102,1,0,71,1101,1066,0,72,1105,1,73,1,1591,1101,0,30893,66,1102,1,1,67,1102,1,1093,68,1101,556,0,69,1102,0,1,71,1101,1095,0,72,1106,0,73,1,1286,1101,359,0,66,1102,1,1,67,1102,1,1122,68,1102,556,1,69,1102,3,1,71,1102,1124,1,72,1106,0,73,1,3,17,34361,33,35978,47,193359,1102,1,95651,66,1101,0,3,67,1101,0,1157,68,1102,1,302,69,1102,1,1,71,1102,1,1163,72,1106,0,73,0,0,0,0,0,0,13,237812,1102,1,17189,66,1102,1,1,67,1101,0,1192,68,1101,0,556,69,1101,0,1,71,1102,1194,1,72,1105,1,73,1,-211,47,128906,1102,1,77081,66,1102,4,1,67,1102,1,1223,68,1102,1,302,69,1102,1,1,71,1102,1231,1,72,1106,0,73,0,0,0,0,0,0,0,0,14,34457,1101,97973,0,66,1101,1,0,67,1101,1260,0,68,1102,556,1,69,1102,1,1,71,1101,0,1262,72,1105,1,73,1,211,33,53967,1101,0,9767,66,1101,0,1,67,1102,1,1291,68,1102,1,556,69,1101,1,0,71,1102,1,1293,72,1106,0,73,1,13,23,19753,1101,40063,0,66,1102,1,1,67,1102,1322,1,68,1101,556,0,69,1102,1,1,71,1101,1324,0,72,1105,1,73,1,-540,31,54962,1101,96997,0,66,1102,1,1,67,1101,0,1353,68,1101,556,0,69,1101,1,0,71,1102,1,1355,72,1106,0,73,1,83,31,27481,1101,94463,0,66,1102,1,1,67,1101,0,1384,68,1101,0,556,69,1101,3,0,71,1102,1386,1,72,1105,1,73,1,10,28,195718,19,290391,38,76673,1102,1,96797,66,1102,4,1,67,1101,1419,0,68,1102,302,1,69,1102,1,1,71,1101,0,1427,72,1106,0,73,0,0,0,0,0,0,0,0,38,306692,1101,17989,0,66,1101,3,0,67,1102,1,1456,68,1102,1,302,69,1102,1,1,71,1102,1,1462,72,1105,1,73,0,0,0,0,0,0,13,59453,1102,1289,1,66,1102,1,1,67,1101,0,1491,68,1101,0,556,69,1101,0,1,71,1102,1,1493,72,1106,0,73,1,1271,43,231243,1101,0,42577,66,1102,1,1,67,1101,0,1522,68,1101,556,0,69,1101,0,1,71,1102,1,1524,72,1105,1,73,1,9349,29,75793,1102,1,93287,66,1101,1,0,67,1101,0,1553,68,1102,556,1,69,1101,1,0,71,1102,1555,1,72,1105,1,73,1,139,29,151586,1101,16699,0,66,1101,1,0,67,1102,1584,1,68,1102,556,1,69,1102,1,1,71,1101,1586,0,72,1105,1,73,1,27,7,31534,1101,44483,0,66,1101,1,0,67,1102,1,1615,68,1101,0,556,69,1102,1,3,71,1102,1,1617,72,1106,0,73,1,1,23,39506,43,154162,29,227379,1102,55073,1,66,1101,2,0,67,1102,1650,1,68,1102,351,1,69,1102,1,1,71,1101,1654,0,72,1106,0,73,0,0,0,0,255,6551,1102,71861,1,66,1102,1,1,67,1101,1683,0,68,1101,556,0,69,1101,0,6,71,1102,1685,1,72,1106,0,73,1,2,31,109924,28,293577,28,391436,43,77081,38,383365,38,460038,1101,15767,0,66,1102,2,1,67,1101,0,1724,68,1101,302,0,69,1102,1,1,71,1102,1,1728,72,1105,1,73,0,0,0,0,17,68722,1102,1,34361,66,1102,1,2,67,1102,1,1757,68,1102,302,1,69,1102,1,1,71,1101,1761,0,72,1105,1,73,0,0,0,0,33,17989,1101,47581,0,66,1102,1,1,67,1102,1790,1,68,1101,556,0,69,1101,0,0,71,1102,1,1792,72,1106,0,73,1,1363,1102,58171,1,66,1101,1,0,67,1102,1819,1,68,1102,556,1,69,1102,1,1,71,1101,1821,0,72,1105,1,73,1,983,43,308324,1101,0,75793,66,1102,1,4,67,1102,1,1850,68,1101,0,302,69,1101,1,0,71,1102,1,1858,72,1106,0,73,0,0,0,0,0,0,0,0,9,81758,1101,48073,0,66,1102,1,1,67,1101,1887,0,68,1101,556,0,69,1102,1,0,71,1101,0,1889,72,1106,0,73,1,1173,1101,0,40879,66,1101,0,2,67,1102,1916,1,68,1102,302,1,69,1102,1,1,71,1102,1920,1,72,1105,1,73,0,0,0,0,13,118906,1101,0,74891,66,1102,1,3,67,1101,0,1949,68,1102,1,302,69,1101,1,0,71,1101,0,1955,72,1106,0,73,0,0,0,0,0,0,13,178359,1101,0,27481,66,1101,0,4,67,1102,1,1984,68,1101,0,302,69,1102,1,1,71,1101,1992,0,72,1106,0,73,0,0,0,0,0,0,0,0,14,68914,1102,1,71171,66,1101,1,0,67,1102,2021,1,68,1101,556,0,69,1101,0,1,71,1102,1,2023,72,1106,0,73,1,160,38,230019,1102,6551,1,66,1101,0,1,67,1101,2052,0,68,1101,556,0,69,1102,6,1,71,1101,2054,0,72,1105,1,73,1,26954,9,40879,8,74891,8,149782,5,95651,5,191302,5,286953,1101,16661,0,66,1101,0,1,67,1101,0,2093,68,1101,556,0,69,1101,0,0,71,1101,2095,0,72,1106,0,73,1,1283,1101,0,64453,66,1101,3,0,67,1101,2122,0,68,1102,302,1,69,1101,0,1,71,1102,2128,1,72,1106,0,73,0,0,0,0,0,0,8,224673,1101,0,69481,66,1101,0,1,67,1101,0,2157,68,1102,556,1,69,1102,1,1,71,1102,2159,1,72,1105,1,73,1,36319,23,59259,1101,48989,0,66,1101,1,0,67,1101,0,2188,68,1102,1,556,69,1102,0,1,71,1102,1,2190,72,1105,1,73,1,1308,1101,15461,0,66,1101,1,0,67,1102,2217,1,68,1102,556,1,69,1102,1,1,71,1101,2219,0,72,1105,1,73,1,4,31,82443]

#data.extend([0]*1000)

num_computers = 50

computers = []
queues = []
nat_data = None
nat_data_last_y = None
for i in range(num_computers):
    computers.append(intcode(data.copy(), True))
    queues.append([]) # the initialization id
    computers[i].intcode_computer([i])
    
round = 0
while 1:

    for i in range(num_computers):
        print("Round " + str(round) + " computer "  + str(i))

        inputs = []

        if len(queues[i]) > 0:
            data = queues[i].pop(0)

            print("sending packet")
            status0 = computers[i].intcode_computer([data[0]])
            status0 = computers[i].intcode_computer([data[1]])
            while 1:
                status1 = computers[i].intcode_computer([-1])
                if status1 is None:
                    break
                status2 = computers[i].intcode_computer([-1])
                status3 = computers[i].intcode_computer([-1])

                if status1 == 255:
                    print("OOH2 " + str(status1) + " " + str(status2) + " " + str(status3))
                    nat_data = (status2, status3)
                    #exit()
                else:
                    print("Got packet for " + str(status1) + " " + str(status2) + " " + str(status3))
                    queues[status1].append((status2, status3))

        else:
            while 1:
                status1 = computers[i].intcode_computer([-1])
                if status1 is None:
                    break
                status2 = computers[i].intcode_computer([-1])
                status3 = computers[i].intcode_computer([-1])

                if status1 == 255:
                    print("OOH1 " + str(status1) + " " + str(status2) + " " + str(status3))
                    nat_data = (status2, status3)
                    #exit() # part 1
                else:
                    print("Got packet for " + str(status1) + " " + str(status2) + " " + str(status3))
                    queues[status1].append((status2, status3))
        if status1 is None:
            continue

    all_idle = True
    for i in range(num_computers):
        if len(queues[i]) > 0:
            all_idle = False
            break
    if all_idle and nat_data is not None:
        queues[0].append((nat_data[0], nat_data[1]))

        if nat_data_last_y is not None and nat_data_last_y == nat_data[1]:
            print("WOO got double y " + str(nat_data_last_y))
            exit()
        nat_data_last_y = nat_data[1]
    round += 1
