n = 9

for i in range(1, n + 1):
    left = ''.join(map(str, range(1, i)))
    spaces = ' ' * (n - i)
    print(f'{spaces}{left}{i}{left[::-1]}')