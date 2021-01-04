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


#Seedのセット。


# n:学生数#m:科類の学生数k:学科数
def stu_num():
    m = [113, 151, 150, 443, 190, 29]
    n = sum(m)

    k = 79
    return n, m, k


# 選好リストの作成の関数


#typeは科類、aは指定科類枠方、Bは同じ文理枠内
def make_prelist():
    pre_l_1a = [1]
    pre_l_1b = list(range(2, 21))
    pre_l_1c = list(range(21, 79))
    pre_l_1 = [pre_l_1a, pre_l_1b, pre_l_1c]

    pre_l_2a = [2]
    pre_l_2b = [1] + list(range(3, 21))
    pre_l_2c = list(range(21, 79))
    pre_l_2 = [pre_l_2a, pre_l_2b, pre_l_2c]

    pre_l_3a = list(range(3, 18))
    pre_l_3b = [1, 2] + list(range(18, 21))
    pre_l_3c = list(range(21, 79))
    pre_l_3 = [pre_l_3a, pre_l_3b, pre_l_3c]

    pre_s_1a = list(range(46, 79))
    pre_s_1b = list(range(21, 27)) + list(range(29, 46))
    pre_s_1c = list(range(1, 21))
    pre_s_1 = [pre_s_1a, pre_s_1b, pre_s_1c]

    pre_s_2a = list(range(69, 79)) + list(range(29, 46))
    pre_s_2b = list(range(21, 27)) + list(range(46, 69))
    pre_s_2c = list(range(1, 21))
    pre_s_2 = [pre_s_2a, pre_s_2b, pre_s_2c]

    pre_s_3a = [30]
    pre_s_3b = [29] + list(range(31, 78))
    pre_s_3c = list(range(1, 29))
    pre_s_3 = [pre_s_3a, pre_s_3b, pre_s_3c]
    pre_list = [pre_l_1, pre_l_2, pre_l_3, pre_s_1, pre_s_2, pre_s_3]
    return pre_list


def make_pre(pre_list, type, a, b):
    #typeはl1 =0,l2=1,,s3=5
    tmp = random.random()
    if tmp < a / 2:
        key = [0, 1, 2]
    elif a / 2 <= tmp < a:
        key = [0, 2, 1]
    elif a <= tmp < (a + b) / 2:
        key = [1, 0, 2]
    elif (a + b) / 2 <= tmp < b:
        key = [1, 2, 0]
    elif b / 2 <= tmp < (1 + b) / 2:
        key = [2, 0, 1]
    elif (1 + b) / 2 <= tmp < 1:
        key = [2, 1, 0]

    pre_result = []
    for i in key:
        random.shuffle(pre_list[type][i])
        pre_result.extend(pre_list[type][i])
        #ここバグってる

    while len(pre_result) < 80:
        pre_result.extend([0])
    #pre_resultの要素は79こ
    return pre_result


# 学生のデータの作成。
# # student(0:学生番号,1科類2点数3内定学科4Time5選好)
#n = 1076    m = [113, 151, 150, 443, 190, 29]k = 79
def make_stu(n, m, k, a, b):
    tmp = 0
    tmp_2 = ["1", "2", "3", "4", "5", "6"]
    cus_m = np.cumsum(m)
    pre_list = make_prelist()

    student = np.zeros((n + 1, k + 5))
    for i in range(1, n + 1):
        #0には学生番号、2には点数、3には内定学科（最初は-1）を入れる
        student[i][0] = i
        student[i][2] = random.randrange(11, 9998, 1)
        student[i][3] = -1
        # make_prefを使う
        student[i][1] = tmp_2[tmp]

        pre = make_pre(pre_list, tmp, a, b)
        #(0-77)
        for j in range(k - 1):
            student[i][5 + j] = pre[j]

        if cus_m[tmp] == i:
            tmp += 1

    return student


#student = make_stu(n, m)


# 大学のデータの作成。Hard用
# ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
def univ_make(df, df_collist):
    for j in df_collist:
        df[j[0]] = df[j[0]].astype('str')
        df[j[2]] = df[j[1]]
        df[j[4]] = df[j[1]].apply(lambda x: np.zeros((x)))
        df[j[5]] = df[j[1]].apply(lambda x: np.zeros((x)))

    # ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
    return df


# 大学のデータの作成。(Soft用)
def univ_make_s(df, df_collist):
    univ_s = df.copy()
    for j in df_collist:
        univ_s[j[0]] = univ_s[j[0]].astype('str')

    for index, row in df.iterrows():
        for k in range(3):
            for l in range(1, 4 - k):
                if (univ_s.iloc[index][df_collist[k][0]]
                        in univ_s.iloc[index][df_collist[l + k][0]]):
                    ext = df.at[index, df_collist[k][1]].copy()
                    univ_s.at[index, df_collist[l + k][1]] += ext

    for j in df_collist:
        univ_s[j[2]] = univ_s[j[1]].copy()
        univ_s[j[4]] = univ_s[j[1]].apply(lambda x: np.zeros((x)))
        univ_s[j[5]] = univ_s[j[1]].apply(lambda x: np.zeros((x)))

    # ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
    return univ_s


#df_r = univ_make_s(df, df_collist)
#print(df_r.iloc[2]['第二段階指定1科類'] in df_r.iloc[2]['第二段階指定4科類'])

#print(univ_make_s(df, df_collist))

