import math

def rsaAlgo(pi, qi, ri, si, msg):
    n = pi * qi * ri * si
    phi = (pi - 1) * (qi - 1) * (ri - 1) * (si - 1)
    e = 2
    
    while (e < phi):
        if(gcd(e, phi) == 1):
            break;
        else:
            e = e + 1

    d = pow(e, -1, phi)
    d = mod_fn(d, phi)      
    
    c = pow(msg, e)
    c = math.fmod(c, n)
    c = round(c)
    print("Encrypted Data before Bit Stuffing:", c)

    bs = 0
    ctemp = c
    while (ctemp > 0):
        r = ctemp % 10
        bs += r
        ctemp = ctemp / 10
    bs = math.fmod(bs, 9)
    bs = math.floor(bs)
    c = int(str(c) + str(bs))

    print("Encrypted Data after Bit Stuffing:", c)

    c = c / 10
    c = math.floor(c)
    print("Removing Bit Stuffing:", c)
    m = pow(c, d, n)
    print("Decrypted Data:", m)
    
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

def mod_fn(z, phi):
    return z % phi
    
p = int(input('P: '))
q = int(input('Q: '))
r = int(input('R: '))
s = int(input('S: '))
m = int(input('Message: '))

rsaAlgo(p, q, r, s, m)