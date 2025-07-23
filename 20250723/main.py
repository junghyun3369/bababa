# a = "문자열"

# print(a[-1:])

# a = [1,2,3,4,5]

# print(a[1:3])
# for v in a:
#     print(v)

# a = [
#     [1,2,3],
#     [4,5,6,7],
# ]

# b = [8,9]
# del a[1:]
# a.append(b)

# a[-1:] = [b]
# a[1][:] = b

# a[1:] = [b] # << 문제 a[:] 이용하여 b의 리스트로 변경하기!!

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = {'k1':10, 'k2':20}
# b = {'k1':30}

# arr1 = [a]
# arr2 = [b]
# arr1[0]['k1'] = arr2[0]['k1']
# #[{'k1':10, 'k2':20}]
# #[{'k1':30}]
# print(arr1)
# # print(arr2)
# # [{'k1':30, 'k2':20}] <<문제 결과 출력 되려면

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = {"k1":10, "k2":20}
# b = {"k1": '케이1', "k2": '케이2'}
# c = {"k1":True, "k2":False}

# arr = [a,b,c]
# #리스트 행중에 값이 논리형(불)인 행을 출력하기
# print(arr[-1])
# if type(arr[0]['k1']) == bool:
#     print(arr[0])
# if type(arr[1]['k1']) == bool:
#     print(arr[1])
# if type(arr[2]['k1']) == bool:
#     print(arr[2])


# for row in arr:
#     for key in row:
#         if type(row[key]) == bool:
#             print(f'{key} : {row[key]}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = [
  {'no': 1, 'title': 'Python'},
  {'no': 2, 'title': 'JavaScript'},
  {'no': 3, 'title': 'CSS'}
  ]
# print(type(a), a)
b = tuple(a)
b[1]['title'] = 'Java'

# 1. 슬라이싱을 이용하여 선택적 값 변경
# b[1]['title'] = b[1]['title'][:4]

# 2. 해당 key인 `no`의 값을 확인 후 슬라이싱 방법으로 값 변경
# for row in b:
#   if row['no'] == 2:
#     row['title'] = row['title'][:4]

print(b)






