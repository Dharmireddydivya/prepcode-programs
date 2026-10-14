def chck(balance,amount=5000):
    if amount%500==0 and amount<=balance:
        return "allow"
    else:
        