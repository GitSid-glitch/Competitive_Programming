def find_removal_operations(s):
    n = len(s)
    operations = []
    
    # We'll continue operating on the string while it contains 'abc'
    while True:
        found_abc = False
        
        # Search for "abc" in the string
        for i in range(len(s) - 2):
            if s[i:i+3] == "abc":
                # Apply operation 4: remove "abc"
                operations.append((4, i + 1))
                s = s[:i] + s[i+3:]  # Remove "abc"
                found_abc = True
                break
        
        if not found_abc:
            break
        
    # After removing all "abc", if there are any characters left, return -1
    if s:
        return -1
    
    # Return the operations
    return operations

# Input
s = input().strip()

# Get the operations
result = find_removal_operations(s)

# Output the result
if result == -1:
    print(-1)
else:
    print(len(result))
    for op in result:
        print(op[0], op[1])
