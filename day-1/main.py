
# Setting Variables
elves = list()
calc = 0

# Open input document, and then add the max values of each elf together
with open('input.txt') as f:
    for line in f:
        e = line.strip()
        if e:
            calc += int(e)
        else:
            elves.append(calc)
            calc = 0

# Sort the list from high to Low
elves.sort(reverse=True)

# Print entire list
print(elves)

# Print the maximum value, the solution for Part 1
print("Answer 1:", elves[0])

# Resetting values for Part 2
calc = 0
range_ = 3

# Add the top 3 Elves values (calories) together
for x in range(range_):
    calc += elves[x]

# Print the top 3 Elves values, the solution for Part 2
print("Answer 2:", calc)
