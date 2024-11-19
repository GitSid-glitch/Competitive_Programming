def min_button_presses(t, test_cases):
    results = []
    
    for i in range(t):
        n, k = test_cases[i][0]  # n: number of buttons, k: target number of cans
        a = test_cases[i][1]  # list of cans that each button can release
        
        # Sort the buttons by the number of cans they can release, in descending order
        a.sort(reverse=True)
        
        total_cans = 0
        presses = 0
        
        # First round: press each button once
        for cans in a:
            total_cans += 1  # Collect at least 1 can from this button
            presses += 1     # This counts as 1 button press
            if total_cans >= k:  # Stop if we've collected enough cans
                results.append(presses)
                break
        else:
            # If we still need more cans after the first round
            needed = k - total_cans  # How many more cans we need
            
            # Now, we press buttons again to collect more cans
            for cans in a:
                if needed <= 0:
                    break
                if cans > 1:  # We've already pressed this button once
                    # We can collect (cans - 1) more cans from this button
                    available_cans = cans - 1
                    # Take the minimum of the available cans or the remaining needed cans
                    additional_cans = min(available_cans, needed)
                    presses += additional_cans  # Each can requires an additional press
                    needed -= additional_cans  # Decrease the number of needed cans
            
            results.append(presses)
    
    # Print all results at once
    print('\n'.join(map(str, results)))

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append(((n, k), a))

# Solve the problem
min_button_presses(t, test_cases)
