from itertools import permutations, combinations

hands = input("Enter characters : ").split(" ")

f1 = open("result_with_bracket.txt", "w", -1, 'utf-8')
f2 = open("result_without_bracket.txt", "w", -1, 'utf-8')

for i in range(1, 7):
    results = []
    combs = combinations(hands, i)
    for comb in combs:
        perms = [''.join(p) for p in permutations(comb)]
        results.append(list(perms))
    f1.write("\n")
    f1.write(f"----------Words with Length {i}---------- ")
    f2.write("\n")
    f2.write(f"----------Words with Length {i}---------- ")
    
    for word_set in results:
        for word in word_set:
            f2.write("\n")
            f2.write(word)
            
            for letter in word:
                word = word.replace(letter, "【"+letter+"】")
            f1.write("\n")
            f1.write(word)

f1.close()
f2.close()

exit = input("Enter any key to exit: ")