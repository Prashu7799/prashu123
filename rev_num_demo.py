num=int(input("enter a number "))
rev=0
n2=num
while num!=0:
    n1=num % 10
    rev=rev*10+n1
    num=num //10

print("Reverse Number :::",rev)

if rev==n2:
    print("the given number is pal")
else:
    print("the given number is not pal")