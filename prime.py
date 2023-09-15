def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(N):
    prime_list = []
    for i in range(2, N + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
N = int(input(" Please enter a number between 50 and 100: "))
if 50 <= N <= 100:
    prime_numbers = generate_primes(N)
    print("Prime numbers from 1 to", N, "are:", prime_numbers)
else:
    print("Invalid input. N should be between 50 and 100.")
