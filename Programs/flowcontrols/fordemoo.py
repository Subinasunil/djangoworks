def is_prime(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    return True if flag==0 else False
print(is_prime(13))


def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)
prime_range(10,37)