from typing import List


def conocerMultiplos(a,b,x):

    print("")
    print("Los múltiplos son:")
    list=[]
    for m in range(a, b+1):
        if m % x == 0:
            print(m)
            list.append(m);
    return list;
def main():
    print("Binevenido, con este programa podrá concocer múltiplos");
    a=-2;
    b=-2;
    x=0;
    while a >= b or (x<a or x>b):
        print("")
        a = int(input("Introduzca el primer número del rango, el a de [a,b]: "));
        b = int(input("Introduzca el segundo número del rango, el b de [a,b]: "));
        x = int(input("Introduzca el número x para los multiplos que desea buscar en el rango  "));
        if a >= b:
            print("El valor de a es mayor o igual al de b, vuelva a digitar los datos");
        else:
         print("Se ha registrado el rango");

        if x<a:
            print("El valor de x debe estar entre a y b, vuelva a digitar los datos");
        else:
            print("Se ha registrado X");

        if x>b:
            print("El valor de x debe estar entre a y b, vuelva a digitar los datos");

        if a<0:
            print("El valor de a debe ser mayor a cero, digitelo nuevamente");

    conocerMultiplos(a,b,x)

if __name__ == '__main__':
    main()
