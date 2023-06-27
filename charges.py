amount = int(input('enter the amount: '))
agent = int(input("""Are you an agent:
                 1:yes\n
                 2:no\n
             """))
if agent==1:
    network = int(input("""Transfer:
                1:Within the same network\n
                2:To another network\n
                 """))
    if network==1:
        charges=0.10*amount
        print(f'transfer fee is {charges}')
    elif network==2:
        charges = 0.18 * amount
        print(f'transfer fee is {charges}')
    else:
        print('invalid choice!!')
elif agent==2:
    network = int(input("""Transfer:
                   1:Within the same network\n
                   2:To another network\n
                    """))
    if network == 1:
        charges = 0.23 * amount
        print(f'transfer fee is {charges}')
    elif network == 2:
        charges = 0.30 * amount
        print(f'transfer fee is {charges}')
    else:
        print('invalid choice!!')
else:
    print('invalid choice')




