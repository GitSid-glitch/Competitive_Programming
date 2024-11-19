def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
            

def check(n):
     for m in range(1,1001):
          x=n*m+1
          if not is_prime(x):
               print(m)
               return

n=int(input())
check(n)