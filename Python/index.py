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
        return 1 / fast_pow_mod(base, -exp)
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


print(Fore.BLUE + "                     ⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀     \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀    \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿  \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟   \n                     ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀   \n                     ⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n                     ⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀     \n                     ⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀     \n")
print(Fore.BLUE + " .d8888b.          d8b          888                                      .d888 d8b             8888888b.   .d8888b.        d8888 \nd88P  Y88b         Y8P          888                                     d88P   Y8P             888   Y88b d88P  Y88b      d88888 \n888    888                      888                                     888                    888    888 Y88b.          d88P888 \n888        888d888 888 88888b.  888888 .d88b.   .d88b.  888d888 8888b.  888888 888  8888b.     888   d88P   Y888b.      d88P 888 \n888        888P    888 888  88b 888   d88  88b d88P 88b 888P        88b 888    888      88b    8888888P        Y88b.   d88P  888 \n888    888 888     888 888  888 888   888  888 888  888 888    .d888888 888    888 .d888888    888 T88b          888  d88P   888 \nY88b  d88P 888     888 888 d88P Y88b. Y88..88P Y88b 888 888    888  888 888    888 888  888    888  T88b  Y88b  d88P d8888888888 \n  Y8888P   888     888 88888P     Y888  Y88P     Y88888 888     Y888888 888    888  Y888888    888   T88b   Y8888P  d88P     888 \n                       888                          888                                                                          \n                       888                     Y8b d88P                                                                          \n                       888                       Y88P                                                                            \n")
#prompt para o usuario escolher a programação
programa = int(input("Digite\n1-Gerar chave publica\n2-Encriptar\n3-Desencriptar\n4-Gerar Decriptador\n"))

if programa == 1:
    # Gerar chave publica
    p = int(input("digite um numero primo:\n"))
    q = int(input("digite outro numero primo:\n"))
    e = int(input("digite um numero relativamente primo ao produto dos numeros sucessores de p e q:\n"))
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
        p = int(input('     digite o p:'))
        q = int(input('     digite o q:'))
        d = int(input('     digite o d:'))
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
        p = int(input('     digite o p:'))
        q = int(input('     digite o q:'))
        e = int(input('     digite o e:'))
    #calcula o d
    d = modinv(e, (p - 1) * (q - 1))
    saveKey(p, q, d)
    print(d)