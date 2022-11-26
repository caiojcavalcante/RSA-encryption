from array import *
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V',
    'W', 'X', 'Y', 'Z', ' ']

letterShift = 2

def fast_pow_mod(base, exp, mod):
    if exp < 0:
        return 1 / fast_pow_mod(base, -exp, mod)
    ans = 1
    while exp:
        if exp & 1:
            ans = (ans * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return ans

def criptografar(texto, shift):
    resultado = []
    for a in texto:
        #converte cada letra
        a = fast_pow_mod(alfabeto.index(a) + shift, e, n)
        resultado.append(a)
    saveMessage(resultado)
    return resultado

def desencriptar(array):
    resultado = ""
    for a in array:
        #converte cada letra
        a = fast_pow_mod(a, d, n)
        resultado += alfabeto[(a - letterShift) % len(alfabeto)]

    return resultado

def getMessageToDecrypt():
    f = open("message.txt", "r")
    content = f.read()
    content = content.split()
    content = [int(i) for i in content]

    f.close()
    return content

def getKey():
    f = open("key.txt", "r")
    content = f.read()
    content = content.split(',')
    content = [int(i) for i in content]
    f.close()
    return content

def getLock():
    f = open("lock.txt", "r")
    content = f.read()
    content = content.split(',')
    content = [int(i) for i in content]
    f.close()
    return content

def getMessageToEncrypt():
    f = open("text.txt", "r")
    content = f.read()

    f.close()
    return content

def saveMessage(text):
    f = open("message.txt", "w+")
    for i in range(len(text)):
        f.write("%s " % text[i])
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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def treatMessage(text):
    return text.replace(",", " ").replace("é", "e").replace("ê", "e").replace("á", "a").replace("à", "a").replace("ã", "a").replace("â", "a").replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("í", "i").replace("ú", "u").replace("ç", "c")

def modinv(a, b):
    #teorema chines do resto
    (r0, m0, n0) = a, 1, 0
    (r1, m1, n1) = b, 0, 1

    while(r0 % r1 > 0):
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        m0, m1 = m1, m0 - m1 * q
        n0, n1 = n1, n0 - n1 * q
    
    return m1



print(Fore.BLUE + "                     ⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿  \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟   \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀   \n                     ⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀     \n                     ⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀     \n")
print(Fore.BLUE + " .d8888b.          d8b          888                                      .d888 d8b             8888888b.   .d8888b.        d8888 \nd88P  Y88b         Y8P          888                                     d88P   Y8P             888   Y88b d88P  Y88b      d88888 \n888    888                      888                                     888                    888    888 Y88b.          d88P888 \n888        888d888 888 88888b.  888888 .d88b.   .d88b.  888d888 8888b.  888888 888  8888b.     888   d88P   Y888b.      d88P 888 \n888        888P    888 888  88b 888   d88  88b d88P 88b 888P        88b 888    888      88b    8888888P        Y88b.   d88P  888 \n888    888 888     888 888  888 888   888  888 888  888 888    .d888888 888    888 .d888888    888 T88b          888  d88P   888 \nY88b  d88P 888     888 888 d88P Y88b. Y88..88P Y88b 888 888    888  888 888    888 888  888    888  T88b  Y88b  d88P d8888888888 \n  Y8888P   888     888 88888P     Y888  Y88P     Y88888 888     Y888888 888    888  Y888888    888   T88b   Y8888P  d88P     888 \n                       888                          888                                                                          \n                       888                     Y8b d88P                                                                          \n                       888                       Y88P                                                                            \n")
#prompt para o usuario escolher a programação
programa = int(input("Digite\n1-Gerar chave publica\n2-Encriptar\n3-Desencriptar\n4-Gerar Decriptador\n"))

if programa == 1:
    # Gerar chave publica
    p = int(input("digite um numero primo:\n"))
    q = int(input("digite outro numero primo:\n"))
    if(int(input("Gerar e ou digitar?\n0-gerar\n1-digitar\n"))):
        e = int(input("digite o numero e:\n"))
    else:
        e = 3
        while(gcd(e, (p - 1)*(q - 1)) != 1):
            e += 2
        print("e = ", e)

    n = p * q 
    saveLock(p, q, e, n)
    print("chave: %d" % n)

elif programa == 2:
    # Encriptar
    chaves = getLock() #puxa 
    p, q, e, n = chaves

    if(int(input("Carregar ou digitar ?\n0-carregar\n1-digitar\n"))):
        mensagem = input("Digite a mensagem:\n")
    else:
        mensagem = getMessageToEncrypt()
        mensagem = treatMessage(mensagem)

    mensagem = criptografar(mensagem.upper(), letterShift)
    print(mensagem)
    
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
    message = getMessageToDecrypt()
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
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi) % phi
    saveKey(p, q, d)
    print(d)