s1=input()
s2=input()
s1lower=s1.lower()
s2lower=s2.lower()
if s1lower==s2lower:
    print(0)
else:
    if s1lower<s2lower:
        print(-1)
    else:
        print(1)