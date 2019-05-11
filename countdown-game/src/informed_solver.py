from .number_node import NumberNode
import operator, heapq

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def solve(nrs, goal):
    """Solve the game using the breadth-first (uninformed) search algorithm"""

    it_numbers = enumerate(nrs)

    # Simple array to represent queue of the tree
    tree = [NumberNode(result=nr, nr=nr, goal=goal, left_overs=nrs[:i]+nrs[i+1:]) for i, nr in it_numbers]

    heapq.heapify(tree)

    # Placeholders
    closest = 0
    solution = False

    # Loop till solution found or tree is empty (all possible solutions)
    while not solution and len(tree) > 0:

        current_node = heapq.heappop(tree)
        c_nr = current_node.result
        c_lo = current_node.left_overs

        for i, nr in enumerate(c_lo):
            for o_str, fun in operators.items():
                # Leftover check if division doesn't create a decimal number
                # if c_nr % nr == 0 or o_str != '/':
                new_lo = c_lo[:i] + c_lo[i+1:]
                new_node = NumberNode(result=fun(c_nr, nr), goal=goal, left_overs=new_lo, nr=str(nr), prev=current_node, op=o_str)

                if new_node.is_solution():
                    solution = new_node
                else:
                    heapq.heappush(tree, new_node)

                    if new_node < closest:
                        closest = new_node

    return (solution, solution.equation, goal) if solution else (solution, closest.equation, closest)
