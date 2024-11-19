# Read input
n = int(input())
s = input().strip()

# Dictionary to count occurrences of each two-gram
two_gram_count = {}

# Loop through the string and count two-grams
for i in range(n- 1):
    two_gram=s[i:i + 2]
    if two_gram in two_gram_count:
        two_gram_count[two_gram] += 1
    else:
        two_gram_count[two_gram] = 1

# Find the two-gram with the maximum count
max_two_gram = max(two_gram_count, key=two_gram_count.get)

# Print the result
print(max_two_gram)
