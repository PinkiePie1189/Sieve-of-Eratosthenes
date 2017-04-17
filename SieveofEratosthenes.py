from math import sqrt #FOR V2
import itertools #FOR V3
import time

"""
~~ Sieve of Eratosthenes ~~
"""

print "Sum of prime numbers up to 2 million."
print
print "Version 1"
start = time.time()
m = 2*10**6
 
def fast__primes_under(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n = n-n%6+6
    correction = 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]] 

print sum(fast__primes_under(m))
end = time.time() - start
print "Runtime =", end

#V2
print
print "Version 2"
start = time.time()
def sum_range(n):
    A = [1 if i > 1 else 0 for i in xrange(n+1)]
    for i, p in enumerate(A):
        if A[i] and i < int(sqrt(n)):
            for j in xrange(i, len(A), i):
                if i == j:
                    continue
                A[j] = 0
    return sum([i[0] for i in enumerate(A) if A[i[0]]])
    
if __name__ == '__main__':
    primesum = sum_range(1000*1000*2)
    print "{}".format(primesum)
    end = time.time()
    print "Runtime =", end

#V3
print
print "Version 3"
# number to find summation of all primes below number
start = time.time()
hi = 2000000

# create a set excluding even numbers
numbers = set(xrange(3, hi + 1, 2)) 

for number in xrange(3, int(hi ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < hi:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print 2 + sum(numbers)
end = time.time() - start
print "Runtime =", end

#V4
print
print "Version 4"
start = time.time()
primes_below_number = 2000000
numbers = [v % 2 != 0 for v in xrange(primes_below_number)]
numbers[0] = False
numbers[1] = False
numbers[2] = True

number = 3

while number < primes_below_number:
    n = number * 3  # We already excluded even numbers
    while n < primes_below_number:
        numbers[n] = False
        n += number
    number += 1
    while number < primes_below_number and not numbers[number]:
        number += 1

sum_of_numbers = sum(itertools.imap(lambda index_n: index_n[1] and index_n[0] or 0, enumerate(numbers)))

print(sum_of_numbers)
end = time.time() - start
print "Runtime =", end
