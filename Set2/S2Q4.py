begin = int(input())
end = int(input())
c = 0
for i in range(begin, end + 1):
    if i % 13 == 0 and i % 4 != 0 and i % 7 == 3:
        print(i, end=' ')
        c += 1
print()
print(c)
