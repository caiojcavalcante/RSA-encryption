#include <math.h>

#define k 2

typedef unsigned long long int ulli;

char alphabet[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

ulli fast_pow(int base, int exp)
{
    ulli result = 1;
    for (;;)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        if (!exp)
            break;
        base *= base;
    }

    return result;
}
int mod_inv(int a, int m)
{
    for (int i = 1; i < m; i++)
        if ((a * i) % m == 1)
            return i;

    return -1;
}
int mdc(int a, int b)
{
    if (a == 0)
        return b;
    return mdc(b % a, a);
}
int is_relative_prime(int a, int b)
{
    return mdc(a, b) == 1;
}
int is_prime(int n)
{
    if (n <= 1)
        return 0;
    if (n <= 3)
        return 1;

    if (n % 2 == 0 || n % 3 == 0)
        return 0;

    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;

    return 1;
}
/*
    params:
        p: prime number
        q: prime number
*/
int create_key(int p, int q)
{
    if (!is_prime(p) || !is_prime(q))
    {
        printf("p and q must be prime numbers");
        return 0;
    }
    
    int n = p * q;

    int phi = (p - 1) * (q - 1);

    int e = 2;

    while (e++ < phi)
    {
        if (is_relative_prime(e, phi))
            break;
        e++;
    }

    int d = (1 + (k * phi)) / e;

    printf("Public key: (%d, %d)\n", e, n);

    printf("Private key: (%d, %d)\n", d, n);

    return 0;
}
void encrypt(char message[], int e, ulli n)
{
    //e = expoente
    //n = chave de codificação
    printf("Encrypted message:\n");
    int i = 0;
    ulli c;
    while (message[i] != '\0')
    {
        printf("%llu ", fast_pow(message[i], e) % n);
        i++;
    }
    printf("\n");
}
void decrypt(int message[], int d, int n, int letter_shift)
{
    //d = expoente
    //n = chave de codificação
    int i = 0;
    char c;
    printf("Decrypted message:\n");
    while (message[i] != -1)
    {
        c = alphabet[(fast_pow(message[i], d) % n) - letter_shift];

        printf("%c", c ? c : ' ');
        
        i++;
    }
    printf("\n");
}