def fizzbuzz(number: int) -> list:
    fizzbuzz_list = []
    for n in range(1, number + 1, 1):
        if n % 15 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif n % 5 == 0:
            fizzbuzz_list.append("Buzz")
        elif n % 3 == 0:
            fizzbuzz_list.append("Fizz")
        else:
            fizzbuzz_list.append(n)
    return fizzbuzz_list

print(fizzbuzz(15))