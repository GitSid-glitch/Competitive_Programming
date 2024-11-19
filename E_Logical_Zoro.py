from collections import defaultdict

def find_pairs(N, K, A, B):
    result = []
    freqA = defaultdict(int)
    
    # Step 1: Count frequency of each element in A
    for x in A:
        freqA[x] += 1

    # Step 2: Iterate over all unique pairs (X, Y)
    for i in range(N):
        for j in range(i + 1, N):
            X, Y = A[i], A[j]
            
            # Only consider (X, Y) where X < Y
            if X < Y:
                # Step 3: Check if equation holds
                if 2 * (X + Y) - 3 * (X & Y) - (X | Y) == K:
                    
                    # Step 4: Find (X+Y)//2 and count its occurrence in range [B[X], B[Y]]
                    target = (X + Y) // 2
                    count_in_B = B[i:B[j] + 1].count(target)
                    
                    # Step 5: Multiply by the frequency of (X, Y) in A
                    count_in_A = freqA[X] * freqA[Y]
                    score = count_in_B * count_in_A
                    
                    result.append((X, Y, score))
    
    # Step 6: Sort results by X (ascending order)
    result.sort()

    # Output
    if result:
        for res in result:
            print(f"{res[0]} {res[1]} {res[2]}")
    else:
        print(-1)

# Input handling
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

find_pairs(N, K, A, B)
