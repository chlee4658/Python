import pandas as pd

# 1. 경기결과 수집히기
import pandas as pd


# 1. 경기결과 불러오기
mlb_result = pd.read_csv("./data/mlb_result_2018.csv")
len(mlb_result)
mlb_result.head()


# 2. 투구, 타격 기록 불러오기
pitch = pd.read_csv("./data/mlb_record_pitch_2018.csv")
hit = pd.read_csv("./data/mlb_record_hit1_2018.csv")
pitch.dtypes


# 3. 팀평균 방어율 구하기
pitch["ER_9"] = pitch["ER"] * 9
pitch_team = pitch.groupby(["team", "month"])["ER_9","IP"].sum()
pitch_team = pitch_team.reset_index(drop=False)
pitch_team["ERA"] = pitch_team["ER_9"] / pitch_team["IP"]


# 4. 경기결과와 투구, 타격 기록 합치기
hit["month_aft"] = hit["month"] + 1
pitch_team["month_aft"] = pitch_team["month"] + 1

hit_1 = hit.rename(columns = {"AVG":"AVG_1"})
hit_2 = hit.rename(columns = {"AVG":"AVG_2"})

hit_1 = hit_1[["team", "month_aft", "AVG_1"]]
hit_2 = hit_2[["team", "month_aft", "AVG_2"]]

pitch_team_1 = pitch_team.rename(columns = {"ERA":"ERA_1"})
pitch_team_2 = pitch_team.rename(columns = {"ERA":"ERA_2"})

pitch_team_1 = pitch_team_1[["team", "month_aft", "ERA_1"]]
pitch_team_2 = pitch_team_2[["team", "month_aft", "ERA_2"]]

mlb_result["month"] = mlb_result["date"] / 100
mlb_result["month"] = mlb_result["month"].astype(int)

mlb_result1 = pd.merge(mlb_result, hit_1, left_on=["team1", "month"],
                       right_on=["team", "month_aft"], how="left")
mlb_result1 = mlb_result1.drop(["team","month_aft"],1)
mlb_result1 = pd.merge(mlb_result1, hit_2, left_on=["team2", "month"],
                       right_on=["team", "month_aft"], how="left")
mlb_result1 = mlb_result1.drop(["team","month_aft"],1)
mlb_result1 = pd.merge(mlb_result1, pitch_team_1, left_on=["team1", "month"],
                       right_on=["team", "month_aft"], how="left")
mlb_result1 = mlb_result1.drop(["team","month_aft"],1)
mlb_result1 = pd.merge(mlb_result1, pitch_team_2, left_on=["team2", "month"],
                       right_on=["team", "month_aft"], how="left")
mlb_result1 = mlb_result1.drop(["team","month_aft"],1)


# 5. 승패 기록 변환하기
print("before: {}".format(len(mlb_result))+", after: {}".format(len(mlb_result1)))

mlb_result1["win_cls"] = ""
mlb_result1["win_cls"][mlb_result1["score1"]<mlb_result1["score2"]] = "2team win"
mlb_result1["win_cls"][mlb_result1["score1"]>mlb_result1["score2"]] = "1team win"
mlb_result1["win_cls"][mlb_result1["score1"]==mlb_result1["score2"]] = "even"


# 6. 그래프 그리기
import seaborn as sns

sns.countplot(x="win_cls", data=mlb_result1)

mlb_result1["target"]=0
mlb_result1["target"][mlb_result1["score1"]>mlb_result1["score2"]] = 1

mlb_result1["avg_dif"] = mlb_result1["AVG_1"] - mlb_result1["AVG_2"]
mlb_result1["era_dif"] = mlb_result1["ERA_1"] - mlb_result1["ERA_2"]

mlb_result1 = mlb_result1[mlb_result1["AVG_1"].isna()==False]
mlb_result1 = mlb_result1.reset_index(drop=True)


# 7. 의사결정트리 알고리즘에 학습시키기

from sklearn.model_selection import train_test_split

mlb_result2 = mlb_result1[["target", "avg_dif", "era_dif", "AVG_1", "AVG_2", "ERA_1", "ERA_2"]]
# mlb_result2 = mlb_result1[["target", "avg_dif", "era_dif"]]
mlb_train, mlb_test = train_test_split(mlb_result2, test_size=0.3, random_state=1)

from sklearn import tree

dt = tree.DecisionTreeClassifier(max_depth=2)
clf = dt.fit(mlb_train.drop("target",1), mlb_train["target"])


# 8. 알고리즘 평가히기

from sklearn.metrics import accuracy_score

train_pre = clf.predict(mlb_train.drop("target",1))
print(accuracy_score(mlb_train["target"], train_pre))

test_pre = clf.predict(mlb_test.drop("target",1))
accuracy_score(mlb_test["target"], test_pre)


# 9.의사결정나무 그림 그리기
import pydot

filename="./output/tree.dot"
filename1="./output/tree.png"

with open(filename,"w") as f:
    tree.export_graphviz(clf, out_file=f,feature_names = list(mlb_train.drop("target",1).columns), filled=True, proportion=True, rounded=True,special_characters=True)

(graph,) = pydot.graph_from_dot_file(filename)
graph.write_png(filename1)
