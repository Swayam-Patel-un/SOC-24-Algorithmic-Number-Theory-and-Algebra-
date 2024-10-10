# SOC-24: Algorithmic Number Theory and Algebra

This project, part of the Summer of Code (SOC) under the **Web and Coding Club (WnCC)** at IIT Bombay, focuses on the implementation of key algorithms in number theory and algebra. The project is mentored by **Nilabha Saha** and implemented from the book *A Computational Introduction to Number Theory and Algebra* by **Victor Shoup**.

## Implemented Functions

### 1. `pair_gcd(a: int, b: int) -> int`
Returns the GCD of `a` and `b` (Hint: Euclidean Algorithm).

### 2. `pair_egcd(a: int, b: int) -> tuple[int, int, int]`
Returns a tuple `(x, y, d)` where `d` is the GCD of `a` and `b`, and `x` and `y` are integers such that `a*x + b*y = d`.

### 3. `gcd(*args: int) -> int`
Returns the GCD of all integers provided as arguments (Assume 2 or more arguments are always passed).

### 4. `pair_lcm(a: int, b: int) -> int`
Returns the LCM of `a` and `b`.

### 5. `lcm(*args: int) -> int`
Returns the LCM of all integers provided as arguments (Assume 2 or more arguments are always passed).

### 6. `are_relatively_prime(a: int, b: int) -> bool`
Returns `True` if `a` and `b` are relatively prime, `False` otherwise.

### 7. `mod_inv(a: int, n: int) -> int`
Returns the modular inverse of `a` modulo `n`. Raises an exception if `a` and `n` are not coprime.

### 8. `crt(a: list[int], n: list[int]) -> int`
Applies the Chinese Remainder Theorem to find the unique value of `a` modulo the product of all `n[i]`, such that `a = a[i] (mod n[i])`. Assumes all `n[i]` are pairwise coprime and the lengths of `a` and `n` are the same.

### 9. `is_quadratic_residue_prime(a: int, p: int) -> int`
Returns `1` if `a` is a quadratic residue modulo `p`, `-1` if `a` is a quadratic non-residue, and `0` if `a` is not coprime to `p` (Assumes `p` is prime).

### 10. `is_quadratic_residue_prime_power(a: int, p: int, e: int) -> int`
Returns `1` if `a` is a quadratic residue modulo `p^e`, `-1` if `a` is a quadratic non-residue, and `0` if `a` is not coprime to `p^e` (Assumes `p` is prime and `e >= 1`).

### 11. `floor_sqrt(x: int) -> int`
Returns the floor of the square root of `x` (Assumes `x > 0`).

### 12. `is_perfect_power(x: int) -> bool`
Returns `True` if `x` is a perfect power (Assumes `x > 1`).

### 13. `is_prime(n: int) -> bool`
Uses the **Miller-Rabin test** to return `True` if `n` is (probably) prime or `False` if it is composite. (Assumes `n > 1` and chooses a good set of bases).

### 14. `gen_prime(m: int) -> int`
Generates a random prime number `p` such that `2 <= p <= m` (Assumes `m > 2`).

### 15. `gen_k_bit_prime(k: int) -> int`
Generates a random `k`-bit prime number, that is, a prime number `p` such that `2^(k-1) <= p < 2^k` (Assumes `k >= 1`).

### 16. `factor(n: int) -> list[tuple[int, int]]`
Returns the prime factorization of `n`. (Assumes `n >= 1` and returns a list of tuples where the first component is the prime factor and the second component is the corresponding power in the factorization).

### 17. `euler_phi(n: int) -> int`
Returns the **Euler phi function** of `n`.

### 18. `aks_test(n: int) -> bool`
Uses the **AKS deterministic primality test** to return `True` if `n` is prime or `False` if it is composite (Assumes `n > 1`).

### 19. **`QuotientPolynomialRing` Class**
This class represents elements in a univariate polynomial ring over integers modulo some specified monic polynomial in the same ring. Polynomials are represented using a list of ints where the `i^th` index represents the coefficient of `X^i`.

#### Methods:
- **`__init__(self, poly: list[int], pi_gen: list[int]) -> None`**: Initializes the object as required. Raises an exception if `pi_gen` is empty or not monic.
- **`Add(poly1: QuotientPolynomialRing, poly2: QuotientPolynomialRing) -> QuotientPolynomialRing`**: Adds two polynomials modulo `pi_generator`. Raises an exception if `pi_generators` differ.
- **`Sub(poly1: QuotientPolynomialRing, poly2: QuotientPolynomialRing) -> QuotientPolynomialRing`**: Subtracts two polynomials modulo `pi_generator`. Raises an exception if `pi_generators` differ.
- **`Mul(poly1: QuotientPolynomialRing, poly2: QuotientPolynomialRing) -> QuotientPolynomialRing`**: Multiplies two polynomials modulo `pi_generator`. Raises an exception if `pi_generators` differ.
- **`GCD(poly1: QuotientPolynomialRing, poly2: QuotientPolynomialRing) -> QuotientPolynomialRing`**: Returns the GCD of two polynomials modulo `pi_generator`. Raises an exception if `pi_generators` differ.
- **`Inv(poly: QuotientPolynomialRing) -> QuotientPolynomialRing`**: Returns the modular inverse of a polynomial modulo `pi_generator`. Raises an exception if the polynomial is not invertible.

### 20. `get_generator(p: int) -> int`
Returns a generator of `(Z_p)^*` (Assumes `p` is prime).

### 21. `discrete_log(x: int, g: int, p: int) -> int`
Returns the discrete logarithm of `x` to the base `g` in `(Z_p)^*` (Assumes `p` is prime). Raises an exception if the discrete logarithm does not exist.

### 22. `legendre_symbol(a: int, p: int) -> int`
Returns the value of the **Legendre Symbol** `(a | p)` (Assumes `p` is prime).

### 23. `jacobi_symbol(a: int, n: int) -> int`
Returns the value of the **Jacobi Symbol** `(a | n)` (Assumes `n` is positive).

### 24. `modular_sqrt_prime(x: int, p: int) -> int`
Returns the modular square root of `x` modulo `p` (Assumes `p` is prime). Raises an exception if the square root does not exist.

### 25. `modular_sqrt_prime_power(x: int, p: int, e: int) -> int`
Returns the modular square root of `x` modulo `p^e` (Assumes `p` is prime and `e >= 1`). Raises an exception if the square root does not exist.

### 26. `modular_sqrt(x: int, n: int) -> int`
Returns the modular square root of `x` modulo `n` (Assumes `n >= 1`). Raises an exception if the square root does not exist (Not working yet).

### 27. `is_smooth(m: int, y: int) -> bool`
Returns `True` if `m` is `y`-smooth, `False` otherwise.

### 28. `probabilistic_dlog(x: int, g: int, p: int) -> int`
Returns the discrete log of `x` to the base `g` in `(Z_p)^*` using a **subexponential probabilistic algorithm**. (Assumes `p` is prime, and `g` is a generator of `(Z_p)^*`). Raises an exception if the square root does not exist.

### 29. `probabilistic_factor(n: int) -> list[tuple[int, int]]`
Returns the prime factorization of `n` using a **subexponential probabilistic algorithm**. (Assumes `n >= 1` and returns a list of tuples where the first component is the prime factor and the second component is the corresponding power in the factorization).
