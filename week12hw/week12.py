#! usr/bin/env python

import numpy
import sys
import matplotlib.pyplot as plt
import matplotlib.text as txt


def Wright_Fischer(population, af = 0.5):
    list_af = []
    while (af < 1) and (af > 0):
        simulation = numpy.random.binomial(population, af)
        af = simulation/population
        list_af.append(af)
    return(list_af)
    
def plotter():
    data = Wright_Fischer(100, 0.5)
    # print(data)
    generation = list(range(len(data)))
    # print(generation)
    fig, ax = plt.subplots()
    ax.plot(generation, data)
    plt.xlabel('generation')
    plt.ylabel('allele frequency')
    # plt.ylim(0,1)
    plt.title("Population = 100, AF = 0.5")
    # plt.show()
    plt.savefig("Firstplot.png")
    
def hister():
    simulate = []
    for p in range(1000):
        data = Wright_Fischer(100, 0.5)
        settime = len(data)
        simulate.append(settime)
    # print(simulate)
    fig, ax = plt.subplots()
    ax.hist(simulate)
    plt.xlabel('Population Set Time')
    plt.ylabel('Frequency')
    plt.title("Population = 100, AF = 0.5, 1000 iters")
    # plt.show()
    plt.savefig("Secondplot.png")

def pops():
    settime = []
    population = []
    for p in [123, 1234, 12345, 123456, 1234567, 10000000]:
        data = Wright_Fischer(p, 0.5)
        population.append(p)
        settime.append(len(data))
    fig,ax = plt.subplots()
    ax.plot(population, settime)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('population size')
    plt.xticks(ticks = population)
    plt.ylabel('Set Time')
    # plt.show()
    plt.savefig("Thirdplot.png")


def varied():
    freqs = [0.23, 0.45, 0.73, 0.13, 0.34, 0.54, 0.89, 0.12, 0.63, 0.48]
    settime = numpy.zeros((100, len(freqs)))
    for p in range(settime.shape[1]):
        for q in range(settime.shape[0]):
            settime[q][p]=len(Wright_Fischer(100,freqs[p]))
    fig,ax = plt.subplots()
    plt.xlabel('Starting Frequencies')
    plt.ylabel('fix time')
    plt.title('Population = 100')
    ax.violinplot(settime, positions = [1,2,3,4,5,6,7,8,9,10], showextrema = False, showmeans = True, widths = 1.0)
    plt.xticks(ticks = [1,2,3,4,5,6,7,8,9,10], labels = freqs)
    # plt.show()
    plt.savefig("lastplot.png")
        
varied()