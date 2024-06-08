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
    raise ValueError(f"Modular inverse does not exist: gcd({a},{n}) is not 1")
  return x%n

def crt(a: list[int], n: list[int]) -> int:
  if (len(a)!=len(n)):
    raise ValueError("Length of residues (a) and moduli (n) must be equal")
  for num in n:
    if(num<0):
      raise ValueError("Moduli (n) must contain positive integers only")
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