#title:math quiz
#author: michael stoll
#date: 2/21/25
import random
integer1 = random.randint(1, 1000)
integer2 = random.randint(1, 1000)
def random_math_problem(int1, int2):
    print('Add these numbers')
    print(' ', int1)
    print('+', int2)
    print('-----')
math_solution = integer1 + integer2
random_math_problem(integer1, integer2)
user_solution = int(input('Enter answer here:'))
if user_solution == math_solution:
    print('Correct! Good job!')
else:
    print('Wrong. Try another?')