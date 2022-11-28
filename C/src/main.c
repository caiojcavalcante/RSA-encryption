#include <stdio.h>
#include <string.h>
#include <gmp.h>
#include "rsa.h"

int main()
{
    int opcao;
    printf("1 - Criptografar\n2 - Descriptografar\n3 - Gerar chaves\n");
    scanf("%d", &opcao);
    switch(opcao)
    {
        case 1:
            criptografar();
            break;
        case 2:
            descriptografar();
            break;
        case 3:
            gerar_chaves();
            break;
    }
}