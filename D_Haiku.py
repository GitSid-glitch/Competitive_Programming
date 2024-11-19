s1=input()
s2=input()
s3=input()
s1strip=s1.strip()
s2strip=s2.strip()
s3strip=s3.strip()
vowels="aeiou"
c=0
c1=0
c2=0

for i in s1strip:
    if i in vowels:
        c+=1

for i in s2strip:
    if i in vowels:
        c1+=1

for i in s3strip:
    if i in vowels:
        c2+=1
'''while vowels in s1strip:
    c+=1

while vowels in s2strip:
    c1+=1

while vowels in s3strip:
    c2+=1'''

if (c==5 and c1==7 and c2==5):
    print("YES")
else:
    print("NO")