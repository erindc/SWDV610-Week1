#Erin Cox

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

def main():
    print('This program checks if the first integer entered is a multiple of the second integer entered')
    print()
    int1 = int(input('Enter an integer: '))
    int2 = int(input('Enter another integer: '))
    isMultiple = is_multiple(int1, int2)
    print(isMultiple)
    
main()