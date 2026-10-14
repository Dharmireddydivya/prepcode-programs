password=input("enter the password")
if len(password)>=8 and (("@") or ("$") or ("~"))in password:
    print("valid")
else:
    print("not valid")