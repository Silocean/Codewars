/*
Description:

We need a function prime_bef_aft() that gives the largest prime below a certain given value n,

befPrime or bef_prime (depending on the language),

and the smallest prime larger than this value,

aftPrime/aft_prime (depending on the language).

The result should be output in a list like the following:

prime_bef_aft(n) == [befPrime, aftPrime]
If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:

prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
Happy coding!!
 */
class BeforeAfterPrimes {
    
    public static long[] primeBefAft(long num) {
        long[] result = new long[2];
        for (long i = num-1; ; i--) {
            if (isPrime(i)) {
                result[0] = i;
                break;
            }
        }
        for (long i = num+1; ; i++) {
            if (isPrime(i)) {
                result[1] = i;
                break;
            }
        }
        return result;
    }

    public static boolean isPrime(long num) {
        for (long i = 2; i < num / 2; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}