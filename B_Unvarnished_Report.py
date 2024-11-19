def find_first_difference(S, T):
    # Find the length of both strings
    len_s, len_t = len(S), len(T)
    
    # Loop through the characters of both strings up to the shorter one
    for i in range(min(len_s, len_t)):
        if S[i] != T[i]:
            # Return the 1-based index of the first different character
            print(i + 1)
            return
    
    # If no difference is found in the common part, the longer string has an extra character
    if len_s != len_t:
        print(min(len_s, len_t) + 1)
    else:
        # If the strings are equal, print 0
        print(0)

# Input
S = input().strip()
T = input().strip()

# Call the function
find_first_difference(S, T)
