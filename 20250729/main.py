import test
#  CRUD > 입력,읽기,수정,삭제 > 태이블(NOTIC)
# test.c("insert into NOTICE (title) value ('2025')")
returned_from_back = False
while True:
    if returned_from_back:
        print("\n>> 돌아오셨군요. 다른 무언가를 찾으시고 계신가요? <<")
        returned_from_back = False

    print("\n--- [게시판 관리 프로그램] ---")
    print("1. 게시글 추가")
    print("2. 게시글 수정")
    print("3. 게시글 삭제")
    print("4. 전체 게시글 보기")
    print("5. 종료")
    choice = input("무엇을 원하나요? ")

    if choice == '1':    
        title = input("새로운 것을 가져오셨네요. 여기에..")
        if title == '뒤로':
            returned_from_back = True
            continue
        test.c(f"insert into NOTICE (title) value ('{title}')")
        test.r('select * from NOTICE')
    elif choice == '2':
        #  수정 실행
        print("\n수정사항인가요,일 할 시간이군요. 마음껏 둘러보시길.")
        test.r('select * from NOTICE')
        uuu = input("자, 새로 태어나고 싶은 당신을 말하세요.")
        if uuu == '뒤로':
            returned_from_back = True
            continue
        newtitle = input("그것의 숫자를 말해주세요.")
        if newtitle == '뒤로':
            returned_from_back = True
            continue
        sql = f"update NOTICE set title = '{uuu}' where no = {newtitle}"
        test.u(sql)
        #  수정 내용 확인
        test.r('select * from NOTICE')
    elif choice == '3':
        # 삭제 실행
        print("\n지우고 싶으신게 있으신가요?")
        test.r('select * from NOTICE') 
        ddd = input("그 숫자를 말해주세요.")
        if ddd == '뒤로':
            returned_from_back = True
            continue
        sql = f"delete from NOTICE where no = {ddd}"
        test.d(sql)
        # 삭제 내용 확인
        test.r('select * from NOTICE')
    elif choice == '4':
        print("\n 자, 천천히 둘러보세요.")
        test.r('select * from NOTICE')
    elif choice == '5':
        print("별들에게 축복 있기를.")
        break

        #ㅇㅅㅌㅇㄱ
    elif choice == '6':
        print("여기는 아무것도 없답니다.")
    elif choice == 'you':
        print("어머, 이건....예상치 못한 답변이네요. 후후.")
    elif choice == 'who?':
        print("저는 그저 별을 섬기는 신자일 뿐이랍니다.")
    elif choice == 'bye':
        print("당신의 별들에도 축복이 있기를.")
        break
    elif choice == 'no.':
        print("언젠가 다시 만날 날을 기다리겠습니다.")
        break
    elif choice == 'what':
        print(" 이건 그냥, 평범한.......'수정구슬'일 뿐이랍니다.")
    else:
        print("다른걸 원하시나요?")