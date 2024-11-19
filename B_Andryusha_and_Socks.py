def max_socks_on_table(s,p):
    mp=0
    for i in s:
        if i in p:
            p.remove(i)
        else:
            p.add(i)
        mp=max(mp,len(p))
    print(mp)

n=int(input())
s=list(map(int, input().split()))
p=set()
max_socks_on_table(s,p)