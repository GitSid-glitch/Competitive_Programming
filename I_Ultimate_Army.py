def sup(n, s):
    supervisors=[0]*(n + 1)
    
    x = []
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            id = 0
            while i < len(s) and s[i].isdigit():
                id = id * 10 + int(s[i])
                i += 1
            
            if x:
                supervisors[id] = x[-1]
            
            x.append(id)
        elif s[i] == ')':
            x.pop()
            i += 1
        else:
            i += 1
    
 
    return supervisors[1:]

n = int(input()) 
s = input().strip()  

supervisor_list = sup(n, s)

print(" ".join(map(str, supervisor_list)))
