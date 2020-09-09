
def conocerPalindromo(palabra):
    respuesta=False;
    if str(palabra) == str(palabra)[::-1]:
        print("La palabra ",palabra ," es palindroma")
        respuesta=True;
    else:
        print("La palabra ",palabra ," no es palindroma")

    return respuesta;
def main():
    print("Binevenido, con este programa podrá concocer si una palabra es palíndroma");
    palabra="";
    conocerPalindromo(palabra)

if __name__ == '__main__':
    main()