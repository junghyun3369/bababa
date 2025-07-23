# a = [
#   [1,2,3,4,5],
#   [6,7,8,9,10],
#   [11,12,13,14,15],
#   [16,17,18,19,20],
#   [21,22,23,24,25],
# ]

# for y in a:
# #  print(y)
#     for x in y:
#     # print(x)

# if True:
#     pass
# else:
#     pass

a = []
b = []
for y in range(1,26):
    b.append(y)
    if y%5 == 0: # 5 10 15 20 25
        a.append(b)
        b = []
for y in a:
    print(y)




































