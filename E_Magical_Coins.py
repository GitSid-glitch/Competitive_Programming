'''t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Cost of the item
    if n % 11 <= n // 11:
        print("YES")
    else:
        print("NO")'''


'''t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Cost of the item
    q = n // 11  # Quotient (how many 11s fit)
    r = n % 11   # Remainder (leftover after using 11s)
    
    if r <= q:
        print("YES")
    else:
        print("NO")'''


'''t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Cost of the item
    if n % 11 <= n // 111:
        print("YES")
    else:
        print("NO")


import math
t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Cost of the item
    x=math.floor(math.log10(n)+1)
    if x==1:
        print("NO")
    if x==2 or x==3:
        if n % 11 <= n // 111:
            print("YES")
        else:
            print("NO")
    
   
   
   
   
   
    if n % 11 <= n // 111:
        print("YES")
    else:
        print("NO")'''



'''t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Cost of the item
    found = False  # Flag to track if we found a valid combination

    # Try subtracting multiples of 11 from n
    for k in range(0, n // 11 + 1):
        if (n - k * 11) % 111 == 0:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")'''


'''def can_pay_with_magical_coins(t, costs):
    results = []
    for n in costs:
        # Check if there exists a valid combination of coins
        found = False
        # Try multiples of 111 coins (maximum is n // 111)
        for k in range(min(n // 111, 11) + 1):
            if (n - 111 * k) % 11 == 0:
                found = True
                break
        results.append("YES" if found else "NO")
    return results

# Input reading
t = int(input())
costs = [int(input()) for _ in range(t)]

# Output results for each test case
results = can_pay_with_magical_coins(t, costs)
print("\n".join(results))'''


def can_pay_with_magical_coins(t, costs):
    results = []
    for n in costs:
        # Check if there exists a valid combination of coins
        found = False
        # Try multiples of 111 coins (maximum is n // 111)
        for k in range(min(n // 111, 11) + 1):
            if (n - 111 * k) % 11 == 0:
                found = True
                break
        results.append("YES" if found else "NO")
    return results

# Input reading
t = int(input())
costs = [int(input()) for _ in range(t)]

# Output results for each test case
results = can_pay_with_magical_coins(t, costs)
print("\n".join(results))






