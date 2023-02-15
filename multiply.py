def mul(a,b,c):
    return a*b*c

print(mul(3,6,4))


def muleven(*a):
    n=1
    for i in a:
        if i%2==0:
            n =n*i
    return n
print(muleven(1,2,3,4,5,6,7,8))