'''def exchange_card(n,m,card):
    even=0 

    for i in card:  
        if i%2==0:  
            even+=1
    odd=n-even  

    if n%2!=0:
        print(-1)
        return
    
    half=n//2  
    a=max(0,half-even)
    b=max(0,half-odd)

    if a > m//2 or b > (m+1)//2:
        print(-1)
        return

    
    set_u=set(card)  
    new_list=list(set_u)  

    e=0 
    for i in range(2,m+1,2):
        if a <= 0:
            break
        if i not in set_u:
            new_list.append(i)
            a-=1
            e+=1  

    for i in range(1,m+1,2):
        if b <= 0:
            break
        if i not in set_u:
            new_list.append(i)
            b-=1
            e+=1  

    new_list.sort()

    print(e)  
    print(' '.join(map(str,new_list)))

n, m=map(int,input().split())
card=list(map(int, input().split()))
exchange_card(n,m,card)


'''



def udit():
    n,m=map(int,input().split())
    a=list(map(int, input().split()))
    
  
    e=[x for x in a if x % 2 == 0]
    o=[x for x in a if x % 2 != 0]
    
    udit_cards = list(set(a))
    distinct_even = [x for x in udit_cards if x % 2 == 0]
    distinct_odd = [x for x in udit_cards if x % 2 != 0]
    
    count_e = len(distinct_even)
    count_o = len(distinct_odd)
    
    half = n // 2

    if abs(count_e - count_o) > (n // 2):
        print(-1)
        return

    opponent_evens = [x for x in range(2, m+1, 2) if x not in udit_cards]
    opponent_odds = [x for x in range(1, m+1, 2) if x not in udit_cards]

    exchanges = 0

    if count_e > half:
        excess_evens = count_e - half
        for even in sorted(distinct_even, reverse=True):
            if excess_evens == 0:
                break
            if opponent_odds:
                udit_cards.remove(even)
                udit_cards.append(opponent_odds.pop(0))
                excess_evens -= 1
                exchanges += 1

    elif count_o > half:
        excess_odds = count_o - half
        for odd in sorted(distinct_odd, reverse=True):
            if excess_odds == 0:
                break
            if opponent_evens:
                udit_cards.remove(odd)
                udit_cards.append(opponent_evens.pop(0))
                excess_odds -= 1
                exchanges += 1

    udit_cards = sorted(list(set(udit_cards)))

    while len(udit_cards) < n:
        if len(distinct_even) < half and opponent_evens:
            udit_cards.append(opponent_evens.pop(0))
            exchanges += 1
        elif len(distinct_odd) < half and opponent_odds:
            udit_cards.append(opponent_odds.pop(0))
            exchanges += 1

    udit_cards = sorted(udit_cards)
    
    print(exchanges)
    print(" ".join(map(str, udit_cards)))

udit()
