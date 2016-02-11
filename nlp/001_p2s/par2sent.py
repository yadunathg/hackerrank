import re
p = raw_input()
for c in '.?!':
    p = (c+'\n').join([s.strip() for s in p.split(c)])
p = re.sub(r'("[^"]*)\n([^"]*")',r'\1\2',p)
p = re.sub('.\n\' ', '.\'\n',p)
print p
