from argparse import ArgumentParser


# Example 1
# parser = ArgumentParser(description='My CLI parser')
# parser.add_argument('--n_one')
# parser.add_argument('--n_two')
# args = parser.parse_args()
# print(args)
# arguments = {key: float(value) for key, value in args.__dict__.items()}
# print(f"{arguments['n_one']} + {arguments['n_two']} = {arguments['n_one'] + arguments['n_two']}")

# Example 2
# parser = ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', type=float, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# Example 3
class Chrome:
    def __init__(self):
        print('I am Chrome')


class Edge:
    def __init__(self):
        print('I am Edge')


parser = ArgumentParser(description='Driver parser')
parser.add_argument('--browser')
arguments = parser.parse_args()

if arguments.browser.lower() == 'chrome':
    Chrome()
elif arguments.browser.lower() == 'edge':
    Edge()
