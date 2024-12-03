def is_safe(levels):

    # Check if the levels are increasing or decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    # Check the difference between levels
    levels_diff = all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1))
    
    return (increasing or decreasing) and levels_diff    

def count_safe_reports():
    safe_count = 0
    with open("input2.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe_count += 1
    return safe_count

# Print the result
result = count_safe_reports()
print(f"Le nombre de rapports sûrs est : {result}")