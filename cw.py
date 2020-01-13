import random
p=0
q=0

#Euclid's Algorithm for determining the greatest common divisor
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def multipl_inv(e,tot):
    '''
    d=0
    x1,x2,y1=0,1,1
    temp_tot=tot

    while e>0:
        temp1=temp_tot /e
        temp2 = temp_tot - temp1*e
        temp_tot = e
        e=temp2

        x=x2-temp1*x1
        y= d- temp1*y1

        x2=x1
        x1=x
        d=y1
        y1=y

    if temp_tot == 1:
        return d+tot
    '''
    # d= (1+k mod(tot))/e
    k=0
    d=(1+k*tot)/e
    while not(d.is_integer()):
        k+=1
        d=(1+k*tot)/e
    return(d)


'''
///////////////////////////////////////////////////
This is known as the 6k ± 1 optimization method.
///////////////////////////////////////////////////
function is_prime(n)
    if n ≤ 3
        return n > 1
    else if n mod 2 = 0 or n mod 3 = 0
        return false
    let i ← 5
    while i * i ≤ n
        if n mod i = 0 or n mod (i + 2) = 0
            return false
        i ← i + 6
    return true
///////////////////////////////////////////////////
'''
def is_prime(n):
    if n<=3:
        return n>1      #if less than or equal to 3{3,2,1} return true if n=2 or 3
    if n % 2 == 0 or n % 3 ==0:
        return False
    # for num in range(3,n)
    i=5
    while i*i<=n:
        if n%i == 0 or n % (i+2)==0:
            return False
        i+=6
    return True

def gen_nums():
    global p,q
    if not is_prime(p):
        p=random.randint(100,1000)
    if not is_prime(q):
        q=random.randint(100,1000)

    if p==q:
        gen_nums()

def main():
    global pubkey,prvkey    
    while not(is_prime(p) and is_prime(q)):
        gen_nums()
    print(p,"\n",q)
    pubkey,prvkey=gen_key()
    print(pubkey,prvkey)

def gen_key():
    global p,q
    #calculate n
    n = p*q
    #calculate Euler's totient "tot"
    tot=(p-1)*(q-1)

    # calculate public key
    # to calculate e::part of public key
    e=0
    while gcd(e,tot)!=1:
        e=random.randint(1,tot)
    # calculate the private key
    # to calculate the private key, multiplicative inverse is used
    d=int(multipl_inv(e,tot))
    public_key=(n,e)
    private_key=(n,d)
    return (public_key,private_key)

def encrypt(num):
    global encrypted
    n,e=pubkey
    encrypted=(num**e)%n
    print(encrypted)
    decrypt()
    
def decrypt():
    n,d=prvkey
    decrypted=(encrypted**d)%n
    print(decrypted)
main()
encrypt(4)

