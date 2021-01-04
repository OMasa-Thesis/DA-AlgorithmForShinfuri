import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake

#df_collist =[['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号'], ['第二段階指定2科類', '第二段階指定2枠数', '指定2残席', '指定2底点', '指定2点数', '指定2学籍番号'], ['第二段階指定3科類', '第二段階指定3枠数', '指定3残席', '指定3底点', '指定3点数', '指定3学籍番号'], ['第二段階指定4科類', '第二段階指定4科類.1', '指定4残席', '指定4底点', '指定4点数', '指定4学籍番号']]


def da_s(student, univ_s, df_collist):
    n, m, k = datamake.stu_num()
    #上から処理を実行
    for i in range(1, n + 1):
        #もし未内定だったら
        if student[i][3] == -1:
            point = student[i][2]  # student[i][2]は点数
            t = student[i][4]  # student[i][4]はtimes
            applyn = int(
                student[i][int(5 +
                               t)])  # student[i][5+t]は申し込み学科。applyn は申し込み学科

            #j = ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
            flag = False

            for count in range(4):
                # 申し込み学科に枠があり、そこ点がiより高い場合
                if (str(int(student[i][1]))
                        in univ_s[df_collist[count][0]].iloc[applyn]) and (
                            univ_s[df_collist[count][1]].iloc[applyn] !=
                            0) and (univ_s[df_collist[count][3]].iloc[applyn] <
                                    point):
                    flag = True

                    # 申し込み学科に残席があり

                    student[i][3] = applyn
                    # change_point:申し込み学科から追い出される学生の学籍番号の場所
                    change_point = np.argmin(
                        univ_s[df_collist[count][4]].iloc[applyn])
                    change_stu = univ_s[df_collist[count]
                                        [5]].iloc[applyn][change_point]
                    if change_stu != 0:
                        student[int(change_stu)][3] = -1
                        student[int(change_stu)][4] -= 1

                    univ_s[df_collist[count]
                           [4]].iloc[applyn][change_point] = point
                    univ_s[df_collist[count]
                           [5]].iloc[applyn][change_point] = student[i][0]
                    univ_s[df_collist[count][3]].iloc[applyn] = np.amin(
                        univ_s[df_collist[count][4]].iloc[applyn])

                    if univ_s[df_collist[count]
                              [2]].iloc[applyn] == 0 and count == 3:
                        break
                    elif univ_s[df_collist[count]
                                [2]].iloc[applyn] > 0 and count == 3:
                        univ_s[df_collist[count][2]].iloc[applyn] -= 1
                        break

                    elif univ_s[df_collist[count]
                                [2]].iloc[applyn] == 0 and count != 3:
                        break
                    else:  #a依存関係のある枠のチェック
                        #依存があったら1枠を減らす、人が押し出されるかみる　押し出された人はdp=-1,t=-1にセット
                        univ_s[df_collist[count][2]].iloc[applyn] -= 1
                        for R in range(1, 4 - count):
                            if ((univ_s[df_collist[count][0]].iloc[applyn]
                                 ) in (univ_s[df_collist[count +
                                                         R][0]].iloc[applyn])):
                                # 依存先学科に残席があり
                                if ((univ_s[df_collist[count +
                                                       R][1]].iloc[applyn] > 0)
                                        and (univ_s[df_collist[count + R]
                                                    [2]].iloc[applyn] > 0)):
                                    #依存先学科の残席と枠を削る

                                    univ_s[df_collist[count +
                                                      R][1]].iloc[applyn] -= 1
                                    univ_s[df_collist[count +
                                                      R][2]].iloc[applyn] -= 1
                                    #change_point_2は10000点0番の学生で埋める

                                    change_point_2 = np.argmin(
                                        univ_s[df_collist[count +
                                                          R][4]].iloc[applyn])
                                    univ_s[df_collist[count + R][4]].iloc[
                                        applyn][change_point_2] = 10000
                                    univ_s[df_collist[
                                        count +
                                        R][5]].iloc[applyn][change_point_2] = 0
                                    univ_s[df_collist[count + R]
                                           [3]].iloc[applyn] = np.amin(
                                               univ_s[df_collist[count + R]
                                                      [4]].iloc[applyn])
                                    # 依存先学科に残席がなし
                                elif (
                                    (univ_s[df_collist[count +
                                                       R][1]].iloc[applyn] > 0)
                                        and
                                    (univ_s[df_collist[count +
                                                       R][2]].iloc[applyn]
                                     == 0)):
                                    # 依存先学科の枠数を削減
                                    univ_s[df_collist[count +
                                                      R][1]].iloc[applyn] -= 1
                                    change_point_3 = np.argmin(
                                        univ_s[df_collist[count +
                                                          R][4]].iloc[applyn])
                                    change_stu_3 = univ_s[df_collist[
                                        count +
                                        R][5]].iloc[applyn][change_point_3]

                                    student[int(change_stu_3)][3] = -1
                                    student[int(change_stu_3)][4] -= 1
                                    univ_s[df_collist[count + R][4]].iloc[
                                        applyn][change_point_3] = 10000
                                    univ_s[df_collist[
                                        count +
                                        R][5]].iloc[applyn][change_point_3] = 0
                                    univ_s[df_collist[count + R]
                                           [3]].iloc[applyn] = np.amin(
                                               univ_s[df_collist[count + R]
                                                      [4]].iloc[applyn])
                                else:
                                    break

                if flag == True:
                    break
                else:
                    continue

                    # 申し込み学科に残席があり

                    #iを仮内定処理

                    # print(univ_s[df_collist[count][4]].iloc[applyn])
                    # 申し込み学科から追い出される学生の処理

            student[i][4] = t + 1

    return student, univ_s
