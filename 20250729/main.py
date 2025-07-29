import test
#  CRUD > 입력,읽기,수정,삭제 > 태이블(NOTIC)
# test.c("insert into NOTICE (title) value ('2025')")
while True:
    print("\n--- [게시판 관리 프로그램] ---")
    print("1. 게시글 추가")
    print("2. 게시글 수정")
    print("3. 게시글 삭제")
    print("4. 전체 게시글 보기")
    print("5. 종료")
    choice = input("무엇을 원하나요? ")

    if choice == '1':    
        title = input("제목 입력")
        test.c(f"insert into NOTICE (title) value ('{title}')")
        test.r('select * from NOTICE')
    elif choice == '2':
        #  수정 실행
        print("\n수정사항이 들어왔네요,일 할 시간이군요. 마음껏 둘러보시길.")
        test.r('select * from NOTICE')
        uuu = input("자, 새로 태어나고 싶은 당신을 말하세요.")
        newtitle = input("그것의 숫자를 말해주세요.")
        sql = f"update NOTICE set title = '{uuu}' where no = {newtitle}"
        test.u(sql)
        #  수정 내용 확인
        test.r('select * from NOTICE')
    elif choice == '3':
        # 삭제 실행
        print("\n지우고 싶으신게 있으신가요?")
        test.r('select * from NOTICE') 
        ddd = input("그 숫자를 말해주세요.")
        sql = f"delete from NOTICE where no = {ddd}"
        test.d(sql)
        # 삭제 내용 확인
        test.r('select * from NOTICE')
    elif choice == '4':
        test.r('select * from NOTICE')
    elif choice == '5':
        print("별에게 축복 있기를.")
        break
    else:
        print("다른걸 원하시나요?")