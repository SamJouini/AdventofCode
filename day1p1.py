def distance_calculation():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    # Split input into two lists and convert to integers
    left = []
    right = []
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    # Sorting the lists
    left.sort()
    right.sort()

    # Calculation of the distance
    total_distance = sum(abs(a - b) for a, b in zip(left, right))

    # Return total distance
    return total_distance

# Result
result = distance_calculation()
print(f"La distance totale est : {result}")
