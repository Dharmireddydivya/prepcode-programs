num=int(input("enter the number:"))
if num%5==0 and num%11==0:
    print("divisible by both 5 and 11:",num)
elif num%5==0:
    print("divisible by 5 only:",num)
elif num%11==0:
    print("divisible by 11 only:",num)
else:
    print("not divisible by5 and 11:",num)
