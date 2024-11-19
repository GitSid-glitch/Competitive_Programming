def minimize_lunch_breaks(N, K):
    total_departments = len(K)
    min_max_people = float('inf')  # Start with infinity as the initial minimum
    
    # We will go through all possible divisions of the departments (2^N possibilities)
    for mask in range(1 << total_departments):  # Loop from 0 to 2^N - 1
        group_a_sum = 0
        group_b_sum = 0
        
        for i in range(total_departments):
            if mask & (1 << i):  # Check if the i-th department is in Group B
                group_b_sum += K[i]
            else:  # Otherwise, it's in Group A
                group_a_sum += K[i]
        
        # Find the maximum of the two groups for this particular division
        max_people = max(group_a_sum, group_b_sum)
        
        # We want to minimize this maximum
        min_max_people = min(min_max_people, max_people)
    
    print(min_max_people)

# Input
N = int(input())  # Number of departments
K = list(map(int, input().split()))  # Number of people in each department

# Call the function
minimize_lunch_breaks(N, K)
