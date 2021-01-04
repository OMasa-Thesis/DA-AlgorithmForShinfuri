import pandas as pd
import numpy as np
import random
import csv
import pprint


#データフレームのダウンロード
def make_df(csv):
    df = pd.read_csv(csv)
    #'/Users/masato/Desktop/UTTdata/prog/PyProgramming/sinhuri2018.csv'

    # print(df)
    df_col = list(df.columns)[4::]
    df_collist = []
    for i in range(0, 24, 6):
        df_collist.append(df_col[i:i + 6:])

    return df, df_collist
stu_cnt =[0,0,0,0,0,0,0] 
def univ_make(df, df_collist):
    for j in df_collist:
        df[j[0]] = df[j[0]].astype('str')
        df[j[2]] = df[j[1]]
        df[j[4]] = df[j[1]].apply(lambda x: np.zeros((x)))
        df[j[5]] = df[j[1]].apply(lambda x: np.zeros((x)))

    # ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
    return df

df, df_collist = make_df("/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/csvdata/sinhuri2018.csv")
df_univ = univ_make(df, df_collist)


def cnt_stu_common(df_univ,stu_cnt):
    for i in range(1,7,1):
        for j in range(1,79,1):
            if str(i) in df.iloc[j,4]:
                stu_cnt[i] += df.iloc[j,5]
            if str(i) in df.iloc[j,10]:
                stu_cnt[i] += df.iloc[j,11]
            if str(i) in df.iloc[j,16]:
                stu_cnt[i] += df.iloc[j,17]
            if str(i) in df.iloc[j,22]:
                stu_cnt[i] += df.iloc[j,23]
    stu_cnt[0] = sum(stu_cnt[1::])
    stu_cnt_np = np.array(stu_cnt)

    return stu_cnt_np

def cnt_stu_withoutzenka(df_univ,stu_cnt):
    for i in range(1,7,1):
        for j in range(1,79,1):
            if str(i) in df.iloc[j,4]:
                stu_cnt[i] += df.iloc[j,5]
            if str(i) in df.iloc[j,10]:
                stu_cnt[i] += df.iloc[j,11]
            if str(i) in df.iloc[j,16]:
                stu_cnt[i] += df.iloc[j,17]
    stu_cnt[0] = sum(stu_cnt[1::])
    stu_cnt_np = np.array(stu_cnt)

    return stu_cnt_np

def cnt_stu_keisya(df_univ,stu_cnt):
    for i in range(1,7,1):
        for j in range(1,79,1):
            if str(i) in df.iloc[j,4]:
                stu_cnt[i] += (df.iloc[j,5]/len(df.iloc[j,4]))
            if str(i) in df.iloc[j,10]:
                stu_cnt[i] += (df.iloc[j,11]/len(df.iloc[j,10]))
            if str(i) in df.iloc[j,16]:
                stu_cnt[i] += (df.iloc[j,17] /len(df.iloc[j,16]))
            if str(i) in df.iloc[j,22]:
                stu_cnt[i] += (df.iloc[j,23] /len(df.iloc[j,22])) 
    stu_cnt[0] = sum(stu_cnt[1::])
    stu_cnt_np = np.array(stu_cnt)

    return stu_cnt_np


def cnt_stu_keisya_withoutzenka(df_univ,stu_cnt):
    for i in range(1,7,1):
        for j in range(1,79,1):
            if str(i) in df.iloc[j,4]:
                stu_cnt[i] += (df.iloc[j,5]/len(df.iloc[j,4]))
            if str(i) in df.iloc[j,10]:
                stu_cnt[i] += (df.iloc[j,11]/len(df.iloc[j,10]))
            if str(i) in df.iloc[j,16]:
                stu_cnt[i] += (df.iloc[j,17] /len(df.iloc[j,16]))

    stu_cnt[0] = sum(stu_cnt[1::])
    stu_cnt_np = np.array(stu_cnt)

    return stu_cnt_np

def cal_rate(stu_num,stulist,result_df):
    result_df = np.vstack((result_df,stulist))
    rate = (stulist/stu_num)*100
    print("学生数に対する枠の準備率")
    print(rate)
    result_df = np.vstack((result_df,rate))
    husoku = stulist - stu_num
    print("学生数に対する枠の不足数")
    print(husoku)
    result_df = np.vstack((result_df,husoku))
    return result_df


result_df = np.array([0,1,2,3,4,5,6])
stu_num = np.array([1076,113 ,151 ,150 ,443 ,190 ,29])
stu_cnt =np.array([0,0,0,0,0,0,0] )
stu_cnt_common = cnt_stu_common(df_univ,stu_cnt)
print(stu_cnt_common)
result_df = cal_rate(stu_num,stu_cnt_common,result_df)

stu_num = np.array([1076,113 ,151 ,150 ,443 ,190 ,29])
stu_cnt =np.array([0,0,0,0,0,0,0] )
stu_cnt_withoutzenka= cnt_stu_withoutzenka(df_univ,stu_cnt)
print(stu_cnt_withoutzenka)
result_df = cal_rate(stu_num,stu_cnt_withoutzenka,result_df)


stu_num = np.array([1076,113 ,151 ,150 ,443 ,190 ,29])
stu_cnt =np.array([0,0,0,0,0,0,0] )
stu_cnt_keisya = cnt_stu_keisya(df_univ,stu_cnt)
print(stu_cnt_keisya)
result_df = cal_rate(stu_num,stu_cnt_keisya,result_df)

stu_num = np.array([1076,113 ,151 ,150 ,443 ,190 ,29])
stu_cnt =np.array([0,0,0,0,0,0,0] )
stu_cnt_keisya_withoutzenka = cnt_stu_keisya_withoutzenka(df_univ,stu_cnt)
print(stu_cnt_keisya_withoutzenka)
result_df = cal_rate(stu_num,stu_cnt_keisya_withoutzenka,result_df)

url = 'localpathsitei_cal.txt'
np.savetxt(url, result_df, delimiter=',')

