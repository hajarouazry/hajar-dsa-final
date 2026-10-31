# ===== Question 3: Recursion =====

import random

# ===== Part (a): The recursive function =====

def follow_instructions(instructions: list[str]) -> list[int]:
    
    def visit(i):
        # base case: if the index is past the end of the list, stop annd return an empty list
        if i >= len(instructions):
            return []
        colour = instructions[i]
        if colour == "green":
            next_i = i + 1
        elif colour == "red":
            next_i = 2 * i + 1
        else:
            next_i = len(instructions)
            for j in range(i + 1, len(instructions)):
                if instructions[j] == "blue":
                    next_i = j + 1
                    break 
        return [i] + visit(next_i)
    
    return visit(0)

print(follow_instructions(["blue", "green", "red", "blue", "green", "red"]))
print(follow_instructions([]))

# brief example and extra checks (empty list, no next blue)
print(follow_instructions(["green", "red", "green", "red"]))
print(follow_instructions(["green", "blue", "green"]))

# ===== Part (a.i): Testing with 2 generated lists =====

# Generate 2 random lists of 10 colours and print each list with the indexes the function visits
random.seed(1)
colours = ["blue", "red", "green"]
for test in range (2):
    test_list = []
    for k in range(10):
        test_list.append(random.choice(colours))
    print("Test", test + 1, ":", test_list)
    print("Visited indexes:", follow_instructions(test_list))
    

