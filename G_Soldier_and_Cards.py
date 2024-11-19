def play_card_war(n, k1, stack1, k2, stack2):
    # Initialize player stacks
    s1 = stack1[:]
    s2 = stack2[:]
    
    fight_count = 0
    max_rounds = 1000  # Arbitrary large number to detect potential infinite games
    
    # Simulate the game
    while s1 and s2 and fight_count < max_rounds:
        fight_count += 1
        
        # Each player plays their top card
        card1 = s1.pop(0)
        card2 = s2.pop(0)
        
        # Determine the winner of this round
        if card1 > card2:
            # Soldier 1 wins the round
            s1.append(card2)
            s1.append(card1)
        else:
            # Soldier 2 wins the round
            s2.append(card1)
            s2.append(card2)
    
    # Check the outcome after the loop
    if fight_count == max_rounds:
        return -1  # Assume infinite game if max rounds reached
    elif s1:
        return fight_count, 1  # Soldier 1 wins
    else:
        return fight_count, 2  # Soldier 2 wins

# Taking input in the specified format
n = int(input())
k1, *stack1 = map(int, input().split())
k2, *stack2 = map(int, input().split())

# Calculate the result and print the output
result = play_card_war(n, k1, stack1, k2, stack2)
if result == -1:
    print(result)
else:
    print(result[0], result[1])
