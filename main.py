from figurasgeometricas import FigurasGeometricas
from cuadrado import Cuadrado
from triangulo import Triangulo
from rectangulo import Rectangulo
from circulo import Circulo
from cilindro import Cilindro
from paralelograma import Paralelogramo
from rombo import Rombo
from pentagono import Pentagono

while True :
    print("Menu")
    print("1.Cuadrado")
    print("2.triangulo")
    print("3.rectangulo")
    print("4.circulo")
    print("5.cilindro")
    print("6.paralelogramo")
    print("7.rombo")
    print("8.pentagono")
    print("9.salir")
    
    opcion = input("Ingresa la opcion deseada :")
    print("La opcion selesccionada es :", opcion)

    if opcion == "1" :
        lado = float(input("ingrese el valor :"))
        cu = Cuadrado(lado)
        print("el area del cuadardo es:", cu.area())
    
    elif opcion == "2" :
        base = float(input("ingresa la base del triangulo :"))
        altura = float(input("ingresa la altura del triangulo :"))
        tr  = Triangulo(base,altura)
        print("el area del triangulo es :", tr.area())
    
    elif opcion == "3":
        base = float(input("ingresa la base del rectangulo :"))
        altura = float(input("ingresa la altura del rectangulo :"))
        rec = Rectangulo(base,altura)
        print("El area del rectangulo es :" , rec.area())
    
    elif opcion == "4" :
        radio = float(input("Ingresa el radio del círculo: "))
        cir = Circulo(radio)
        print("el area del circulo es :" , cir.area())
        
    elif opcion == "5" :
        radio = float(input("Ingresa el radio del cílindro : "))
        altura = float(input("ingresa la altura del cilindro :"))
        cil = Cilindro(radio,altura)
        print("el area del cilindro es : ", cil.area())
    
    elif opcion == "6":
        base = float(input("Introduce la base del paralelogramo: "))
        altura = float(input("Introduce la altura del paralelogramo: "))
        par = Paralelogramo(base,altura)
        print("el area del paralelogramo :" , par.area())
        
    elif opcion == "7" :
        diagonal_mayor =  float(input("introduce el diagonal mayor"))
        diagonal_menor = float(input("introduce el diagonal menor"))
        rom = Rombo(diagonal_mayor,diagonal_menor)
        print("el area del rombo es :", rom.area())
        
    elif opcion == "8":
        perimetro = float(input("ingresa el valor del parametro"))
        apotema = float(input("ingresa el valor del apotema"))
        lado = float(input("Ingresa el  valor del lado"))
        pen = Pentagono(perimetro,apotema,lado)
        print("el area del pentagono es :", pen.area())
        
    elif opcion == "9":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta nuevamente.")