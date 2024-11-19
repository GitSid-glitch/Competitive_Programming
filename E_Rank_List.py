'''a,b=map(int,input().split())
c=0
for i in range(a):
    p,t=map(int,input().split())
    if p==p and t==t:
        c+=1
        '''
'''n,k=map(int,input().split())
teams=[]

for i in range(n):
    p,t = map(int, input().split())
    teams.append((p, t))

for i in range(n):
    for j in range(n-1-i):
        if (teams[j][0] < teams[j + 1][0]) or (teams[j][0] == teams[j + 1][0] and teams[j][1] > teams[j + 1][1]):
            teams[j],teams[j+1]=teams[j+1],teams[j]

k=teams[k-1]
kp,kt=k

c=0
for team in teams:
    if team[0]==kp and team[1]==kt:
        c+=1

print(c)'''
n,k=map(int, input().split())
teams=[]

for i in range(n):
    p,t=map(int,input().split())
    teams.append((p,-t))

teams.sort(reverse=True)  
k=teams[k - 1]

c=teams.count(k)

print(c)



