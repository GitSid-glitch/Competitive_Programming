def r_string(_string):
    ch_count={}
    for ch in _string:
        if ch in ch_count:
            ch_count[ch]+=1
        else:
            ch_count[ch]=1

 
    for ch,count in ch_count.items():
        if count > 1:
            pass
    chs=set(ch_count.values())
    
    if len(chs)==1 and list(chs)[0]>=2:
        r_count=list(chs)[0]
        print(r_count)
        
        s_ch=sorted(ch_count.items())
        rearranged_string=''.join(ch*r_count for ch, _ in s_ch)
        
        print(rearranged_string)
    else:
        print(-1)
        

T = int(input())
for i in range(T):
    s = input()
    r_string(s)










    

