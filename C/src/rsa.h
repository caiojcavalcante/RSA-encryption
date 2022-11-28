#define fast_pow_mod(a, b, c, d) mpz_powm(a, b, c, d)
#define LETTER_SHIFT 2

void criptografar()
{
    mpz_t n, e, aux; 
    mpz_init(n); mpz_init(e); mpz_init(aux);

    FILE* ptr = fopen("lock", "r");
    char s[1000], t[1000];

    fscanf(ptr, "%s", s);

    mpz_set_str(n, s, 10);

    fscanf(ptr, "%s", s);

    mpz_set_str(e, s, 10);

    ptr = fopen("msg", "r");

    fgets(s, 1000, ptr);

    fclose(ptr);

    ptr = fopen("cypher", "w");
    
    for(int i = 0; i < strlen(s); i++)
    {
        if(s[i] > 'Z' || s[i] < 'A')
            s[i] = 'Z' + 1;
        s[i] += LETTER_SHIFT - 'A';
        mpz_set_ui(aux, s[i]);
        fast_pow_mod(aux, aux, e, n);
        gmp_printf("%Zd ", aux);
        mpz_get_str(t, 10, aux);
        fprintf(ptr, "%s ", t);
    }
    printf("\n");
    fclose(ptr);
}

void descriptografar()
{
    char c;
    mpz_t n, d, aux;

    mpz_init(n);mpz_init(d);mpz_init(aux);

    FILE* ptr = fopen("key", "r");

    char s[1000];

    fscanf(ptr, "%s", s);
    printf("%s\n", s);

    mpz_set_str(n, s, 10);

    fscanf(ptr, "%s", s);

    mpz_set_str(d, s, 10);

    fclose(ptr);

    ptr = fopen("cypher", "r");

    while(1)
    {
        if(fscanf(ptr, "%s", s) == EOF)
            break;

        mpz_set_str(aux, s, 10);

        fast_pow_mod(aux, aux, d, n);
        c = mpz_get_ui(aux) - LETTER_SHIFT + 'A';
        if(c > 'Z' || c < 'A')
            c = ' ';
        printf("%c", c);
    }
    printf("\n");
    fclose(ptr);
}

void gerar_chaves()
{

    int opcao;
    mpz_t p, q, n, phi, e, d, aux0, aux1;
    mpz_init(p); mpz_init(q); mpz_init(n); mpz_init(phi); mpz_init(e); mpz_init(d); mpz_init(aux0), mpz_init(aux1);

    FILE* ptr;
    ptr = fopen("chaves", "r");
    if(ptr == NULL)
    {
        printf("Erro ao abrir o arquivo\n");
        return;
    }

    char s[1000];

    fscanf(ptr, "%s", s);

    mpz_set_str(p, s, 10);
    gmp_printf("p: %Zd\n", p);

    fscanf(ptr, "%s", s);

    mpz_set_str(q, s, 10);
    gmp_printf("q: %Zd\n", q);

    mpz_mul(n, p, q);

    mpz_sub_ui(aux0, p, 1);
    mpz_sub_ui(aux1, q, 1);

    mpz_mul(phi, aux0, aux1);

    if(fscanf(ptr, "%s", s) != EOF)
        mpz_set_str(e, s, 10);
    else
    {
        printf("gerando e\n");
        mpz_set_ui(e, 3);
        while(1)
        {
            mpz_gcd(aux0, e, phi);
            if(mpz_cmp_ui(aux0, 1) == 0)
                break;
            mpz_add_ui(e, e, 2);
        }
    }
    fclose(ptr);

    mpz_invert(d, e, phi);
    
    ptr = fopen("chaves", "w");

    fprintf(ptr, "%s\n", mpz_get_str(s, 10, p));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, q));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, e));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, d));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, n));
    fclose(ptr);

    ptr = fopen("lock", "w");
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, n));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, e));
    fclose(ptr);

    ptr = fopen("key", "w");
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, n));
    fprintf(ptr, "%s\n", mpz_get_str(s, 10, d));
    fclose(ptr);

    gmp_printf("chave publica: (%Zd, %Zd)\n", e, n);
    gmp_printf("chave privada: (%Zd, %Zd)\n", d, n);
}