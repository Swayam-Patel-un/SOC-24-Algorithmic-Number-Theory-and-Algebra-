def pair_gcd(a: int, b: int) -> int:
  while(b!=0):
    r=a%b
    a=b
    b=r
  return a

def pair_egcd(a: int, b: int) -> tuple[int, int, int]:
  if (a==0):
    return 0,1,b
  else:
    x,y,g=pair_egcd(b% a,a)
    return y-(b//a)*x,x,g
  
def gcd(*args: int) -> int:
  if(len(args)<2):
    raise ValueError("Lenght of input is lesser than 2")
  else:
    g=args[0]
    for x in args[1:]:
      g=pair_gcd(g,x)
    return g

def pair_lcm(a: int, b: int) -> int:
  g=pair_gcd(a,b)
  return a*b//g

def lcm(*args: int) -> int:
  if(len(args)<2):
    raise ValueError("Lenght of input is lesser than 2")
  else:
    l=args[0]
    for x in args[1:]:
      l=pair_lcm(l,x)
    return l

def are_relatively_prime(a: int, b: int) -> bool:
  if(pair_gcd(a,b)==1):
    return True
  else:
    return False
  
def mod_inv(a: int, n: int) -> int:
  x,y,g=pair_egcd(a,n)
  if g!=1:
    raise ValueError("Modular inverse does not exist: gcd(",a,",",n,") is not 1")
  return x%n

def crt(a: list[int], n: list[int]) -> int:
  if (len(a)!=len(n)):
    raise ValueError("Length of residues and moduli must be equal")
  for num in n:
    if(num<0):
      raise ValueError("Moduli must contain positive integers only")
  pr=1
  for num in n:
    pr*=num
  x=0
  p=[0]*len(n)
  for i in range(len(n)):
    p[i]=pr//n[i]
  for i in range(len(n)):
    p[i]=mod_inv(p[i], n[i])
  for i in range(len(n)):
    x= (x+(a[i]*p[i]*pr//n[i]))%pr
  return x

def is_quadratic_residue_prime(a: int, p: int) -> int:
  if a%p==0:
    return 0
  l=pow(a,(p-1)//2,p)
  if l==p-1:
    return -1
  return l

def is_quadratic_residue_prime_power(a: int, p: int, e: int) -> int:
  if a%p==0:
    return 0
  if e==1:
    return is_quadratic_residue_prime(a, p)
  if is_quadratic_residue_prime(a, p)==-1:
    return -1
  else:
    if pow(a,(p**(e-1)*(p-1))//2,p**e)==1:
      return 1
    else:
      return -1
    
def floor_sqrt(x: int) -> int:
  if x < 0:
    raise ValueError("x must be a non-negative integer")
  k = (x.bit_length()-1)//2
  m = 2**k
  for i in range(k-1,-1,-1):
    if (m+2**i)**2<= x:
        m+=2**i
  return m

def is_perfect_power(x: int) -> bool:
    for b in range(2,floor_sqrt(x)+1):
        a = round(x**(1/b))
        if a**b==x:
            return True
    return False
  
def factor(n: int) -> list[tuple[int, int]]:
    if n<=1:
        return []
    factors=[]
    for p in range(2,floor_sqrt(n)+1):
        if n%p==0:
            c=0
            while n%p==0:
                n//=p
                c+=1
            factors.append((p,c))
    if n>1:
        factors.append((n,1))
    return factors
  
def euler_phi(n: int) -> int:
  if n==1:
    return 1
  ep=1
  for p,c in factor(n):
    ep*=p**(c-1)*(p-1)
  return ep
     
import random

def mr(d:int, n:int) -> bool:
    a=2+random.randint(1, n - 4)
    x=pow(a,d,n)
    if x==1 or x==n-1:
        return True
    while d!=n-1:
        x=(x*x)%n
        d*=2
        if x==1:
            return False
        if x==n-1:
            return True
    return False

def is_prime(n: int) -> bool:
    if n<=1:
      return False
    if n<=3:
      return True
    if n%2==0 or n%3==0:
      return False

    d=n-1
    while d%2==0:
        d//=2
    
    k=random.randint(7,10)

    for _ in range(k):
      if not mr(d, n):
        return False
    return True

def gen_prime(m: int) -> int:
    while True:
      num = random.randint(2, m)
      if is_prime(num):
          return num

def gen_k_bit_prime(k: int) -> int:
    while True:
        num=random.randint(2**(k-1),2**k-1)
        if is_prime(num):
            return num

def log(n: int, b: int) -> int:
  if n<0:
    raise ValueError("Log of negative number, not possible")
  c=0
  while n>1:
    n//=b
    c+=1
  return c

def aks_test(n: int) -> bool:
  if is_perfect_power(n):
    return False
  r = 1
  while True:
    r += 1
    if gcd(n, r) != 1:
      continue
    order = 1
    while pow(n, order, r) != 1:
      order += 1
    if order > floor_sqrt(r) * log(n,2):
      break
  for a in range(1, min(n, r)):
    if gcd(a, n) > 1:
      return False
    if pow(a, n, n) != a % n:
      return False
  return True

class QuotientPolynomialRing:
  def __init__(self, poly: list[int], pi_gen: list[int]) -> None:
    if (pi_gen[-1]) != 1:
      raise ValueError("Quotient polynomial must be monic.")
    self.element = poly
    self.pi_generator = pi_gen
  
  def __len__(self):
    return len(self.element)
    
  @staticmethod
  def _check_pi_generators(poly1, poly2):
    if poly1.pi_generator != poly2.pi_generator:
      raise ValueError("The two polynomials must have the same pi_generator.")
  
  @staticmethod  
  def _modulus(poly, mod):
    while len(poly) >= len(mod):
      if poly[-1] != 0:
        for i in range(len(mod)):
          poly[len(poly) - len(mod) + i] -= poly[-1] * mod[i]
      poly.pop()
    return poly
  
  def _tomonic(poly):
    if QuotientPolynomialRing._empty(poly):
      return "Empty"
    elif len(poly)==0:
      return ValueError("lenght is 0")
    else:
      lc=poly[len(poly)-1]
      if lc!=0:
        poly=[(c/lc) for c in poly]
      return poly
    
  
  @staticmethod  
  def modulusm(poly, mod):
    poly=QuotientPolynomialRing._tomonic(poly)
    if poly=="Empty":
      return [0]
    mod=QuotientPolynomialRing._tomonic(mod)
    while len(poly) >= len(mod):
      if poly[-1] != 0:
        for i in range(len(mod)):
          poly[len(poly) - len(mod) + i] -= poly[-1] * mod[i]
      poly.pop()
    poly=QuotientPolynomialRing._tomonic(poly)
    return poly
  
  @staticmethod
  def _empty(poly):
    s=0
    if poly=="Empty":
      return True
    for i in range(len(poly)):
      s+=poly[i]
    if s==0:
      return True
    else:
      return False
      
  @staticmethod
  def _polyadd(a,b):
    max_len = max(len(a), len(b))
    result = [0] * max_len
    for i in range(len(a)):
      result[i] = a[i]
    for i in range(len(a)):
      result[i] += b[i]
    return result
  
  @staticmethod
  def _polysub(a,b):
    max_len = max(len(a), len(b))
    result = [0] * max_len
    for i in range(len(a)):
      result[i] = a[i]
    for i in range(len(b)):
      result[i] -= b[i]
    return result
  
  @staticmethod
  def _polymul(a,b):
    result = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)): 
      for j in range(len(b)):
        result[i + j] += a[i] * b[j]
    return result
  
  @staticmethod
  def _polygcd(a,b):
    d=len(a)
    while(not QuotientPolynomialRing._empty(b)):
      r=QuotientPolynomialRing.modulusm(a,b)
      a=b
      b=r
      if (b==[0]):
        break
      QuotientPolynomialRing._modulus(a,b)
    for _ in range(len(a)-1,d-1):
      a.append(0)
    return a
    
  @staticmethod
  def Add(poly1, poly2):
    QuotientPolynomialRing._check_pi_generators(poly1, poly2)
    result=QuotientPolynomialRing._polyadd(poly1.element,poly2.element)
    result=QuotientPolynomialRing._modulus(result,poly1.pi_generator)
    return QuotientPolynomialRing(result, poly1.pi_generator)
  
  @staticmethod
  def Sub(poly1, poly2):
    QuotientPolynomialRing._check_pi_generators(poly1, poly2)
    result=QuotientPolynomialRing._polysub(poly1.element,poly2.element)
    result=QuotientPolynomialRing._modulus(result,poly1.pi_generator)
    return QuotientPolynomialRing(result, poly1.pi_generator)
  
  @staticmethod
  def Mul(poly1, poly2):
    QuotientPolynomialRing._check_pi_generators(poly1, poly2)
    result = QuotientPolynomialRing._polymul(poly1.element,poly2.element)
    result = QuotientPolynomialRing._modulus(result, poly1.pi_generator)
    return QuotientPolynomialRing(result, poly1.pi_generator)
  
  @staticmethod
  def GCD(poly1, poly2):
    QuotientPolynomialRing._check_pi_generators(poly1,poly2)
    result=QuotientPolynomialRing._polygcd(poly1.element,poly2.element)
    QuotientPolynomialRing._modulus(result,poly1.pi_generator)
    return QuotientPolynomialRing(result,poly1.pi_generator)
  
  
  @staticmethod
  def Inv(poly):
    def exeu(h,f):
      p1=QuotientPolynomialRing(h,f)
      p2=QuotientPolynomialRing(f,f)
      MOD=f
      print(MOD)
      gcd=QuotientPolynomialRing._polygcd(p1.element,p2.element)
      print("MOD", gcd)
      ch=[1]+[0]*(len(gcd)-1)
      print("Second",gcd, "other ",ch)
      if gcd !=ch:
        return ValueError("Non invertible pair")
      r=f
      print("f ",r)
      r1=h
      s=[1]
      s1=[0]
      t=[0]
      t1=[1]
      while r1!=[0]:
        q,r2=QuotientPolynomialRing.polydivmod(r,r1)
        r=r1
        s=s1
        t=t1
        r1=r2
        s1=QuotientPolynomialRing._polysub(s,QuotientPolynomialRing._polymul(s1,q))
        t1=QuotientPolynomialRing._polysub(t,QuotientPolynomialRing._polymul(t1,q))
        print("t ",t)
        if r==[1]:
          break
        print(MOD)
      return t,poly.pi_generator
    result=QuotientPolynomialRing([],poly.pi_generator)
    print("Before:")
    print(result.element,"\t", result.pi_generator)
    result.element=exeu(poly.element,poly.pi_generator)
    print("After:")
    print(result.element,"\t", result.pi_generator)
    return result
  
  
  @staticmethod
  def polydivmod(dividend, divisor):
        # Ensure the divisor is monic
        if divisor[-1] != 1:
            raise ValueError("Divisor polynomial must be monic.")
        
        quotient = [0] * (len(dividend) - len(divisor) + 1)
        remainder = dividend[:]
        
        while len(remainder) >= len(divisor):
            if remainder[-1] != 0:
                leading_coefficient_ratio = remainder[-1]
                quotient_term_degree = len(remainder) - len(divisor)
                quotient[quotient_term_degree] = leading_coefficient_ratio
                
                for i in range(len(divisor)):
                    remainder[quotient_term_degree + i] -= leading_coefficient_ratio * divisor[i]
            
            remainder.pop()
        
        return quotient, remainder
