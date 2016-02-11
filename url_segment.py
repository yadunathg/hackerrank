import re
words = open('words.txt')
word_dict = {}
h = 0
for w in words:
    word_dict.update({w.strip(' \n').lower(): h})
    h += 1
n = input()
drop = ['www.', '.com', '.co', '.tx']
for i in xrange(n):
    segments = []
    s = raw_input().lower()
    if s[0] == '#':
        s = s[1:]
    else:
        try:
            float(s)
            print s
            continue
        except ValueError:
            pass
        if '.' in s:
            s = '.'.join(s.split('.')[:-1])
        for d in drop:
            s = s.replace(d, '')

    ind = len(s)
    while len(s):
        if ind == 0:
            segments.append(s)
            s = ''
        else:
            try:
                float(s[:ind])
                segments.append(s[:ind])
                s = s[ind:]
                ind = len(s)
            except ValueError:
                if word_dict.get(s[:ind], None) != None:
                    segments.append(s[:ind])
                    s = s[ind:]
                    ind = len(s)
                else:
                    ind -= 1
    print ' '.join(segments)
