mines = input().split(' ')
for j in range(10):
    for i in range(10):
        if ('(' + str(i) + ',' + str(j) + ')') in mines:
            print('O', end=' ')
        else:
            print('X', end=' ')
    print()
