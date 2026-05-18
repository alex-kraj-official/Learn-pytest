number = 97

def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for i in range(2, number, 1):
        if number % i == 0:
            return False           
    return True

print(is_prime(number))