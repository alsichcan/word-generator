from itertools import permutations, combinations

groups = []
n = int(input("Enter Number of groups : "))

for i in range(n):
    group = input("Enter words of group %d : " %(i+1)).split(" ")
    groups.append(group)

curr_index = [0 for i in range(len(groups))]

results = []
finished = False

# Iterate through whole combinations of words from each group
while not finished:
    # Pick one word from each group
    hands = []
    for idx in range(n):
        hands.append(groups[idx][curr_index[idx]])

    # Generate words from hand (2 <= length <= 6)
    for size in range(2, n+1):
        if size > 7:
            break
        combs = combinations(hands, size)
        for comb in combs:
            perms = [''.join(p) for p in permutations(comb)]
            results.append(list(perms))

    # Update index
    idx = -1;
    carry = True;
    while(carry):
        if(idx == -1 * n):
            finished = True
            break

        if(curr_index[idx] != 3):
            curr_index[idx] += 1
            carry = False
        else:
            curr_index[idx] = 0
            carry = True
            idx -= 1

# Output result to text file (Sort by length not provided)
out = open("result.txt", "w", -1, 'utf-8')
for word_set in results:
    for word in word_set:
        out.write(word)
        out.write("\n")
out.close()

exit = input("Enter any key to exit: ")
