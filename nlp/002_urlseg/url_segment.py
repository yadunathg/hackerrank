word_dict = {}


def hash(wordfile):
    global word_dict
    words = open(wordfile)
    h = 1
    for w in words:
        word_dict.update({w.strip(' \n').lower(): h})
        h += 1
    return word_dict


def clean(s):
    if s[0] == '#':
        return s[1:]
    else:
        s = s.replace('www.', '')
        s = s.split('.')
        while len(s) > 1:
            if s[-1].isalpha():
                s = s[:-1]
            else:
                break
        return '.'.join(s)


def getWord(s):
    ind = len(s)
    flag = 0
    while ind:
        try:
            float(s[:ind])
            flag = 1
        except ValueError:
            if word_dict.get(s[:ind], 0):
                flag = 2
        if flag:
            if ind == len(s):
                return [s]
            seg = getWord(s[ind:])
            if len(seg):
                return [s[:ind]] + seg
        flag = 0
        ind -= 1
    return []


def main():
    hash('words.txt')
    n = input()
    for i in xrange(n):
        s = raw_input().lower()
        s = clean(s)
        seg = getWord(s)
        if len(seg):
            print ' '.join(seg)
        else:
            print s

if __name__ == "__main__":
    main()
