start=int(input("시작 값을 입력해봐:"))
end=int(input("끝 값을 입력해봐:"))
baesu=int(input("배수를 입력해봐:"))
sum=0

def baesu_sum(start, end, baesu):
    sum=0
    for i in range(start,end+1):
            if i%baesu==0:
                sum=sum+i
            return sum
hap=baesu_sum(start, end, baesu)
print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(start, end, baesu, hap))    
for i in range(start,end+1):
    if i%baesu==0:
        sum=sum+i
print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(start,end,baesu,sum))        

sum=0
i=start
while i<=end:
     if i%baesu==0:
        sum=sum+i
        i=i+1
print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(start,end,baesu,sum))        
    
