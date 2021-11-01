d = {
    'maciek': 27,
    'john': 30,
    'mary': 22
}

for (k, v) in d.items():
    print(k, v)

for k, v in d.items():
    print(k, v)

print(d.items())

# sorted method
print(sorted(d.items()))

# Comparing tuples
print(('Jones', 'Sara') > ('Jones', 'Sam'))
