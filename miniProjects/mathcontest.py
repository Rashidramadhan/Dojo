# this is a simple python program that acts a maths contest, the user can solve 
# simple maths problems that has a +, -, and *, the program present ten probems
#  the program counts how long the user will take to solve these probems with a timer
#  it is a simple game challenge for young kids
import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10
def generate_problem():
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left_operand) + ' ' + operator + ' ' + str(right_operand)
    answer = eval(expr)
    return expr, answer
wrong = 0
input('press enter to start ')
print('--------------------------------------')

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input('Problem # ' + str(i + 1)+ ': ' + expr + ' = ')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print('-----------------------------------------------------')
print(f'Nice work! you finished in {round(total_time / 60)} minutes and {round(total_time % 60)} seconds. you got {wrong} incorrect answers')