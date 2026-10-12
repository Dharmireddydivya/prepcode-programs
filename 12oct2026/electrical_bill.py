def bill(units,rates):
    unit=units*2
    rate=rates*2
    bill_beforetax=unit*rate
    tax=(bill_beforetax*10)/100
    total_bill=tax+bill_beforetax
    return total_bill
print(bill(5,10))