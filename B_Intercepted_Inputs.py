def main():
    t=int(input())
    for _ in range(t):
        k=int(input())
        a=list(map(int, input().split()))
        s=k - 2
        l=[]
        
        for d in range(1, int(s**0.5) + 1):
            if s % d == 0:
                l.append((d, s // d))
                if d != s // d:
                    l.append((s // d, d))
        
        a.sort()
        flag=False
        
        for n, m in l:
            if n in a and m in a:
                print(f"{n} {m}")
                flag = True
                break
        
        if not flag:
            print("1 1")

if __name__ == "__main__":
    main()
