from collections import Counter

def similarity_score():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    # Split input into two lists and convert to integers
    left = []
    right = []
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    # Count occurrences in the right list
    right_counter = Counter(right)

    # Calculate similarity score
    similarity_score = sum(num * right_counter[num] for num in left)

    # Return similarity score
    return similarity_score

# Calculate and print the result
result = similarity_score()
print(f"Le score de similarité est : {result}")