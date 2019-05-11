from src import number_gen, us_solver
from timeit import default_timer as timer

if __name__ == '__main__':
    usable_numbers = number_gen.generate_numbers()
    goal_number = number_gen.generate_goal_number()

    print('----------------------------------------------------------------------------------------')
    print('Numbers to be used:', ', '.join(str(n) for n in usable_numbers))
    print('Goal:', goal_number)
    print('----------------------------------------------------------------------------------------')

    start_time = timer()
    solved, equation, result = us_solver.solve(usable_numbers, goal_number)
    end_time = timer()

    print('In:', str(round(end_time - start_time, 5)), 'seconds')

    if solved:
        print('Found the solution with the following equation:')
    else:
        print('Didn\'t find a solution, but the closest answer is:', '\t')


    print('')
    print(equation, '=', result)
    print('----------------------------------------------------------------------------------------')
