while True:
    print("="*30)
    print("1. n까지 정수의 합")
    print("2. n~m까지 k의 배수의 합")
    print("3. 구구단 출력")
    print("4. 종료")
    print("="*30)
    menu=int(input("정수를 입력하세요(1~4):"))
    if menu==1:
        n=int(input("하나의 정수를 입력하세요=>"))
        sum=0
        for i in range(n+1):
            sum=sum+i
        print("1부터 %d까지의 합은 %d" %(n,sum))

    if menu==2:
        start=int(input("시작 값을 입력해봐:"))
        end=int(input("끝 값을 입력해봐:"))
        baesu=int(input("배수를 입력해봐:"))
        sum=0
        for i in range(start,end+1):
            if i%baesu==0:
                sum=sum+i
        print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(start,end,baesu,sum))  
    if menu==3:
        a=int(input("정수를 입력하세요:"))
        i = a
        for j in range(1,10):
            print(i*j, end=' ')

    if menu==4:
        print("프로그램을 종료합니다.....")
        break
       

