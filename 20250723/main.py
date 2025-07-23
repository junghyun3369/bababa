# a = "문자열"

# print(a[-1:])

# a = [1,2,3,4,5]

# print(a[1:3])
# for v in a:
#     print(v)

a = [
    [1,2,3],
    [4,5,6,7],
]

b = [8,9]
del a[1:]
a.append(b)

# a[-1:] = [b]
# a[1][:] = b

# a[1:] = [b] # << 문제 a[:] 이용하여 b의 리스트로 변경하기!!
print(a)








