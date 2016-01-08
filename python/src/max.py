import re, collections

abc = ['ab', 'cd', 'ef']

model = collections.defaultdict(lambda: 1)
c = 1
for f in abc:
    c += 1
    model[f] += c

print model

print max(set(a for a in abc), key=model.get)