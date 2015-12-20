from itertools import count

def Fibonacci(startWithRepeatingOnes = False):
    '''Generator for the Fibonacci sequence'''
    n1 = 1
    yield n1
    n2 = 1 if startWithRepeatingOnes else 2
    yield n2
    while True:
        n3 = n1 + n2
        yield n3
        n1 = n2
        n2 = n3

def Primes():
    '''Generator for prime numbers'''
    D = {} # map each composite integer to its first found prime factor
    for q in count(2): #q gets 2, 3, 4, 5, ...
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, therefore q is prime
            yield q
            # mark q^2 as not prime, with q as first prime factor
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p

def TriangleNumbers():
    '''
    Generator for Triangle numbers

    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    '''
    num = 0
    for i in count(1):
        num += i
        yield num

if __name__ == '__main__':
    import unittest

    class Tests(unittest.TestCase):
        def test_Fibonacci(self):
            cases = [{'index': 0, 'startWithRepeatingOnes': False, 'answer': 1},
                     {'index': 1, 'startWithRepeatingOnes': False, 'answer': 2},
                     {'index': 1, 'startWithRepeatingOnes': True, 'answer': 1},
                     {'index': 2, 'startWithRepeatingOnes': False, 'answer': 3},
                     {'index': 3, 'startWithRepeatingOnes': False, 'answer': 5}]
            for case in cases:
                index = case['index']
                startWithRepeatingOnes = case['startWithRepeatingOnes']
                expected = case['answer']
                with self.subTest(index=index, startWithRepeatingOnes=startWithRepeatingOnes, expected=expected):
                    fib = Fibonacci(startWithRepeatingOnes)
                    answer = None
                    for i in range(-1, index):
                        answer = fib.__next__()
                    self.assertEqual(expected, answer)

        def test_Primes(self):
            cases = [{'index': 0, 'answer': 2},
                     {'index': 1, 'answer': 3},
                     {'index': 2, 'answer': 5},
                     {'index': 3, 'answer': 7}]
            for case in cases:
                index = case['index']
                expected = case['answer']
                with self.subTest(index=index, expected=expected):
                    p = Primes()
                    answer = None
                    for i in range(-1, index):
                        answer = p.__next__()
                    self.assertEqual(expected, answer)

        def test_TriangleNumbers(self):
            cases = [{'index': 0, 'answer': 1},
                     {'index': 1, 'answer': 3},
                     {'index': 2, 'answer': 6},
                     {'index': 3, 'answer': 10}]
            for case in cases:
                index = case['index']
                expected = case['answer']
                with self.subTest(index=index, expected=expected):
                    t = TriangleNumbers()
                    answer = None
                    for i in range(-1, index):
                        answer = t.__next__()
                    self.assertEqual(expected, answer)

    unittest.main()