d = {'x': 1, 'y': 2, 'z': 3}
#遍历key
for key in d:
    print(key)

for key in d.iterkeys():
    # d.iterkeys(): an iterator over the keys of d
    print(key)


for key in d.keys():
    # d.keys() -> ['y', 'x', 'z']


    print(key)

#遍历value
for value in d.itervalues():
    # d.itervalues: an iterator over the values of d
    print(value)

for value in d.values():
    # d.values() -> [2, 1, 3]
    print(value)



#遍历keys和values
for key, value in d.iteritems():
    # d.iteritems: an iterator over the (key, value) items
    print(key,'corresponds to',d[key])

for key, value in d.items():
    # d.items(): list of d's (key, value) pairs, as 2-tuples
    # [('y', 2), ('x', 1), ('z', 3)]
    print(key,'corresponds to',value)


