# basic sieve of eratosthenes
class Eratosthenes:
    @classmethod
    def find_prime(cls, n):
        prime = []
        sieve = [True]*(n+1)
        for i in range(2, n):
            if sieve[i]:
                prime.append(i)
                for j in range (i*i, n, i):
                    sieve[j] = False
        return prime
