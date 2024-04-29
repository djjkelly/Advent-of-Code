'''
This is a completely new concept to me which is necessary to solve 2023_Day12_Part2
This first example will be me trying to solve the Fibonacci sequence.
0,1,1,2,3,5,8,13,21,34...
'''

# n is the length of the sequence
n = 7
result = 0
results_table = {}

def fibonacci(n):
    print('function called ',' times: calculating fibonacci(',n,')')
    if n == 0:
        result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2) 
    return result
print(f'commencing fibonacci sequence: {fibonacci(n)}')

def fibonacci_memo(n):
    print('function called ',' times: calculating fibonacci_memo(',n,')')
    if n == 0:
        result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        if n in results_table:
            result = results_table[n]
        else:
            result = fibonacci_memo(n-1)+fibonacci_memo(n-2) 
            results_table[n] = result
        print('results table:' ,results_table)
    return result
print(f'commencing memoised fibonacci function: {fibonacci_memo(n)}')