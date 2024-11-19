'''n=int(input())
for _ in range(n):
    s=input().strip()
    if len(s)>10:
        x=s[1:-1]
        l=len(x)

        print(s[0]+str(l)+s[-1])
    else:
        print(s)'''

n = int(input())
for _ in range(n):
    s=input().strip()
    if len(s)>10:
        print(f"{s[0]}{len(s)-2}{s[-1]}")
    else:
        print(s)
