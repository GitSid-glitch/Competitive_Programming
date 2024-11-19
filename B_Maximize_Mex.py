def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, x = map(int, input().split())  # n: array length, x: increment value
        a = list(map(int, input().split()))  # The array of integers

        # Sort the array to efficiently find the gaps for MEX
        a.sort()

        # Start from MEX = 0 and track how many operations (increments) we've used
        mex = 0
        operations = 0
        
        # Traverse through the sorted array and find the first MEX that we can achieve
        for i in range(n):
            if a[i] > mex:
                # Try to use the available operations to fill the gap
                while operations > 0 and mex < a[i]:
                    mex += 1
                    operations -= 1
                
                # Now, if the array value is greater than mex, no need to increment it further
                if a[i] > mex:
                    break
            mex += 1
        
        # After the loop, try to use remaining operations to further increase MEX
        mex += operations // x
        
        # Output the result for this test case
        print(mex)

# Sample input execution
solve()
