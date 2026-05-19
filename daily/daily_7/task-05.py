# digit_sum(1234)  → 10
# digit_sum(999)   → 27
# digit_sum(0)     → 0
num1 = 1234
num2 = 999
num3 = 0

def digit_sum(num: int) -> int:
    return sum(int(d) for d in str(num))

print(digit_sum(num1))
print(digit_sum(num2))
print(digit_sum(num3))