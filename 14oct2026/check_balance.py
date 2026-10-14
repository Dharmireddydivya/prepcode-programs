def check(balance,amount=5000):
    if amount%500==0 and amount<=balance:
        return "allow"
    else:
       return "not allow"
result=check(2000,500)
print(result)