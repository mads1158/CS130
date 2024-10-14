A = int(input('Please enter the first number:\n'))
X = int(input('Please enter the second number:\n'))
Y = int(input('Please enter the thrid number:\n'))

concat = ''

if(A % X == 0):
    concat += 'Fizz'
if(A % Y == 0):
    concat += 'Buzz'

if(concat != ''):
    print(concat)
else:
    print('Neither')
