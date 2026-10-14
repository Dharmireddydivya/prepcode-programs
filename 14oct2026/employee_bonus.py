performance_rating=int(input("enter the rating:"))
employee_years=int(input("enter the years:"))
if performance_rating>=4 and employee_years>=2:
    print("employee is eligible for bonus")
else:
    print("employee is not eligible for bonus")