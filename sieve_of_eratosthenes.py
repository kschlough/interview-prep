# from ctci
# find all primes smaller than or equal to int n
# exponential time complexity, o(n) linear space complexity

def sieve_of_eratosthenes(n):
    # list of consecutive integers from 2 up through n value
    # but list of boolean values instead of #s
    # each index location if true signifies we have a prime number at that spot
    is_prime = [True] * (n - 1) 

    p = 2 # smallest prime

    # iterate & enumerate all the multiples of p
    # cross off each multiple in our is_prime list to signify is composite not prime
    while True:
        multiplier = 2
        # all multiples of possible prime
        multiple = p * multiplier # 2p, 3p, 4p, etc.

        # nested while loop of all p multiples
        while multiple <= n:
            is_prime[multiple - 2] = False # eg. 4 is at index 2 because we start is_prime at 2
            multiplier += 1
            multiple = p * multiplier

        # find our new prime #
        for i, prime in enumerate(is_prime): # iterate over is_prime index
            if prime and i + 2 > p:
                p = i + 2 # map from prime value to index
                break
        else:
            break # if we never find a bigger prime, end of algorithm

    for i, prime in enumerate(is_prime): # once we've removed all composites
        if prime: 
            print(i + 2 ) # print the actual mapped value
    


# test cases
sieve_of_eratosthenes(30)
# should output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

sieve_of_eratosthenes(7)
# should output: 2, 3, 5, 7

sieve_of_eratosthenes(10)
# should output: 2, 3, 5, 7

sieve_of_eratosthenes(20)
# should output: 2, 3, 5, 7, 11, 13, 17, 19