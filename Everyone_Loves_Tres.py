'''def find_smallest_divisible_number(n):
    # If the length is 1, it's impossible to satisfy the constraints.
    if n == 1:
        return -1
    if n==2:
        return 66

    # We need the number to end with '6' for divisibility by 2.
    # Start with a number of '6's at the end and try to fill with '3's.
    for sixes in range(1, n + 1):  # At least 1 '6' at the end.
        threes = n - sixes  # The rest are '3's.

        # Create the candidate number.
        candidate = '3' * threes + '6' * sixes

        # Check if it's divisible by 33 (divisible by both 3 and 11).
        if int(candidate)%33!=0:
            return candidate 
        if int(candidate)%66!=0:
            return candidate # Return the first valid number found.

    return -1  # If no valid number is found.

# Read input and process each test case.
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Length of the number
    print(find_smallest_divisible_number(n))'''




'''from itertools import product

def divby66(n):
    if n==1:
            return (-1)
    if n==2:
            return (66)
    # Generate all possible numbers of length n consisting of 3s and 6s
    
    for digits in product('36', repeat=n):
        number = int(''.join(digits))
    
        # Check divisibility by 2 (last digit must be 6)
        if number % 33 != 0:
            continue
        
        # Check divisibility by 3 (sum of digits divisible by 3)
        if number % 66 != 0:
            continue
        
        # If all conditions are satisfied, return the number
        return number
    
    # If no valid number is found, return -1
    return -1

# Example usage
t = int(input())
for i in range(t):
    n=int(input())
    print(divby66(n))
'''

from collections import deque

def divby66(n):
    if n == 1:
        return -1  
    if n == 2:
        return 66  
    
    queue = deque(['3', '6'])
    
    while queue:
        n_str = queue.popleft()
        
        if len(n_str) == n and int(n_str) % 66 == 0:
            return int(n_str)
        
        if len(n_str) < n:
            queue.append(n_str + '3')
            queue.append(n_str + '6')
    
    return -1  
t = int(input())
for i in range(t):
    n = int(input())
    print(divby66(n))


'''def divby66(n):
    # No valid single-digit number can be divisible by 66
    if n == 1:
        return -1

    # For n >= 2, we need a number that is divisible by 66
    # Let's try to generate the smallest valid number

    # To ensure the number is divisible by 2, it must end in '6'
    # Start by assuming a number with (n-1) '3's followed by '6'
    threes = n - 1
    sixes = 1  # One '6' at the end for divisibility by 2

    # Sum of (n-1) '3's = 3 * (n - 1)
    # Adding one '6' makes the total sum = 3 * (n - 1) + 6

    # We need the sum of digits to be divisible by 3
    while (3 * threes + 6) % 3 != 0 or (threes - sixes) % 11 != 0:
        threes -= 1
        sixes += 1

        # If we run out of '3's, it's impossible to create a valid number
        if threes < 0:
            return -1

    # Construct the smallest valid number with the correct number of '3's and '6's
    result = '3' * threes + '6' * sixes
    return int(result)

# Example usage and testing for various cases
t = int(input())
for _ in range(t):
    n = int(input())
    print(divby66(n))'''





'''def divby66(n):
    # If n is odd, return -1 because we can't form a valid number
    if n % 2 != 0:
        return -1
    # Construct the smallest number of length n that meets the requirements
    return "36" * (n // 2)

# Read input
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    results.append(divby66(n))

# Output all results
print("\n".join(str(result) for result in results))'''
