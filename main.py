import time
from basic_eratosthenes import Eratosthenes
from basic_gries_misra import GriesMisra

n = 10 ** 3

def timedExecution(func):
    start_time = time.time()
    func(n)
    used_time = time.time() - start_time
    print("--- Execution time of %s is %s seconds ---" % (func.__qualname__, used_time))

print("testing with n = %s" % n)
timedExecution(Eratosthenes.find_prime)
timedExecution(GriesMisra.find_prime)
