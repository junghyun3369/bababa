a=[]
a.append(1) #값추가
print(a)
a[0] = 2 #값변경
# print(a)
for v in a:
    print(v)

a=[
   [1],
   [1,2],
   [1,2,3]
   ]
for y in a:
    print(y) # [1] > [1,2] > [1,2,3]
    for x in y:
        print(x)


a = ((),[]) #값을 넣은 상태로 만들면 변경불가 + 삭제불가 + 추가불가 (사항에따라서)
print(a)
a [0].append(1)
print(a)

a =() # 튜플 < 한번 넣은 값은 변경불가






