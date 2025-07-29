# print(__name__)

# if __name__=="__main__":
#     print("출력")

# def a():
#     print("a")

# def b():
#     print("b") 

# def c():
#     print("c")

# def read(file):
#     try:
#         f = open(file, mode='r', encoding='utf-8')
#         txt = f.readlines()
#         print(txt)
#         f.close()
#     except FileNotFoundError as e:
#         print(e)

def read(file):
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            print(f.readlines())
    except FileNotFoundError as e:
        print(e)



