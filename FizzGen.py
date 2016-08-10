from sys import argv

def generatePrimes(words):
    limit = len(words) ** 2
    notPrimes = []
    for a in range(3, limit):
        for b in range(a * 2, limit, a):
            notPrimes += [b]
    notPrimes = set(notPrimes)

    i = 3
    x = []
    while len(x) < len(words):
        if not i in notPrimes: x += [(words[len(x)], i)]
        i += 2
    return x

if __name__ == "__main__":
    if len(argv) < 3:
        print "FizzGen requires at least 2 arguments. An int, and some strings."
        rangeLimit = 100
        primes = [("Fizz", 3), ("Buzz", 5), ("Bar", 7)]
    else:
        rangeLimit = int(argv[1]) + 1
        primes = generatePrimes(argv[2:])

    for number in range(1, rangeLimit):
        print ''.join([ 
            string 
            for string, prime in primes
            if number % prime == 0 ]) or number
