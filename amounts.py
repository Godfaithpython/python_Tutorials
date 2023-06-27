amount=int(input('enter the amount '))
if amount >=5000 and amount<10000:
    profit=0.25*amount
    if int(profit)>=2000:
        print('profit is {}'.format(profit))
elif amount>=10000 and amount<=30000:
    profit = 0.33 * amount
    if int(profit)>5000:
        print('profit is {}'.format(profit))
elif amount>30000 and amount<=100000:
    profit = 0.45 * amount
    print('profit is {}'.format(profit))
elif amount>100000 and amount<=100000000:
    profit = 0.85 * amount
    print('profit is {}'.format(profit))
else:
    print('amount is not within range')
