# SOC-24-Algorithmic-Number-Theory-and-Algebra-
A python file that contains various functions for Number theory and Algebra

Fuctions till now:
pair_gcd(a: int, b: int) -> int : Returns the GCD of a and b [Hint: Euclidean Algorithm]
pair_egcd(a: int, b: int) -> tuple[int, int, int] : Returns (x,y,d) where d is the GCD of a and b, and x and y are integers such that ax+by=d
gcd(*args: int) -> int: Returns the GCD of all integers provided as arguments [Assume 2 or more arguments are always passed]
pair_lcm(a: int, b: int) _> int : Returns the LCM of a and b
lcm(*args: int) -> int: Returns the LCM of all integers provided as arguments [Assume 2 or more arguments are always passed]
are_relatively_prime(a: int, b: int) -> bool: Returns True if a and b are relatively prime, False otherwise
mod_inv(a: int, n: int) -> int: Return the modular inverse of a modulo n. For this function, raise an Exception if a and n are not coprime
crt(a: list[int], n: list[int]) -> int: This function applies the Chinese Remainder Theorem to find the unique value of a modulo product of all n[i] such that a = a[i] (mod n[i]) [Assume all the n[i] are pairwise coprime and that the length of the two lists are the same and is nonzero)
is_quadratic_residue_prime(a: int, p: int) -> int: Return 1 if a is a quadratic residue modulo p, return -1 if a is a quadratic non-residue modulo p, return 0 if a is not coprime to p [Assume p is prime]
is_quadratic_residue_prime_power(a: int, p: int, e: int) -> int: Return 1 if a is a quadratic residue modulo p^e, return -1 if a is a quadratic non-residue modulo p^e, return 0 if a is not coprime to p^e [Assume p is prime and e >= 1]
