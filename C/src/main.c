#include <stdio.h>
#include <string.h>
#include <gmp.h>
#include "rsa.h"

int main()
{
    int opcao;
    printf("1- Gerar chaves\n2 - Criptografar\n3 - Descriptografar\n");
    scanf("%d", &opcao);
    switch(opcao)
    {
        case 1:
            gerar_chaves();
            break;
        case 2:
            criptografar();
            break;
        case 3:
            descriptografar();
            break;
    }
}