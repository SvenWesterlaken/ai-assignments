from emoji import emojize as e
from colorama import init, Fore

def print_divider():
    print('========================================================================================')

def print_heading(text):
    print_divider()
    print('')
    print(cs(Fore.CYAN, e(text, use_aliases=True)))
    print('')
    print_divider()

def print_nr_info(n, nrs, g_nr):
    print('')
    print(' Amount of generated numbers:', '\t', cs(Fore.YELLOW , n))
    print('')
    print(' Numbers to be used:', '\t\t', cs(Fore.YELLOW, ', '.join(str(n) for n in nrs)))
    print(' Goal:', '\t\t\t\t', cs(Fore.YELLOW, g_nr))
    print('')

def print_results(items, ndigits=5):

    ff = items[0][1] < items[1][1]

    for i, (title, time, solved, equation, result) in enumerate(items):

        is_winning = i == 0 and ff or i == 1 and not ff

        print('')
        print(' ' + cws(title, is_winning))
        print('')
        print( e(' :hourglass:', use_aliases=True), '\t', cs(Fore.YELLOW, round(time, ndigits)), 'seconds')
        print(e(' :heavy_check_mark:') if solved else e(' :heavy_multiplication_x:'), '\t', equation, '=', result)
        print('')

    print_divider()

def cs(color, string):
    return color + str(string) + Fore.RESET

def cws(string, condition):
    return cs(Fore.GREEN, e(':trophy:\t ') + string) if condition else cs(Fore.RED, e(':x:\t ', use_aliases=True) + string)
