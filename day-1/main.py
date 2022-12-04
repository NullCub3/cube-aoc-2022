
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

print(elves[0])
