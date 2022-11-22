/*

    RSA Cryptography Library
    by:  Caio Cavalcante

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "rsa.h"

#define __str_len__ 1000
#define __letter_shift__ 2

int main()
{
    int state;
    //state selector
    printf("RSA Cryptography Library\nChoose an option:\n1 - Encrypt\n2 - Decrypt\n3 - Generate keys\n");
    scanf("%d", &state);

    switch (state)
    {
        case 1:
        {
            //encrypt
            char message[__str_len__];
            int e, n, len;
    
            printf("Enter the message to encrypt: ");
            scanf(" %[^\n]", message);

            len = strlen(message);

            for(int i = 0; i < len; i++)
                for(int j = 0; j < 28; j++)
                    if(message[i] == alphabet[j])
                    {
                        message[i] = j + __letter_shift__;
                        break;
                    }

            for(int i = 0; i < len; i++)
                printf("%d ", message[i]);

            printf("\n");
            printf("Enter the public key (e, n): ");
            scanf("%d %d", &e, &n);
            encrypt(message, e, n);
            break;
        }
        case 2:
        {
            //decrypt
            int d, n, message[__str_len__];

            printf("Enter the code to decrypt: ");
            for(int i = 0;i < __str_len__;i++)
                if(scanf("%d", &message[i]) == EOF || message[i] == -1)
                {
                    message[i] = -1;
                    break;
                }

            printf("Enter the private key (d, n): ");
            scanf("%d %d", &d, &n);
            decrypt(message, d, n, __letter_shift__);
            break;
        }
        case 3:
        {
            //generate keys
            int p, q;
            printf("Enter two prime numbers: ");
            scanf("%d %d", &p, &q);
            create_key(p, q);
            break;
        }
        default:
        {
            printf("Invalid option\n");
            break;
        }
    }
    return 0;
}
