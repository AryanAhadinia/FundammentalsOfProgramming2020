a = input()
l = []
for d in a:
    if int(d) % 3 == 0:
        l.append(d)
if len(l) == 0:
    print('None Found!')
else:
    for d in l:
        print(d, end='')
    # we can use ''.join(l) instead
