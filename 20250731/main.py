import pandas as pd

# data = pd.Series([1,2,3,4], ['행1','행2','행3','행4'])
# print(data.loc['행2':'행3'])
# print(data.loc['행2':'행3'].drop('행3'))
# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# idx=['행1','행2','행3']
# col=['열1','열2','열3']
# data1 = pd.DataFrame(arr, idx, col)
# print(data1)
# data2 = pd.DataFrame(arr[1:], idx[1:], col)
# print(data2)

# data3 = data1 + data2
# print(data3)
# # s = pd.Series(data1.loc) 틀린 코드  - 데이터를 선택하는 명령어(기능) 자체를 데이터로 사용하려고 했기 때문에
# # s = pd.Series(arr[:1], idx[:1])
# s = pd.Series()
# print(data3 + s)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a1 = [60, 84, 80, 70, 19]
# a2 = [77, 62, 95, 85, 17]
# a3 = [61, 97, 72, 67, 15]
# a4 = [75, 65, 95, 51, 18]
# cols = ["국어", "영어", "수학", "과학", "나이"]
# idx = ["A","B","C","D"]
# data = pd.DataFrame([a1, a2, a3, a4], index=idx, columns=cols)
# # print(data.sort_values(by=['수학','영어'], ascending=[0,1]))
# # 위의 성적표에서 수학점수가 동률인 것만 출력.
# d1 = data["수학"].sort_values(ascending=False)
# cnt = d1.value_counts()
# print(cnt[cnt > 1])
# print()
# print(cnt[cnt > 1].index[0])
# print()
# print(d1 == cnt[cnt > 1].index[0])
# print()
# print(d1[d1 == cnt[cnt > 1].index[0]])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# data = pd.read_csv('./data1_20220731.csv')
# # print(data)

# # Q2 위의 인구수 표에서 '세대수'가 가장 높은 동명은 무엇인가요?
# d1 = data.sort_values(by='세대수',ascending=False)
# print("Q2", d1.loc[0].loc['동명'])

# # Q3 위의 인구수 표에서 '남(65세 이상)' 인구수가 높은 동명은 무엇인가요?
# d2 = data.sort_values(by='남(65세이상)',ascending=False)
# print("Q3", d2.iloc[0].loc['동명'])

# # Q4 위의 인구수 표에서 '세대수'의 평균 이상 인구수의 동명은 무엇인가요? 
# 평균값 = data['세대수'].mean().astype(int)
# d3 = data[data['세대수'] >= 평균값]
# print("Q4",d3['동명'])

# max_index1 = data['세대수'].idxmax()
# data1 = data.loc[max_index1, '동명']
# print(f"1.{data1}")

# max_index = data['남(65세이상)'].idxmax()
# data2 = data.loc[max_index, '동명']
# print(f"2.{data2}")

# condition = data['세대수'] >= 평균값
# filtered_data = data[condition]
# data3 = filtered_data['동명']
# a =data3.iloc[0]
# print(f"3.{a}")


