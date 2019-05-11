from src import number_gen, uninformed_solver, informed_solver
from timeit import default_timer as timer
from colorama import init
from printer import *


# Amount of numbers to be used
n = 6

if __name__ == '__main__':
    init()

    usable_numbers = number_gen.generate_numbers(n)
    goal_number = number_gen.generate_goal_number()

    print_heading(' :1234: COUNTDOWN NUMBER GAME')
    print_nr_info(n, usable_numbers, goal_number)
    print_heading(' :memo: RESULTS')

    u_start_time = timer()
    u_search_result = uninformed_solver.solve(usable_numbers, goal_number)
    u_end_time = timer()


    u_search = ('Breadth-first search algorithm (Uninformed):', u_end_time - u_start_time) + u_search_result

    i_start_time = timer()
    i_search_result = informed_solver.solve(usable_numbers, goal_number)
    i_end_time = timer()

    i_search = ('A* search algorithm (Informed):', i_end_time - i_start_time) + i_search_result

    print_results([u_search, i_search])
