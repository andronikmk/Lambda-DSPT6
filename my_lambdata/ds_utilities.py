import pandas as pd

def enlarge(n):
    ''' This function multiples the input by 100. '''
    return n*100

if __name__=='__main__':
    y = int(input("Enter a number: "))
    print(y, enlarge(y))