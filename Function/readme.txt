



---datamake----(H,S共通)
#データフレームのダウンロード(H,S共通)
def make_df(csv):
# n:学生数#m:科類の学生数k:学科数
def stu_num():(H,S共通)
#typeは科類、aは指定科類枠方、Bは同じ文理枠内
def make_prelist():(H,S共通)
def make_pre(pre_list, type, a, b):
    #typeはl1 =0,l2=1,,s3=5


# 学生のデータの作成。
# # student(0:学生番号,1科類2点数3内定学科4Time5選好)
#n = 1076    m = [113, 151, 150, 443, 190, 29]k = 79
def make_stu(n, m, k, a, b):
# 大学のデータの作成。(Hard用)
def univ_make(df, df_collist):
# 大学のデータの作成。(Soft用)
def univ_make_s(df, df_collist):



---dafunc_H---(H用)
def da_H(student, univ, df_collist):
現行方式(Hard)のDAを実行する。
一回の関数実行で1回のアプライのステップを行うため、未内定(student[i][3] == -1)がいなくなるまで実行する必要あり。




---dafunc_S---(S用)
def da_H(student, univ, df_collist):
MInority Reserve方式(Soft)のDAを実行する。
一回の関数実行で1回のアプライのステップを行うため、未内定(student[i][3] == -1)がいなくなるまで実行する必要あり。
実装方針は、基本的には最初は指定科類枠科類分も全科類枠で持っておき、
指定科類枠がきたときには
指定科類枠を一枠
全科類枠を一枠 減らす。




---simulation---(H,S共通)
#cnt:シミュレーション の実行回数 a :Aの確率b:Bの確率,rand = seedの決定
a,bの条件は 0< a < b <1
def simulation(cnt, a, b, rand):

a,bの条件は 0< a < b <1
#cnt:シミュレーション の実行回数 a :Aの確率b:Bの確率,rand = seedの決定
def simulation_s(cnt, a, b, rand):

---simu_run---(H,S共通)
シミュレーションを実行する。
返り値は
学生
0学生番号、
1科類、
2点数
3内定場所、
4内定先志望順位
×シミュレーション 回数となっている。
結果はurl = 'localpath' +  シミュレーション 回数 + "-" + 確率A + "-" + 確率B + 'DA実施方式.txt'の順で保存される。

返り値は大学のデータフレームのうち、
0指定科類枠第1内定者数、
1指定科類枠第2内定者数、
2指定科類枠第3内定者数、
3指定科類枠第4内定者数、
4合計内定者数
×シミュレーション 回数となっている。
結果はurl_univ = 'localpath' + シミュレーション 回数 + "-" + 確率A + "-" + 確率B + 'DA実施方式_univ.txt'順で保存される。

#a =start ,b=finish ,c間隔
def make_interval(a, b, c):
#Nシミュレーション 回数, interval_list = [[A,B]]の確率のリスト, rand:乱数のseed
def run_simulation_s(N, interval_list, rand):
#Nシミュレーション 回数, interval_list = [[A,B]]の確率のリスト, rand:乱数のseed
def run_simulation(N, interval_list, rand):




#４章のシミュレーションで用いたグラフの生成に用いた。パッケージはmatpltlibとseabornを中心に用いた。
#3つのファイルはそれぞれ以下のグラフに対応している。
analyzemain
    留年者（unmatch）数
    内定先志望順位（平均）
analyzehist
    内定先志望順位（累積）ヒストグラム
analyzeuniv
    進学単位の指定科類枠、全科類枠の消費数

---analyzemain---
留年者（unmatch）数と内定先志望順位（平均）を生成する。

---analyzehist---
内定先志望順位（累積）ヒストグラムを生成する。

---analyzeuniv---
進学単位の指定科類枠、全科類枠の消費数を生成する。