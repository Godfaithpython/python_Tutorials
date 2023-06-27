num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
summer=0
if(num1%2 == 0) and (num2%2 == 0):
    summer = num1+num2
    # print(summer)
    print(f'the sum of {num1=} and {num2=} is: {summer=}')
    # print('the sum of {} and {} is: {}'.format(num1,num2,summer))
if num1>num2:
    print('{} is greater'.format(num1))
elif num1==num2:
    print('the two numbers are equal')
else:
    print('{} is greater'.format(num2))
