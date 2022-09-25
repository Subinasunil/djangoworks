num=45
sum=0
while(num !=0):
    last_digit=num %10
    cube=last_digit**3
    sum=sum+cube
    num=num//10
print(sum) 