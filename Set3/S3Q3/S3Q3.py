n = int(input())
names = []
for i in range(n):
    names.append(input())
for name in names:
    words = name.split(' ')
    for i in range(len(words)):
        if len(words[i]) > 1:
            words[i] = words[i][0].upper() + words[i][1:].lower()
        elif len(words[i]) == 1:
            words[i] = words[i][0].upper()
    print(' '.join(words))
