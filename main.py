from figuras_geometricas import Figuras_geometricas
from cuadrado import Cuadrado
from triangulo import Triangulo
from rectangulo import Rectangulo
from circulo import Circulo



while True :
    print("Menu")
    print("1.Cuadrado")
    print("2.triangulo")
    print("3.rectangulo")
    print("4.circulo")
    print("Salir")
    nombre = input("que figura desea usar : ")
    print("la figura seleccionada es :" , nombre )
    fg = Figuras_geometricas (nombre)
    fg.area()
#
    if nombre == "1" :
        lado = float(input("ingrese el lado del cuadrado:"))
        cu = Cuadrado(lado)
        print(f"El area del cuadrdao es :{cu.area()}")

    if nombre == "2" :
            base = float(input("ingrese la base del triangulo:"))
            altura = float(input("ingrese la altura del triangulo:"))
            tr = Triangulo(base , altura)
            print(f"El area del triangulo es : {tr.area()}")

    if nombre == "3" :
            base = float(input("ingrese la base del rectangulo :"))
            altura = float(input("ingrese la altura del rectangulo :"))
            re = Rectangulo(base,altura)
            print(f"El area del rectangulo es : {re.area()}")

    if nombre == "4" :
                    r = float(input("ingrese el radio del circulo :"))
                    cir = Circulo(r)
                    print(f"El área del circulo es: {cir.area()}")

    if nombre == "salir" :
            print("salir del programa :")
            break

