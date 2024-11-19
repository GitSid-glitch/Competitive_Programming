n=int(input())
a=list(map(int, input().split()))
sos=sorted(set(a))
if len(sos)>1:
    print(sos[1])
else:
    print("NO")