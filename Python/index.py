from array import *

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V',
    'W', 'X', 'Y', 'Z', ' ']

letterShift = 2

def convert(b, e, n):
    #faz a conversao do texto
    return pow(b, e) % n

def criptografar(texto, shift):
    resultado = []
    for a in texto:
        #converte cada letra
        a = convert(alfabeto.index(a) + shift, e, n)
        resultado.append(a)
    saveMessage(resultado)
    return resultado

def desencriptar(array):
    resultado = ""
    for a in array:
        #converte cada letra
        a = convert(a, d, n)
        resultado += alfabeto[a - letterShift]
    print("d: %d" % d)
    return resultado

def getMessage():
    f = open("message.txt", "r")
    content = f.read()[1:]
    content = content[:len(content) - 1].split(',')
    for i in range(len(content)):
        content[i] = int(content[i])
    f.close()
    return content

def getKey():
    f = open("key.txt", "r")
    content = f.read()
    content = content.split(',')
    for i in range(len(content)):
        content[i] = int(content[i])
    f.close()
    return content

def getLock():
    f = open("lock.txt", "r")
    content = f.read()
    content = content.split(',')
    for i in range(len(content)):
        content[i] = int(content[i])
    f.close()
    return content

def saveMessage(text):
    f = open("message.txt", "w+")
    f.write("%s" % text)
    print("salvo :)")
    f.close()
    return 0

def saveKey(p, q, d):
    resultado = str(p) + ',' + str(q) + ',' + str(d)
    f = open("key.txt", "w+")
    f.write("%s" % resultado)
    print("salvo :)")
    f.close()

def saveLock(p, q, l, n):
    resultado = str(p) + ',' + str(q) + ',' + str(l) + ',' + str(n)
    f = open("lock.txt", "w+")
    f.write("%s" % resultado)
    print("salvo :)")
    f.close()

def modinv(a, m):
    #testa um por um os valores de 1 a m
    for x in range(1, m):
        #checa se x é inverso de a mod m
        if (a * x) % m == 1:
            return x
    return None

#prompt para o usuario escolher a programação
programa = int(input("Digite\n1-Gerar chave publica\n2-Encriptar\n3-Desencriptar\n4-Gerar Decriptador\n"))

if programa == 1:
    # Gerar chave publica
    p = int(input("digite um numero primo:\n"))
    q = int(input("digite outro numero primo:\n"))
    e = int(input("digite um numero relativamente primo aos numeros sucessores dos anteriores\n"))
    n = p * q 
    saveLock(p, q, e, n)
    print("chave: %d" % n)

elif programa == 2:
    # Encriptar
    chaves = getLock() #puxa 
    p, q, e, n = chaves
    texto = input("digite seu texto:\n").upper()
    texto = criptografar(texto, letterShift)
    print(texto)
    

elif programa == 3:
    # Desencriptar
    if(int(input("Carregar chaves ou digitar?\n0-Digitar\n1-Carregar\n"))):
        #carregar
        p, q, d = getKey()
        n = p * q
    else:
        #digitar
        p = int(input('digite o p:'))
        q = int(input('digite o q:'))
        d = int(input('digite o d:'))
        n = p * q
    message = getMessage()
    print(desencriptar(message))

elif programa == 4:
    # Gerar d
    if(int(input("Carregar chaves ou digitar?\n0-Digitar\n1-Carregar\n"))):
        #carregar
        p, q, e, n = getLock()
    else:
        #digitar
        p = int(input('digite o p:'))
        q = int(input('digite o q:'))
        e = int(input('digite o e:'))
    #calcula o d
    d = modinv(e, (p - 1) * (q - 1))
    saveKey(p, q, d)
    print(d)