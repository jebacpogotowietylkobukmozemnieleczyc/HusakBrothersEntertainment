#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv as csv
import numpy as np


def avg(table):
    sum = 0
    for value in table:
        sum += value
    return sum / len(table)


def mul100(i):
    return i * 100


def div1000(i):
    return i / 1000


def readdata(filename, generationall, effortall, runall):
    with open(filename, 'r') as f:
        read = csv.reader(f)
        newtable = []
        generation = []
        effort = []
        run = []
        inteffort = []
        for row in read:
            newrow = []
            for data in row:
                newrow.append(data)
            newtable.append(newrow)
        newtable.pop(0)
        for row in newtable:
            generation.append(int(row[0]))
            effort.append(int(row[1]))
            introw = list(map(float, row))
            run.append(avg(introw[2:]))
    generationall.append(generation)
    effortall.append(effort)
    runall.append(run)


def main():
    generationall = []
    effortall = []
    runall = []
    readdata("cel.csv", generationall, effortall, runall)
    readdata("2cel.csv", generationall, effortall, runall)
    readdata("cel-rs.csv", generationall, effortall, runall)
    readdata("2cel-rs.csv", generationall, effortall, runall)
    readdata("rsel.csv", generationall, effortall, runall)

    plt.figure(figsize=(14, 8))
    sp = plt.subplot(1, 2, 1)
    ax2 = sp.twiny()
    sp.set_ylabel('Odsetek wygranych gier [%]')
    sp.set_xlabel('Rozegranych gier (x1000)')
    sp.grid()
    effortall[3][196] = 499850
    effortall[3][197] = 499950
    effortall[3][198] = 499950
    effortall[3][199] = 499999
    sp.plot(list(map(div1000, effortall[0])), list(map(mul100, runall[0])), label='cel', linestyle='-', marker='o',
            markevery=20)
    sp.plot(list(map(div1000, effortall[1])), list(map(mul100, runall[1])), label='2cel', linestyle='-', marker='^',
            markevery=20)
    sp.plot(list(map(div1000, effortall[2])), list(map(mul100, runall[2])), label='cel-res', linestyle='-', marker='s',
            markevery=20)
    sp.plot(list(map(div1000, effortall[3])), list(map(mul100, runall[3])), label='2cel-rs', linestyle='-', marker='p',
            markevery=20)
    sp.plot(list(map(div1000, effortall[4])), list(map(mul100, runall[4])), label='rsel', linestyle='-', marker='D',
            markevery=20)
    sp.legend(loc='lower right')
    print(generationall)
    new_tick_locations = np.array([0.2, 0.5, 0.9])
    # ax2.set_xticks([0.2, 0.5, 0.9])
    ax2.set_xticklabels([0, 40, 80, 120, 160, 200])
    ax2.set_xlabel("Pokolenie")
    # sp.plot(effortall[0], runall[0], label='cel')
    # ax2.plot(generationall[0], list(map(mul100,runall[0])) )
    # ax2.plot(generationall[1], list(map(mul100,runall[1])) )
    # ax2.plot(generationall[2], list(map(mul100,runall[2])) )
    # ax2.plot(generationall[3], list(map(mul100,runall[3])) )
    # ax2.plot(generationall[4], list(map(mul100,runall[4])) )
    # ax2.cla()
    sp2 = plt.subplot(1, 2, 2)
    labels = ['cel', '2cel', 'cel-rs', '2cel-rs', 'rsel']
    sp2.boxplot(runall, labels=labels, showmeans=True, notch=True)
    sp2.grid()
    plt.savefig('myplot.pdf')
    plt.close()


if __name__ == '__main__':
    main()
