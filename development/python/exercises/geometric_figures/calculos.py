def get_figuras():
    figuras = ["Triángulo", "Triángulo rectángulo", "Rectángulo", "Hexágono", "Círculo", "Cubo", "Esfera", "Cilindro", "Prisma rectangular"]
    return figuras

def get_calculos():
    calculos = ["Perimetro", "Angulo", "Area", "Volumen", "Circunferencia"]
    return calculos

def calculate(num_figura, nombre_calculo):
    
    nombre_figura = get_figuras()[num_figura-1]
    print(f"\nFigura -> ({nombre_figura})\nCalcular -> ({nombre_calculo}) ")
    
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
        print(f"\n[RESULTADO] {nombre_calculo} de ({nombre_figura}) es {result}")

def get_area(num_figura):
    
    PI = 3.14159

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
        radio = float(input("Ingrese el radio del Circulo (Float): "))
        area = PI * (radio ** 2)
        return area

    elif num_figura == 6: # Cubo
        lado = float(input("Ingrese la longitud del lado del cubo (Float): "))
        area = 6 * (lado ** 2)
        return area

    elif num_figura == 7: # Esfera
        radio = float(input("Ingrese el radio de la Esfera (Float): "))
        
        area = 4 * PI * (radio ** 2)
        return area
    
    elif num_figura == 8: # Cilindro
        radio = float(input("Introduce el radio del cilindro (Float): "))
        altura = float(input("Introduce la altura del cilindro (Float): "))
        area = 2 * PI * radio * (radio + altura)
        return area
    
    elif num_figura == 9: # Prisma rectangular
        largo = float(input("Ingrese el largo del Prisma (Float): "))
        ancho = float(input("Ingrese el ancho del Prisma (Float): "))
        alto = float(input("Ingrese el alto del Prisma (Float): "))
        area = 2 * ((largo * ancho) + (largo * alto) + (ancho * alto))
        return area


def get_angulo(num_figura):

    if num_figura == 1: # Triángulo
        angulo1 = float(input("Ingrese el primer ángulo (Float): "))
        angulo2 = float(input("Ingrese el segundo ángulo (Float): "))
        tercer_angulo = 180 - (angulo1 + angulo2)

        return tercer_angulo
    
    elif num_figura == 2: # Triángulo rectángulo
        cateto1 = float(input("Introduce el valor del primer cateto (Float): "))
        hipotenusa = float(input("Introduce el valor de la hipotenusa (Float): "))

        return (cateto / hipotenusa) * 90
    
    elif num_figura == 3: # Rectangulo
        return "90° Cada uno"

    elif num_figura == 4: # Hexagono
        return "120° Cada uno"
    
    elif num_figura == 5: # Circulo
        return "360° en total"

   

def get_perimetro(num_figura):
    print("")

def get_volumen(num_figura):

    PI = 3.14159
    
    if num_figura == 6: # Cubo
        lado = float(input("Ingrese la longitud del lado del cubo (Float): "))
        volumen = lado ** 3
        return volumen

    elif num_figura == 7: # Esfera
        radio = float(input("Ingrese el radio de la esfera (Float): "))
        volumen = (4/3) * PI * (radio ** 3)
        return volumen
    
    elif num_figura == 8: # Cilindro
        radio = float(input("Introduce el radio del cilindro (Float): "))
        altura = float(input("Introduce la altura del cilindro (Float): "))
        volumen = PI * (radio**2) * altura
        return volumen
    
    elif num_figura == 9: # Prisma rectangular
        largo = float(input("Ingrese el largo del Prisma (Float): "))
        ancho = float(input("Ingrese el ancho del Prisma (Float): "))
        alto = float(input("Ingrese el alto del Prisma (Float): "))
        volumen = largo * ancho * alto
        return volumen

def get_circunferencia(num_figura):
    if num_figura == 5:
        radio = float(input("Ingrese el radio del Circulo (Float): "))
        circunferencia = 2 * PI * radio
        return circunferencia
        
