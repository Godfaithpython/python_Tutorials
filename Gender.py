age = int(input('enter your age '))
gender =int(input("""Which is your gender:
                  1:male\n
                  2:female\n
                  """))
loan = int(input('enter the loan '))
if gender==1:
    if age>=25:
        if loan<100000:
           print('cannot loan amount less than 100000')
        else:
            interest = 0.14 * loan
            print('the interest is {:.3f}'.format(interest))
    else:
        interest = 0.28 * loan
        print('the interest is {:.3f}'.format(interest))
elif gender==2:
    if age>=30:
        if loan<75000:
           print('cannot loan amount less than 75000')
        else:
            interest = 0.09 * loan
            print('the interest is {:.3f}'.format(interest))
    else:
        interest = 0.18 * loan
        print('the interest is {:.3f}'.format(interest))
else:
    print('invalid choice!!')