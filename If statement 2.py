price=100000
has_good_credit=False
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price

print(f'Down payment: ${down_payment}')
