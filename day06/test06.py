d1 = {1: 'a', 2: 'b'}
d2 = d1.copy()
d3 = d1
print(id(d1))
print(id(d2))
print(id(d3))
print(d1)
d2[1] = 'aaa'
print(d1)