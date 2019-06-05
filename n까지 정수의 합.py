n=int(input("하나의 정수를 입력하세요=>"))

sum=0
for i in range(n+1):
    sum=sum+i
print("1부터 %d까지의 합은 %d" %(n,sum))
