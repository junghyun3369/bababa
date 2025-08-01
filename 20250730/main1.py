import pandas as pd
import numpy as np

data = np.array([1,2,3,4,5])
r = data * 3
print(r)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# # print(pd.__version__)

# a = [1,2,3,4]
# # a = ["1","2","3","4"]
# i = ["인1","2","3","4"]
# data = pd.Series(data=a, index=i)
# print(data)
# # loc[] iloc[]
# print(data.loc["인1"], data.iloc[0])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++


# data = pd.Series(data=[1,2,3,4])
# print(data[ : ]) #1,2

# a= [1,2,3,4]
# print(a[ : ]) # 1~2

# data = pd.Series(data=[3.0, 5.0, 7.0, 9.0])
# print(data) 

# data = pd.Series(data=["가","나", "다"])
# print(data) 

# data = pd.Series([3.0, 5.0, 7.0, 9.0], ["가","나", "다", "라"])
# print(data) 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# idx = ["1행", "2행", "3행"]
# col = ["첫번째", "두번째", "세번째"]
# data = pd.DataFrame(data=arr, index=idx, columns=col)
# # print(data[1:2])
# print(data.loc["2행"])
# # print(type(data.loc["2행"]))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++


# data = pd.read_csv("./data1.csv", index_col=0)
# # print(data.index)
# # print(type(data))
# # print(data.loc["row1"])
# for i in data.index:
#     s = data.loc[i]
#     dan = s.loc["dan"]
#     num = s.loc["num"]
#     print(f'{dan} * {num} = {dan * num}')
#     # for r in s:
#     #     print(r)
#     # print((i))
#     # print(data.loc[i])
