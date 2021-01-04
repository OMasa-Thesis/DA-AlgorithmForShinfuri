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



df_univcap = np.loadtxt("localpathunivcap.txt", delimiter=',', dtype='int64')


def mean_unmatch(path, K,p,method):
    #plt.style.use('ggplot')
    #font = {'family': 'meiryo'}
    #mpl.rc('font', **font)

    df = pd.read_csv(path, sep=",", header=None)
    df_boollist = []
    df_meanlist = []


    for i in range(K):
        mean = df.mean(axis='columns', skipna=True).copy()
        df_meanlist.append([method,p,mean[4]])
        df_bool = (df.iloc[5 * i + 3, :] == 0)
        df_boollist.append([method,p,df_bool.sum()])


    return df_boollist,df_meanlist


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


#Hard用の分析
df_univcap = np.tile(df_univcap,(10,1))

for i in range(11):
    path = makepath_H_univ(0.0 + i*0.1,0.5 + i*0.05)
    if i == 0:
        df_H_tmp = np.loadtxt(path, delimiter=',', dtype='int64')
        df_H = df_univcap - df_H_tmp
    else:
        df_H_tmp=  np.loadtxt(path, delimiter=',', dtype='int64')
        df_Hadd = df_univcap - df_H_tmp
        df_H = np.concatenate([df_H, df_Hadd], 0) 


df_H_sum = df_H[:,1::].sum(axis=1)
df_rest_sitei = []
df_rest_zenka = []
df_rest_unmatch = []
for i in range(11):
    for j in range(10):
        df_rest_sitei.append(["H",i*0.1,df_H_sum[i*50 +j*5]+ df_H_sum[i*50 +j*5+1] + df_H_sum[i*50 +j*5+2]])
        df_rest_zenka.append(["H",i*0.1,df_H_sum[i*50 +j*5+3]])
        df_rest_unmatch.append(["H",i*0.1,800 - df_H[i*50 +j*5,0]])


#df_rest_sitei= list(itertools.chain.from_iterable(df_rest_sitei))
df_rest_sitei= pd.DataFrame(df_rest_sitei,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_sitei['prob'], y=df_rest_sitei['num'],label="残指定科類枠")
df_rest_zenka= pd.DataFrame(df_rest_zenka,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_zenka['prob'], y=df_rest_zenka['num'],label="残全科類枠")
df_rest_unmatch= pd.DataFrame(df_rest_unmatch,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_unmatch['prob'], y=df_rest_unmatch['num'],label="留年者数")

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', prop={"family":"IPAexGothic"},borderaxespad=0, fontsize=18)


# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("人数", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)
plt.savefig('Hard_univ_notitle.pdf')
plt.title("Hard方式 進学枠利用状況", fontname="IPAexGothic", fontsize=22)
plt.savefig('Hard_univ.pdf')
plt.show()
##終了




#Soft用の分析


for i in range(11):
    path = makepath_S_univ(0.0 + i*0.1,0.5 + i*0.05)
    if i == 0:
        df_S_tmp = np.loadtxt(path, delimiter=',', dtype='int64')
        df_S = df_univcap - df_S_tmp
    else:
        df_S_tmp=  np.loadtxt(path, delimiter=',', dtype='int64')
        df_Sadd = df_univcap - df_S_tmp
        df_S = np.concatenate([df_S, df_Sadd], 0) 


df_S_sum = df_S[:,1::].sum(axis=1)
df_rest_sitei = []
df_rest_zenka = []
df_rest_unmatch = []
for i in range(11):
    for j in range(10):
        df_rest_sitei.append(["H",i*0.1,df_S_sum[i*50 +j*5]+ df_S_sum[i*50 +j*5+1] + df_S_sum[i*50 +j*5+2]])
        df_rest_zenka.append(["H",i*0.1,df_S_sum[i*50 +j*5+3]])
        df_rest_unmatch.append(["H",i*0.1,800 - df_S[i*50 +j*5,0]])


#df_rest_sitei= list(itertools.chain.from_iterable(df_rest_sitei))
df_rest_sitei= pd.DataFrame(df_rest_sitei,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_sitei['prob'], y=df_rest_sitei['num'],label="残指定科類枠")
df_rest_zenka= pd.DataFrame(df_rest_zenka,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_zenka['prob'], y=df_rest_zenka['num'],label="残全科類枠")
df_rest_unmatch= pd.DataFrame(df_rest_unmatch,columns=['meathod', 'prob', 'num'])
sns.regplot(x=df_rest_unmatch['prob'], y=df_rest_unmatch['num'],label="留年者数")

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', prop={"family":"IPAexGothic"},borderaxespad=0, fontsize=18)


# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("人数", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)
plt.savefig('Soft_univ_notitle.pdf')
plt.title("Soft方式 進学枠利用状況", fontname="IPAexGothic", fontsize=22)
plt.savefig('Soft_univ.pdf')

plt.show()
##終了




  