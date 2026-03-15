def get_figuras():
    figuras = ["Triángulo", "Triángulo rectángulo", "Rectángulo", "Hexágono", "Círculo", "Cubo", "Esfera", "Cilindro", "Prisma rectangular"]
    return figuras

def get_calculos():
    calculos = ["Perimetro", "Angulo", "Area", "Volumen", "Circunferencia"]
    return calculos

def calculate(num_figura, nombre_calculo):
    
    nombre_figura = get_figuras()[num_figura-1]
    print(f"\nCalcular -> {nombre_calculo} de la figura: ({nombre_figura}) <-")
    
    num_calculo = get_calculos().index(nombre_calculo)
    result = ""
    if num_calculo == 0:
        result = get_perimetro(num_figura)
    if num_calculo == 1:
        result = get_angulo(num_figura)
    if num_calculo == 2:
        result = get_area(num_figura)
    if num_calculo == 3:
        result = get_volumen(num_figura)
    if num_calculo == 4:
        result = get_circunferencia(num_figura)
    
    
    if result == None:
        print("Aun no implementado =)")
    else:
        result = str(f"{result:.1f}")
        print(f"\n[RESULTADO] El {nombre_calculo} de su ({nombre_figura}) es {result}")

def get_area(num_figura):
    
    pi = 3.14159

    if num_figura == 1 or num_figura == 2: # Triángulo / Triángulo rectángulo
        base = float(input("Ingrese la base (Float): "))
        altura = float(input("Ingrese la altura (Float): "))
        area = (base * altura) / 2
        return area
    
    elif num_figura == 3: # Rectangulo
        base = float(input("Ingrese la base (Float): "))
        altura = float(input("Ingrese la altura (Float): "))
        area = base * altura
        return area

    elif num_figura == 4: # Hexagono
        lado = float(input("Ingrese la longitud del lado (Float): "))
        raiz_3 = 3 ** 0.5
        area = ((3 * raiz_3) / 2) * (lado ** 2)
        return area
    
    elif num_figura == 5: # Circulo
        radio = float(input("Ingrese el radio del Circulo (Float: )"))
        area = pi * (radio ** 2)
        return area

    elif num_figura == 6: # Cubo
        lado = float(input("Ingrese la longitud del lado del cubo (Float): "))
        area = 6 * (lado ** 2)
        return area

    elif num_figura == 7: # Esfera
        radio = float(input("Ingrese el radio de la Esfera (Float): "))
        
        area = 4 * pi * (radio ** 2)
        return area
    
    elif num_figura == 8: # Cilindro
        radio = float(input("Introduce el radio del cilindro (Float): "))
        altura = float(input("Introduce la altura del cilindro (Float): "))
        area = 2 * pi * radio * (radio + altura)
        return area
    
    if num_figura == 9: # Prisma rectangular
        largo = float(input("Ingrese el largo del Prima (Float): "))
        ancho = float(input("Ingrese el ancho del Prima (Float): "))
        alto = float(input("Ingrese el alto del Prima (Float): "))
        area = 2 * ((largo * ancho) + (largo * alto) + (ancho * alto))
        return area


def get_angulo(num_figura):
    print("")

def get_perimetro(num_figura):
    print("")

def get_volumen(num_figura):
    print("")

def get_circunferencia(num_figura):
    print("")


    
    # if num_fig == 1: # Triángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 2:# Hexágono
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 3:# Rectángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 4:# Círculo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 5:# Triángulo rectángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])  
    # elif num_fig == 6:# Cubo
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 7:# Esfera
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 8:# Cilindro
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 9:# Prisma rectangular
    #     print(calculos[2])
    #     print(calculos[3])