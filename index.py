from array import *
# from locale import resetlocale
# from tkinter.messagebox import RETRY


alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V',
    'W', 'X', 'Y', 'Z', ' ']

letterShift = 2

def criptografar(texto):
    resultado = []
    for i in range(len(texto)):
        b = alfabeto.index(texto[i]) + letterShift
        a = (b ** e) % n
        resultado.append(a)
    f = open("message.txt", "w+")
    f.write("%s" % resultado)
    f.close()
    return resultado

def desencriptar(array):
    resultado = ""
    for a in array:
        a = (a ** d) % n
        resultado += alfabeto[a - letterShift]
    return resultado

def getMessage():
    f = open("message.txt", "r")
    content = f.read()[1:]
    content = content[:len(content) - 1].split(',')
    for i in range(len(content)):
        content[i] = int(content[i])
    f.close()
    return content

def saveMessage(text):
    f = open("message.txt", "w+")
    f.write("%s" % text)
    print("salvo :)")
    f.close()

def getKeys():
    f = open("key.txt", "r")
    content = f.read()
    content = content.split(',')
    for i in range(len(content)):
        content[i] = int(content[i])
    f.close()
    # zip([p, q, e, n], content)
    return content

def saveKeys(p, q, l, n):
    resultado = str(p) + ',' + str(q) + ',' + str(l) + ',' + str(n)
    f = open("key.txt", "w+")
    f.write("%s" % resultado)
    print("salvo :)")
    f.close()

def keysCompatible(p, q, l, n):
    if((l % 2) == 0):
        print("Este numero nao pode ser par")
        return False
    return True

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

programa = int(input("Digite \n1-Gerar chave publica\n2-Encriptar\n3-Desencriptar\n"))

if programa == 1:
    # Gerar chave publica
    p = int(input("digite um numero primo:\n"))
    q = int(input("digite outro numero primo:\n"))
    l = int(input("digite um numero relativamente primo aos numeros sucessores dos anteriores:\nsugestão: 3\n"))
    n = p * q
    if(keysCompatible(p, q, l, n)):
        saveKeys(p, q, l, n)
        print("chave: %d" % n)
    else:
        print("chaves nao compativeis")


elif programa == 2:
    # Encriptar
    chaves = getKeys()
    p, q, e, n = chaves #isso funciona igual a
    texto = input("digite seu texto:\n").upper()
    texto = criptografar(texto)
    print(texto)
    

elif programa == 3:
    # Desencriptar
    if(int(input("Carregar chaves ou digitar?\n0-Digitar\n1-Carregar\n"))):
        chaves = getKeys()
        p, q, e, n = chaves
    else:
        p = int(input('digite o p:'))
        q = int(input('digite o q:'))
        e = int(input('digite o e:'))
        n = p * q
    # d = modinv(e, (p - 1) * (q - 1))
    d = pow(e, -1, (p - 1) * (q - 1))
    message = getMessage()
    print(desencriptar(message))
