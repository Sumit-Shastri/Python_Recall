# Sort Dictionary by values

d = {'apple': 5, 'banana': 2, 'cherry': 7}

sorted = dict(sorted(d.items(), key = lambda item : item[1]))

print(sorted)
