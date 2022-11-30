from array import *
from unidecode import unidecode

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

letterShift = 2

def fast_pow_mod(base, exp, mod):
    #exponenciacao modular rapida
    if exp < 0:
        return 1 / fast_pow_mod(base, -exp, mod)
    ans = 1
    while exp:
        if exp & 1:
            ans = (ans * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return ans

def criptografar(texto, shift, e, n):
    resultado = []
    for a in texto:
        #converte cada letra
        if(alfabeto.count(a)):
            a = fast_pow_mod(alfabeto.index(a) + shift, e, n)
            resultado.append(a)

    return resultado

def desencriptar(array, letterShift, d, n):
    resultado = ""
    for a in array:
        #converte cada letra
        a = fast_pow_mod(a, d, n)
        resultado += alfabeto[(a - letterShift) % len(alfabeto)]

    return resultado

def getCypherToDecrypt():
    f = open("message.txt", "r")
    content = f.read()
    content = content.split()
    content = [int(i) for i in content]

    f.close()
    return content

def setKey(d, n):
    f = open("key.txt", "w+")
    f.write("%d %d" % (d, n))
    f.close()

def getKey():
    f = open("key.txt", "r")
    content = f.read()
    content = content.split()
    content = [int(i) for i in content]
    f.close()
    return content

def setLock(e, n):
    f = open("lock.txt", "w+")
    f.write("%d %d" % (e, n))
    f.close()

def getLock():
    f = open("lock.txt", "r")
    content = f.read().split(' ')
    content = [int(i) for i in content]
    f.close()
    return content

def getMessageToEncrypt():
    f = open("text.txt", "r")
    content = f.read()
    f.close()
    return content

def setMessage(text):
    f = open("message.txt", "w+")
    for i in range(len(text)):
        f.write("%s " % text[i])
    print("salvo :)")
    f.close()
    return 0


def gcd(a, b):
    #algoritmo de euclides
    while b:
        a, b = b, a % b
    return a

def treatMessage(text):
    return unidecode(text.upper())
    
def modinv(a, b):
    #algoritmo de euclides extendido
    (r0, m0, n0) = a, 1, 0
    (r1, m1, n1) = b, 0, 1

    while(r0 % r1 > 0):
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        m0, m1 = m1, m0 - m1 * q
        n0, n1 = n1, n0 - n1 * q
    
    return m1 % b
