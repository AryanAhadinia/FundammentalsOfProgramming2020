n = int(input())
isPrime = True
for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break
if n == 1:
    isPrime = False
if isPrime:
    print('*' * n)
    for i in range(n - 2):
        print('*' + (' ' * (n - 2)) + '*')
    print('*' * n)
else:
    for i in range(n):
        print('*' * n)
