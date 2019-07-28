import time
from basic_eratosthenes import Eratosthenes

n = 10 ** 5

def timedExecution(func):
    start_time = time.time()
    func(n)
    used_time = time.time() - start_time
    print("--- Execution time of %s is %s seconds ---" % (func.__qualname__, used_time))

print("testing with n = %s" % n)
timedExecution(Eratosthenes.find_prime)
