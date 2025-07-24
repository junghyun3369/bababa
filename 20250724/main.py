# a = {}

# if a:
#     print("참")
# else:
#     print("거짓")


# a = [
#   {'k1': {}},
#   [1]
# ]

# for v in a:
#   print(v)
# # {'k1': {}}
# # [1]
#   for t in v:
#     if :
#       print("참")
#     else :
#       print("거짓")
# # k1 = 거짓
# # 1 = 참

# a = [
#   {'k1': {}},
#   [1]
# ]

# for v in a:
#   for t in v:
#     # 자료형 비교하여 값을 비교에 사용할 수 있다.
#     if v[t] if type(v) == dict else t :
#       print(t ,"참")
#     else :
#       print(t, "거짓")
# # k1 > 거짓
# # 1  > 참

# +++++++++++++++++++++++++++++++++++++++++++++

# # a = 5
# # while a >= 0:
# #     print(a, '출력')
# #     a -= 1

# i = 5
# for j in range(i + 1):
#     print(i - j, '출력')


# print("while문으로 실행")
# i = 5
# while i >= 0:
#   print(i, '출력')
#   i -= 1

# print("for문으로 실행")
# i = 5
# for j in range(i+1):
#   # 최대값 변수에서 회전 변수를 빼기 하여 역순으로 출력 가능
#   print(i - j, '출력')

# # range함수의 속성을 이용하여 역순으로 출력 가능
# for j in range(5, -1, -1):
#   print(j, '출력')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# i = 1
# arr = []
# while i <= 100:
#     arr.append(i)
#     i+=1
# print(arr)


# i = 1
# arr = []
# total = 0
# while i <= 100:
#   arr.append(i)
#   total += i
#   i += 1

# print(sum(arr))

# +++++++++++++++++++++++++++++++++++++++++++++++++

# pwd =""
# while pwd != "pwd":
#     pwd = input("비밀번호를 입력하세요.")

# pwd = ""
# for pwd in range(3):
#     pwd = input("비밀번호를 입력하세요")
#     if pwd == 'pwd':
#         print("맞음")
#         break
#     else:
#         print("틀림")
#         break


# for i in iter(int, 1):
#   if input("비밀번호를 입력하세요.") == "PassWord":
#     break



n = int(input("숫자를 입력하세요: "))
i = 1
even = 0
odd = 0
# 문제 while문를 사용하여 홀수와 짝수를 각각 합을 구하시오.

while i <= n:
    if i%2 == 0:
       even += i
    else:
       odd += i
    i = i + 1

print("짝수 개수:", even)
print("홀수 개수:", odd)















