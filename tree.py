def count_minimum_operations(arr):
    n = len(arr)
    min_shifts = float('inf')  
    for shift in range(n):
        is_sorted = True

        for i in range(n):
            if arr[(i + shift) % n] != i + 1:
                is_sorted = False
                break

        if is_sorted:
            min_shifts = min(min_shifts, shift)

    if min_shifts != float('inf'):
        return min_shifts  
    else:
        return min_shifts + 1  

if __name__ == "__main__":
    t=int(input())
    arr=[]
    for i in range(t):
        n,d,l=map(int,input().split())
        arr.append(n)
        arr.append(d)
        arr.append(l)

        print(count_minimum_operations(arr))  
