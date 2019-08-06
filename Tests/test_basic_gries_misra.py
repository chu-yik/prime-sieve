# testing basic eratosthenes prime sieve

import unittest
from basic_gries_misra import GriesMisra

class TestBasicEratosthenes(unittest.TestCase):
    def test_10_3(self):
        prime = GriesMisra.find_prime(10 ** 3)
        print(len(prime))
        self.assertEqual(len(prime), 168)

    def test_10_4(self):
        prime = GriesMisra.find_prime(10 ** 4)
        print(len(prime))
        self.assertEqual(len(prime), 1229)

    def test_10_5(self):
        prime = GriesMisra.find_prime(10 ** 5)
        print(len(prime))
        self.assertEqual(len(prime), 9592)

    def test_10_6(self):
        prime = GriesMisra.find_prime(10 ** 6)
        print(len(prime))
        self.assertEqual(len(prime), 78498)
