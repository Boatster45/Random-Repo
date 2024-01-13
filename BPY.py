import argparse
import math

def cube_operations(number, operation):
    if operation == 'cuberoot':
        result = math.pow(number, 1/3)
        print(f'The cube root of {number} is: {result}')
    elif operation == 'cube':
        result = number ** 3
        print(f'The cube of {number} is: {result}')
    else:
        print('Invalid operation. Use "cuberoot" or "cube."')

def main():
    parser = argparse.ArgumentParser(description='Calculate cube root or cube of a number.')
    parser.add_argument('number', type=float, help='The number for cube root or cube calculation.')
    
    parser.add_argument('-c', '--cube', action='store_true',
                        help='Cubes the specified number.')
    parser.add_argument('-r', '--cuberoot', action='store_true',
                        help='Cuberoots the specified number.')

    args = parser.parse_args()

    cube_operations(args.number, 'cube' if args.cube else 'cuberoot')

if __name__ == '__main__':
    main()
