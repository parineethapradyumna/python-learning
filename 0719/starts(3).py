n = 3
i = 0
while i < n:
    j = i
    while j < n:
        print(' ', end='')
        j += 1
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    print()
    i += 1