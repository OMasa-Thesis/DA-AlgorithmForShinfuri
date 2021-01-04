import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake
import dafunc_H
import dafunc_S
import simulation
import matplotlib
#matplotlib inline
import matplotlib.pyplot as plt


#a =start ,b=finish ,c間隔
def make_interval(a, b, c):
    d = int((b - a) / c) + 1
    inter = []
    for i in range(d):
        inter.append([round(a + i * c, 2), round(1 / 2 + (a + i * c) / 2, 2)])

    return inter


#Nシミュレーション 回数, interval_list = [[A,B]]の確率のリスト, rand:乱数のseed
def run_simulation(N, interval_list, rand):
    K = len(interval_list)
    for i in range(K):
        simulation.simulation(N, interval_list[i][0], interval_list[i][1],
                              rand)


#Nシミュレーション 回数, interval_list = [[A,B]]の確率のリスト, rand:乱数のseed
def run_simulation_s(N, interval_list, rand):
    K = len(interval_list)
    for i in range(K):
        simulation.simulation_s(N, interval_list[i][0], interval_list[i][1],
                                rand)


interval = make_interval(0.0, 1.0, 0.1)
#interval = make_interval(0.0, 1.0, 0.1)
#print(interval)
print("ready")
#run_simulation(10, interval, 100)
run_simulation_s(10, interval, 100)
print("done")

