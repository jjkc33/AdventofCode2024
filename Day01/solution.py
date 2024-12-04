from collections import Counter


with open('input.txt') as f:
    data = [list(map(int, r.split())) for r in f]


# part 1
d1, d2 = zip(*data)
part1 = sum(abs(x - y) for x, y in zip(sorted(d1), sorted(d2)))
print(part1)

# alternative one-line
# part1 = sum(abs(x - y) for x, y in zip(*map(sorted, zip(*data))))

# part 2
counts = Counter(d2)
part2 = sum(x * counts[x] for x in d1)
print(part2)