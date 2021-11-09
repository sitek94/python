import urllib.request

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
words = dict()

for line in file:
    for word in line.decode().rstrip().split():
        words[word] = words.get(word, 0) + 1

print(words)
