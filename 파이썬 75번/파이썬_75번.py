#연습 75번
m=int(input("m의 값을 입력해주세요: "))
n=int(input("n의 값을 입력해주세요: "))
if m<=n:
    d=n
else:
    d=m
for i in range(2,d+1):
    if m%i==0 and n%i==0:
        max_div=i
print(max_div)
            
            
#Greatest Common divisor 최대공약수? >> ㅇㅇ
#기말과제랑 비슷한 형식으로 가면 된다. >>근데 걔는 c언어
#최대공약수는 나누어지는 걸 봐야되잖아. 그럼 최소값이 먼저아닌가?


#연습 76번
prime=int(input("Enter an integer (2 or qreater): "))
print("The prime factors of {} are: ".format(prime))
#얘는 공약수를 다 구하는거네.
while prime>=2:
    for i in range(2,prime+1):
         if prime%i==0:
            prime=prime//i

            break

#연습 77번
#이진수를 십진수로 바꿔서 출력해주기
#일의 자리 계산 어떻게 하더라?
bin=input("이진수의 값을 입력해주세요: ")
bin_list=[]
for i in bin:
    a=int(i)
    bin_list.append(a)
bin_list.reverse()
total=0
n=0
for i in bin_list:
    if i!=0:
       total+=2**(n)
       n+=1
    else:
       n+=1
print(total)


#연습 78번
#십진수를 이진수로 바꿔서 출력해주기
ten_num=int(input("십진수의 값을 입력해주세요: "))
print("십진수 {}의 이진수 값은 ".format(ten_num),end='')
last=[]
while ten_num>=1:
    last.append(ten_num%2)
    ten_num=ten_num//2
for i in last[::-1]:
    print(i,end='')

