#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

targetrange = []
result = []

with open('speeds.csv', 'r') as inputfile:
    reader = csv.reader(inputfile, dialect = 'excel')
    header = next(reader)
    index = 0
    for title in header:
        if title in [
            '201603050000',
            '201603110000',
            '201603120000',
            '201603180000',
            '201603190000',
            '201603260000',
            '201604020000',
            '201604090000',
            '201604110000',
            '201604160000',
            '201604190000',
        ]:
            targetrange.append(index)
        if title in [
            '201603070000',
            '201603120000',
            '201603140000',
            '201603190000',
            '201603210000',
            '201603280000',
            '201604050000',
            '201604110000',
            '201604120000',
            '201604180000',
            '201604200000',
        ]:
            targetrange.append(index)
        index = index + 1

with open('speeds.csv', 'r') as inputfile:
    reader = csv.reader(inputfile, dialect = 'excel')
    for row in reader:
        for count in range(12, -1, -2):
            for _ in range(targetrange[count], targetrange[count + 1]):
                row.pop(targetrange[count])
        result.append(row)




with open('speeds_without_zero.csv', 'w') as outputfile:
    writer = csv.writer(outputfile, dialect = 'excel')
    for row in result:
        writer.writerow(row)
