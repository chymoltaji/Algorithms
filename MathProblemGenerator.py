import random as rand

OPERATIONS = ['+', '-', '*', '/']
def problems_printer(arr):
    for i in arr:
        print(i)

def problem_generator(n):
    """Generates math problems with increasing difficulty"""
    problems = []
    for i in range(1,n):
        problem = str(rand.randint(1,i))+rand.choice(OPERATIONS)+str(rand.randint(1,i))
        print(problem)
    return problems

problems_printer(problem_generator(20))