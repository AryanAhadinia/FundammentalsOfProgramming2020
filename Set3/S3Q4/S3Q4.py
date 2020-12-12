n = int(input())
c = 0
for i in range(n):
    name = input()
    chars = []
    for char in name:
        if not char in chars:
            chars.append(char)
    if len(chars) > c:
        c = len(chars)
print(c)
