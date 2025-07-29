# def a(c):
#     if c:
#         print("76", c)
#         del c[0]
#         a(c)

# a([1,2,3,4,5,6,7,8,9,10])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class A():
#     def a():
#      pass
    # def b():
    #  pass

# def a():
#  pass

# class T():
#     # def a():
#     def a(s):
#         pass

# t = T()
# t.a()

# # print(type(a), type(A))


# v1 = 50 # 변수 << 전역

# def a(v):
#   v2 = 100 # 변수 << 지역
#   print(v1, v2)
#   return v2

# class T():
#   def a(s,v):
#     print(v1, v)
#     pass

# t = T()

# vvvv = a(1)
# t.a(vvvv)                                                                                                                                                                                                                                 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class T():
#   def __init__(s, no): # 생성자
#     s.no = no
#   def a(s):            # 함수
#    print(s.no)

# t = T(1) # 클래스를 생성하는 인스턴스 만들기
# t.a()    # 클래스 안에 있는 함수 호출

# class T():
#   def __init__(s, no): # 생성자
#     s.__no = no  # _T__no
#     # s._no = no   # _no
#     # s.no = no    # no
#   @property   # setter 함수
#   def no(s):  # 클래스.변수명
#     return s.__no
  
#   def a(s):            # 함수
#     pass

# t = T(1) # 클래스를 생성하는 인스턴스 만들기 
# # t.a()    # 클래스 안에 있는 함수 호출
# # t.no = 50
# print(t.no)

class T():
  def __init__(s,no): #생성자
    s.__no = no       #클래스에서 사용되는 변수 '__no'
  @property           # 인스턴스로 변수를 호출 하기 위한 설정
  def no(s):
      return s.__no
  def setNo(s,no):   #인스턴스로 변수의 값을 변경할때 사용하는 함수 :setter
     s.__no =no  
#   def a(s):
#       pass
    
t =T()
print("전",t.no)  
#t.no =200 #사용불가
t.setNo(10) #setter를 이용하여 변수 값 변경하는 부분
print("후",t.no)
























