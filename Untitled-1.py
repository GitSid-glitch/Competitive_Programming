
def num_of_digits(n):
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits


def is_armstrong(num):
    original_num = num
    digits = num_of_digits(num)
    sum_of_powers = 0
    
    
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** digits
        num //= 10
    
  
    return sum_of_powers == original_num


def find_armstrong_in_range(start, end):
    armstrong_numbers = []
    for i in range(start, end + 1):
        if is_armstrong(i):
            armstrong_numbers.append(i)
    
    return armstrong_numbers


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))


armstrong_numbers = find_armstrong_in_range(a, b)
print("Armstrong numbers:", armstrong_numbers)
'''


def find_armstrong_in_range(a, b):
    def is_armstrong(num):
        def num_of_digits(n):
            digits = 0
            while n > 0:
                digits += 1
                n //= 10
            return digits
        original_num = num
        digits = num_of_digits(num)
        sum_of_powers = 0
        
        while num > 0:
            digit = num % 10
            sum_of_powers += digit ** digits
            num //= 10
    
  
        return sum_of_powers == original_num



    armstrong_numbers = []
    for i in range(a, b + 1):
        if is_armstrong(i):
            armstrong_numbers.append(i)
        for l in armstrong_numbers:
            print(l)