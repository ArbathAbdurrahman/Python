def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 13
hitung_fibonacci = fibonacci(n)
print(f"Fibonacci dari {n} adalah {hitung_fibonacci}.")

# Output: Fibonacci dari 8 adalah 21.


#dengan loop
def fibonacci_loop(n: int) -> int:
    numbers: list = []
    for i in range(0, n+1):
        if i <= 1:
            numbers.append(i)
        else:
            next_fib = numbers[i-1] + numbers[i-2]
            numbers.append(next_fib)
    return numbers[-1]
 
n = 5
hitung_fibonacci = fibonacci_loop(n)
print(f"Fibonacci dari {n} adalah {hitung_fibonacci}.")
 
# Output: Fibonacci dari 5 adalah 5.