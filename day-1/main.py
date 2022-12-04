
elves = list()
calc = 0

with open('input.txt') as f:
    for line in f:
        e = line.strip()
        if e:
            calc += int(e)
        else:
            elves.append(calc)
            calc = 0

elves.sort(reverse=True)

print(elves)

print("Answer 1:", elves[0])

calc = 0
range_ = 3

for x in range(range_):
    calc += elves[x]

print("Answer 2:", calc)
