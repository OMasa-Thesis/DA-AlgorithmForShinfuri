import pandas as pd
import numpy as np
import datetime as dt
import random
import csv
import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
mpl.font_manager._rebuild()
#mpl.rcParameters['font.family'] = 'IPAexGothic'





def mean_unmatch(path, K,p,method):
    plt.style.use('ggplot')
    #font = {'family': 'meiryo'}
    #mpl.rc('font', **font)

    df = pd.read_csv(path, sep=",", header=None)
    df_histlist = []



    for i in range(K):
        df_hist = df.iloc[5 * i + 4, :] 
        df_histlist.append([method,p,df_hist ])


    return df_histlist


def makepath_H(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "localpath10-" + str(a) +"-" + str(b) + "DA-H.txt"
  
  return path

def makepath_H_univ(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "localpath10-" + str(a) +"-" + str(b) + "DA-H_univ.txt"
  
  return path

def makepath_S(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "localpath10-" + str(a) +"-" + str(b) + "DA-S.txt"
  return path

def makepath_S_univ(a,b):

  a = round(a, 1)
  b = round(b, 2)
  
  path = "localpath10-" + str(a) +"-" + str(b) + "DA-S_univ.txt"
  return path






hist_H = []
hist_S  = []

DF_list = [hist_H,hist_S]

for i in range(11):
  path = makepath_H(0.0 + i*0.1,0.5 + i*0.05)
  a = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"H")
  hist_H.append(a)






for i in range(11):
  path = makepath_S(0.0 + i*0.1,0.5 + i*0.05)
  a = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"S")
  hist_S.append(a)

"""
##各方式ごとの指定科類枠志望率別ヒストグラムを作成する
##Soft方式の指定科類枠志望率別ヒストグラム
bins = np.linspace(-1, 90, 50)
for i in range(0,11):
    plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    

    plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    plt.ylabel("度数", fontname="IPAexGothic")
    plt.xlim(-1, 85)
    plt.ylim(0,900)

    plt.legend(loc='upper right')
    plt.savefig("S-0" +str(i) + "hist_notitle.pdf")
    plt.title("Soft方式 内定志望順位", fontname="IPAexGothic",fontsize=22)
    plt.savefig("S-0" +str(i) + "hist.pdf")


    plt.close()
##Hard方式の指定科類枠志望率別ヒストグラム
bins = np.linspace(-1, 90, 50)
for i in range(0,11):
    plt.hist( hist_H[i][0][2::], bins, alpha = 0.5, label='H0'+str(i))
    

    plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    plt.ylabel("度数", fontname="IPAexGothic")
    plt.xlim(-1, 85)
    plt.ylim(0,900)

    plt.legend(loc='upper right')
    plt.savefig("H-0" +str(i) + "hist_notitle.pdf")
    plt.title("Hard方式 内定志望順位", fontname="IPAexGothic",fontsize=22)
    plt.savefig("H-0" +str(i) + "hist.pdf")

    plt.close()
"""
##各方式ごとの指定科類枠志望率別ヒストグラムを一枚に乗っけたものを作成する
##Soft方式の指定科類枠志望率別ヒストグラム
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
bins = np.linspace(-1, 80, 50)

for i in range(0,10):
    #ab = plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    axes[i//5, i%5].set_xlim(-1, 85)
    axes[i//5, i%5].set_ylim(0,900)
    axes[i//5, i%5].set(title= str(i))
    
    
    axes[i//5, i%5].hist( hist_S[i][0][2::], bins,color = "b" ,alpha = 0.5, label='S0'+str(i))
    axes[i//5, i%5].legend(loc='upper right')
    
    #plt.title("Soft内定志望順位", fontname="IPAexGothic")

    #plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    #plt.ylabel("度数", fontname="IPAexGothic")
    

    

plt.savefig("Shist_notitle.pdf")
fig.suptitle("Soft内定志望順位", fontname="IPAexGothic",fontsize = 22)
plt.savefig("Shist.pdf")
plt.close()

##Hard方式の指定科類枠志望率別ヒストグラム
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
bins = np.linspace(-1, 80, 50)

for i in range(0,10):
    #ab = plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    axes[i//5, i%5].set_xlim(-1, 85)
    axes[i//5, i%5].set_ylim(0,900)
    axes[i//5, i%5].set(title= str(i))
    
    
    axes[i//5, i%5].hist( hist_H[i][0][2::], bins,color = "r" ,alpha = 0.5, label='H0'+str(i))
    axes[i//5, i%5].legend(loc='upper right')
    
    #plt.title("Hard内定志望順位", fontname="IPAexGothic")

    #plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    #plt.ylabel("度数", fontname="IPAexGothic")
    

    

plt.savefig("Hhist_notitle.pdf")
fig.suptitle("Hard内定志望順位", fontname="IPAexGothic",fontsize = 22)
plt.savefig("Hhist.pdf")
plt.close()

