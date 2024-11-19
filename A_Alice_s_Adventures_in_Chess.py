'''t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    s = input()

    x, y = 0, 0
    flag = False

    for i in range(101):
        if x == a and y == b:
            flag = True
            break
        if s[i % n] == 'N':
            y += 1
        elif s[i % n] == 'E':
            x += 1
        elif s[i % n] == 'S':
            y -= 1
        elif s[i % n] == 'W':
            x -= 1

    if flag:
        print("YES")
    else:
        print("NO")
'''

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()

    x, y = 0, 0
    flag = False

    for i in range(2000):
        if x == a and y == b:
            flag = True
            break
        
        if s[i % n] == 'N':
            y += 1
        elif s[i % n] == 'E':
            x += 1
        elif s[i % n] == 'S':
            y -= 1
        elif s[i % n] == 'W':
            x -= 1

    if flag:
        print("YES")
    else:
        print("NO")
