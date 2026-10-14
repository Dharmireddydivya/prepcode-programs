datas=input()
data=datas.split()
salary=int(data[0])
hra=int(data[1])*salary/100
da=int(data[2])*salary/100
pf=int(data[3])*salary/100
allowance=data[4]
if allowance=='a':
    print(salary+hra+da-pf+1500)
elif allowance=='b':
    print(salary+hra+da-pf+1700)
elif allowance=='c':
    print(salary+hra+da-pf+1900)