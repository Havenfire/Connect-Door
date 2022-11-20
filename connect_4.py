from math import comb
 
profiles = 7**7
max_moves = 7*6

move_profiles = {}
move_permutations = {}
 
for i in range(max_moves + 1):
    move_profiles[i] = 0
    move_permutations[i] = comb(i, (i + 1) // 2)
 
print(move_permutations)

def b7sum(n):
    s = 0
    while n:
        s += n % 7
        n //= 7
    return s

for n in range(profiles):
    s = b7sum(n)
    move_profiles[s] += 1

print(move_profiles)

total = 0

for i in move_profiles:
    total += move_profiles[i] * move_permutations[i]

print(f'{move_permutations[42]:,}')
print(f'{total:,}')
