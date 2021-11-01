c = {
    'a': 10,
    'b': 50,
    'c': 33
}

print(sorted([(v, k) for k, v in c.items()]))
