'''
This is a completely new concept to me which is necessary to solve 2023_Day12_Part2
This first example will be me trying to solve the Fibonacci sequence.
0,1,1,2,3,5,8,13,21,34...
'''

# n is the length of the sequence
n = 7

call_count = 0
def fibonacci(n):
    global call_count
    call_count += 1
    #print('function called',call_count,'times: calculating fibonacci(',n,')')
    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
    return result
print(f'basic function. calculating fibonacci number for n of {n}: {fibonacci(n)}')
print('total number of calls: ', call_count)

call_count_memo = 0
results_table = {}
def fibonacci_memo(n):
    global call_count_memo
    call_count_memo += 1
    #print('function called',call_count,'times: calculating fibonacci_memo(',n,')')
    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        if n in results_table:
            result = results_table[n]
        else:
            result = fibonacci_memo(n-1)+fibonacci_memo(n-2) 
            results_table[n] = result
    return result
print(f'\nmemoised function. calculating  fibonacci number for n of {n}: {fibonacci_memo(n)}')
print('total number of calls: ', call_count_memo)

call_count_bottom = 0
def fib_bottom_up(n):
    global call_count_bottom
    call_count_bottom += 1
    array = []
    for i in range(n+1):
        if i == 0:
            result = 0
        elif i == 1:
            result = 1
        else:
            result = array[i-1] + array[i-2]
        array.append(result)
        #print('iteration',i,'complete. array:',array)
    return result
print(f'\nbottom-up function. calculating fibonacci number for n of {n}: {fib_bottom_up(n)}')
print('total number of calls: ', call_count_bottom)

def bottom_fib_2_variables(n):
    x,y = 0,0
    for i in range(n+1):
        if i == 0:
            result = 0
        if i == 1:
            result = 1
        else:
            result = x + y
        x = y
        y = result
    return result
print(f'\nmore efficient bottom-up function. calculating fibonacci number for n of {n}: {bottom_fib_2_variables(n)}')
print('total number of calls: ', 1)