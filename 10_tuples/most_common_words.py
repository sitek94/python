file = open('../materials/intro.txt')

words_counts = {}

for line in file:
    words = line.rstrip().split()
    for word in words:
        words_counts[word] = words_counts.get(word, 0) + 1

counts_list = []
for key, value in words_counts.items():
    counts_list.append((value, key))

counts_list = sorted(counts_list, reverse=True)

for value, key in counts_list[:10]:
    print(key, value)
