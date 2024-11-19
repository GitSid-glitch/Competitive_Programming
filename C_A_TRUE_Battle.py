t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n = int(input())  # Length of the binary string
    binary_string = input().strip()  # The binary string of booleans

    # Find the first occurrence of '0'
    first_zero_pos = binary_string.find('0')

    if first_zero_pos == -1 or first_zero_pos % 2 == 0:
        # No '0' or first '0' at an odd 1-indexed position -> Alice wins
        results.append("YES")
    else:
        # First '0' at an even 1-indexed position -> Bob wins
        results.append("NO")

print("\n".join(results))
