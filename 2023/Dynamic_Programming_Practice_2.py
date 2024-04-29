'''
"Topological sort order" is typically used to solve problems with dependencies.
This refers to arranging tasks in such a way that all dependencies of a given task are resolved before the task itself.
This ordering is crucial in a bottom-up approach, where simpler subproblems are solved first, building up to more complex ones.

COIN PROBLEM
Given a set of coin values, and a target amount of money, what's the minimum number of coins needed to meet that target?

A greedy approach works for many real world coins (pounds/euros) and this is conceptually the simplest method.
But this is not mathematically true for all denominations
'''

target_amount_cents = 38
coins = [1,4,5]

call_count = 0
def brute_force(coins,amount):
    global call_count
    call_count += 1
    answer = float('inf')
    if amount == 0:
        answer = 0
    else:
        for coin in coins:
            sub_amount = amount - coin
            if sub_amount >= 0:
                answer = min(answer,brute_force(coins,sub_amount)+1)
    return answer
print('minimum coins using brute force method:',brute_force(coins,target_amount_cents))
print('brute force call count: ',call_count)

memo = {}
call_count = 0
def minimum_coins_memo(coins,amount):
    global call_count
    call_count += 1
    if amount in memo:
        return memo[amount]
    answer = float('inf')
    if amount == 0:
        answer = 0
    else:
        for coin in coins:
            sub_amount = amount - coin
            if sub_amount >= 0:
                answer = min(answer,minimum_coins_memo(coins,sub_amount)+1)
        memo[amount] = answer
    return answer
print('\nminimum coins using memoisation:',minimum_coins_memo(coins,target_amount_cents))
print('memoised call count:',call_count)