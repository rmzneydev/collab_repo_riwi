
print("###### Ejercicios Python Intermedio ######")
print("### 1. Heladería: sabor más pedido ###")
print("### 2. Gimnasio: acceso por edad ###")
print("### 3. Cafetería: total de una compra sencilla ###")
print("### 4. Cine: entrada según edad ###")
print("### 5. Tienda de mascotas: alimento por tipo de animal ###")
print("### 6. Parqueadero: cobro por horas ###")
print("### 7. Peluquería: turno del día ###")
print("### 8. Tienda deportiva: contar productos caros ###")
print("### 9. Spa: servicio disponible ###")
print("### 10. Academia de baile: asistencia ###")
print("### 11. Heladería: factura de varios clientes ###")
print("### 12. Gimnasio: promedio de rendimiento semanal ###")
print("### 13. Cafetería: descuento por consumo ###")
print("### 14. Cine: control de sala ###")
print("### 15. Parqueadero: control de vehículos ###")
print("### 16. Tienda de mascotas: ventas por categoría ###")
print("### 17. Peluquería: agenda de atención ###")
print("### 18. Centro de idiomas: evaluación de estudiantes ###")
print("### 19. Tienda de ropa deportiva: inventario crítico ###")
print("### 20. Club recreativo: control de membresías ###")

salir = False

while not salir:
    valid_op = False
    num_ejercicio = 0
    while not valid_op:
        try:
            opcion = input(f"\nIngrese: numero de ejercicio o 'salir' para finalizar: ")
            if opcion.lower() != "salir":
                num_ejercicio = int(opcion)
                if num_ejercicio > 20 or num_ejercicio < 1:
                    print(f"No existe el ejercicio numero {num_ejercicio}")
                else:
                    valid_op = True
            else:
                valid_op = True
                salir = True
        except ValueError:
            print("No ingreso un numero valido!")
    print("\n")
    if num_ejercicio == 1:

        print("### 1. Heladería: sabor más pedido ###")
        num_pedidos = 5

        count_vainilla = 0
        count_chocolate = 0
        count_fresa = 0
            
        salir = False
        cliente = 0
        while not salir:
            cliente+=1
            print("cliente #",cliente)
            for pedido in range(num_pedidos):
                print("Pedido #",pedido+1)
                print("Sabores disponibles:\n1. Vainilla \n2. Chocolate \n3. Fresa")
                sabor = input("Ingrese numero de sabor (1-3): ")
                if sabor == "1":
                    count_vainilla+=1
                elif sabor == "2":
                    count_chocolate+=1
                elif sabor == "3":
                    count_fresa+=1
                    
            salir = input("Presione enter para otro cliente / ingrese (x) para salir: ")
            salir = bool(salir.strip())
            

        print("\nEn total se pidieron: ")
        print("Vainilla:", count_vainilla)
        print("Chocolate:", count_chocolate)
        print("Fresa:", count_fresa)

    if num_ejercicio == 2:
        print("### 2. Gimnasio: acceso por edad ###")
        edad = int(input("Ingrese edad: "))

        if edad <13:
            print("No puede ingresar")
        elif edad >=13 and edad <=17:
            print("Clase juvenil")
        elif edad >=18 and edad <=59:
            print("Clase general")
        else:
            print("Clase senior")
            
    if num_ejercicio == 3:
        print("### 3. Cafetería: total de una compra sencilla ###")
        cafe = 4000
        te = 3500
        jugo = 5000

        print("Cafetería\nBebidas disponibles:\n- Café\n- Té\n- Jugo")
        bebida = input("Que bebida quiere: ")
        unidades = int(input("Ingre las unidades a comprar: "))

        total = 0
        bebida = bebida.lower()

        if bebida == "cafe":
            total = cafe * unidades
        elif bebida == "te":
            total = te * unidades
        elif bebida == "jugo":
            total = te * unidades
            
        print("Total a pagar: ", total)

    if num_ejercicio == 4:
            
        print("### 4. Cine: entrada según edad ###")
        edad = int(input("Ingrese edad: "))

        if edad <12:
            print("Debe pagar: 8000")
        elif edad >=12 and edad <=59:
            print("Debe pagar: 12000")
        elif edad >60:
            print("Debe pagar: 9000")

    if num_ejercicio == 5:
        print("### 5. Tienda de mascotas: alimento por tipo de animal ###")
        mascota = input("Ingrese el tipo de masconta :\n> perro \n> gato \n> conejo\n:")
        mascota = mascota.lower()
        if mascota == "perro":
            print("Alimento recomendado: Carne de pollo")
        elif mascota == "gato":
            print("Alimento recomendado: Pezcado")
        elif mascota == "conejo":
            print("Alimento recomendado: Zanahoria")

    if num_ejercicio == 6:
        print("### 6. Parqueadero: cobro por horas ###")
        num_horas = int(input("Parqueadero\nIngrese numero de horas de parqueo: "))

        hora_base = 5000
        hora_adicional = 3000

        total =0

        if num_horas == 1:
            total = hora_base
        elif num_horas > 1:
            num_horas -= 1
            total = hora_base + (num_horas*hora_adicional)
            
        print(f"Total a pagar: {total}")

    if num_ejercicio == 7:
        print("### 7. Peluquería: turno del día ###")

        hora_de_llegada = int(input("Peluquería\nIngrese hora de llegada: "))

        if hora_de_llegada >= 6 and hora_de_llegada <=11:
            print("mañana")
        elif hora_de_llegada >= 12 and hora_de_llegada <=17:
            print("tarde")
        elif hora_de_llegada >= 18 and hora_de_llegada <=22:
            print("noche")
        else:
            print("fuera de horario")

    if num_ejercicio == 8:
        print("### 8. Tienda deportiva: contar productos caros ###")
        num_productos = 6

        contador = 0
        for i in range(num_productos):
            precio = int(input(f"Ingrese el precio del producto #{i+1}: "))
            if precio > 100000:
                contador +=1

        print(f"En total ({contador}) productos cuestan más de 100000.")

    if num_ejercicio == 9:
        print("### 9. Spa: servicio disponible ###")
        servicios = ["masaje", "facial", "manicure"]
        servicio = input("Spa\nIngrese el nombre del servicio desea: ")

        if servicio.lower() in servicios:
            print(f"El servico {servicio} si existe")
        else:
            print(f"El servico {servicio} no existe")

    if num_ejercicio == 10:
        print("### 10. Academia de baile: asistencia ###")
        cant_clases = int(input("Academia de baile: asistencia\nIngrese cantidad de clases: "))

        if cant_clases <5:
            print("Asistencia baja")
        if cant_clases >=5 and cant_clases <=8:
            print("Asistencia media")
        else:
            print("Asistencia alta")

    if num_ejercicio == 11:
        print("### 11. Heladería: factura de varios clientes ###")
        salir = False

        cono = 3000
        vaso = 4000
        banana_split = 9000

        num_clientes = 0
        total = 0

        conos_vendidos = 0
        vaso_vendidos = 0
        banana_split_vendidos = 0
        mas_vendido = ""

        while not salir:
            num_clientes+=1
            print(f"Cliente # {num_clientes}")
            print("Productos disponibles:\n1. cono \n2. vaso \n3. banana split")
            producto = input("Ingrese numero de producto (1-3): ")
            cantidad = int(input("Ingrese cantidad : "))
            
            if producto == "1":
                total = cono * cantidad
                conos_vendidos += cantidad
            elif producto == "2":
                total = vaso * cantidad
                vaso_vendidos += cantidad
            elif producto == "3":
                total = banana_split * cantidad
                banana_split_vendidos += cantidad
            
            salir = input("Presione enter para otro cliente / ingrese (x) para salir: ")
            salir = bool(salir.strip())
            
            
        if conos_vendidos > vaso_vendidos and conos_vendidos > banana_split_vendidos:
            mas_vendido = "Conos"
        elif vaso_vendidos > conos_vendidos and vaso_vendidos > banana_split_vendidos:
            mas_vendido = "Vaso"
        elif banana_split_vendidos > conos_vendidos and banana_split_vendidos > vaso_vendidos:
            mas_vendido = "Banana split"

        print(f"Total vendido: {total}")
        print(f"Clientes atendidos: {num_clientes}")
        print(f"Producto mas  vendido: {mas_vendido}")

    if num_ejercicio == 12:
        print("### 12. Gimnasio: promedio de rendimiento semanal ###")

        num_personas = 5

        cat_bajo = 0
        cat_medio = 0
        cat_alto = 0


        for i in range(num_personas):
            print(f"Persona #{i+1}")
            nombre = input("Ingrese nombre: ")
            dias = int(input("Numero de dias asistidos: "))
            min_promedio = int(input("Minutos promedio: "))
            if dias < 3:
                cat_bajo += 1
            if dias >= 3 and dias <=4:
                cat_medio += 1
            if dias >= 5:
                cat_alto += 1

        print(f"Total personas en categoria:")
        print(f"bajo compromiso {cat_bajo}")
        print(f"compromiso medio {cat_medio}")
        print(f"compromiso alto {cat_alto}")

    if num_ejercicio == 13:
        print("### 13. Cafetería: descuento por consumo ###")
        cafe = 4000
        capuchino = 7000
        pastel = 6000

        total_acumulado = 0

        salir = False

        pedido = 1
        while not salir:
            total_cliente = 0
            print(f"\n(Ingresando el Pedido #{pedido})")
            
            producto = ""
            while producto != "4":
                print("Productos:\n1. Café \n2. Capuchino\n3. Pastel")
                producto = input("Ingrese numero de producto (1-3) o (4 para completar pedido): ")
                
                if producto.lower() == "salir":
                    salir = True
                    producto = "4"
                elif producto.lower() == "1":
                    total_cliente += cafe
                elif producto.lower() == "2":
                    total_cliente += capuchino 
                elif producto.lower() == "3":
                    total_cliente += pastel
                elif producto.lower() != "4":
                    print("No ingreso un numero valido")
                
            
            if total_cliente > 20000:
                total_cliente = total_cliente - (total_cliente*0.10)
            
            print(f"Total cliente: {total_cliente}")

            total_acumulado += total_cliente
            pedido+=1

        print(f"Total acumulado: {total_acumulado}")

    if num_ejercicio == 14:
        print("### 14. Cine: control de sala ###")
        capacidad = int(input("Ingrese capacidad de la sala: "))

        niños = 0
        adultos = 0
        adulto_mayor = 0

        salir = False
        persona = 0
        while not salir:
            persona+=1
            print(f"Persona #{persona}")
            edad = int(input("Ingrese la edad: "))
            if edad <12:
                niños+=1
            elif edad >=18 and edad <=59:
                adultos+=1
            elif edad >=60:
                adulto_mayor+=1
            
            salir = input("Presione enter para ingresar otra persona / ingrese (x) para salir: ")
            salir = bool(salir.strip())

        sala_llena = "NO"

        if persona >= capacidad:
            sala_llena = "SI"

        print(f"Personas ingresadas {persona}")
        print(f"Niños: {niños}")
        print(f"Adultos: {adultos}")
        print(f"Adultos mayores: {adulto_mayor}")
        print(f"Se lleno la sala {sala_llena}")

    if num_ejercicio == 15:
        print("### 15. Parqueadero: control de vehículos ###")
        num_vehiculos = 8
        tf_carro = 4000
        tf_moto = 2000

        pago_mas = ""
        pago_mas_value = 0

        total_carros = 0
        total_motos = 0

        total = 0

        for i in range(num_vehiculos):
            print(f"Registrando vehículo #{i+1}")
            placa = input("Ingrese placa: ")
            tipo = input("Ingrese tipo Carro/Moto: ")
            horas = int(input("Ingrese horas de parqueo: "))

            total_vehiculo = 0

            if tipo.lower() == "carro":
                total_carros+=1
                total_vehiculo = tf_carro * horas
            if tipo.lower() == "moto":
                total_motos+=1
                total_vehiculo = tf_moto * horas

            total += total_vehiculo

            if total_vehiculo > pago_mas_value:
                pago_mas = placa
                pago_mas_value = total_vehiculo

        print(f"Total recaudado: {total}")
        print(f"Carros que ingresaron: {total_carros}")
        print(f"Motos que ingresaron: {total_motos}")
        print(f"Vehículo que pagó más: {pago_mas}")

    if num_ejercicio == 16:
        print("### 16. Tienda de mascotas: ventas por categoría ###")

        num_ventas = 10

        max_cat = ""
        total_alimento = 0
        total_juguete = 0
        total_accesorio = 0

        for venta in range(num_ventas):
            print(f"Venta #{venta+1}")
            categoria = input("Categorias:\n1. alimento \n2. juguete \n3. accesorio\nDigite el numero de categoria:")
            valor_compra = float(input("Ingrese valor de compra: "))
            
            if categoria == "1":
                total_alimento+=valor_compra
            elif categoria == "2":
                total_juguete+=valor_compra
            elif categoria == "3":
                total_accesorio+=valor_compra

        if total_alimento > total_juguete and total_juguete >= total_accesorio:
            max_cat = "Alimento"
        if total_juguete > total_alimento and total_alimento >= total_accesorio:
            max_cat = "Juguete"
        if total_accesorio > total_alimento and total_alimento >= total_juguete:
            max_cat = "Accesorio"
            
        print(f"Total vendido alimento: {total_alimento}")
        print(f"Total vendido juguete: {total_juguete}")
        print(f"Total vendido accesorio: {total_accesorio}")
        print(f"Categoría generó más dinero: {max_cat}")

    if num_ejercicio == 17:
        print("### 17. Peluquería: agenda de atención ###")

        clientes = 7
        total_dia = 0
        max_servicio = ""
        corte = 0
        cepillado = 0
        tintura = 0

        for cliente in range(clientes):
            print(f"Cliente #{cliente+1}")
            nombre = input("Ingrese nombre: ")
            servicio = input("servicios:\n1. Corte\n2. Cepillado\n3. Tintura\nDigite el numero de servicio:")
            valor_pagado = float(input("Ingrese valor pagado: "))
            
            if servicio == "1":
                corte+=1
            elif servicio == "2":
                cepillado+=1
            elif servicio == "3":
                tintura+=1
            
            total_dia+=valor_pagado
            
        if corte > cepillado and cepillado >= tintura:
            max_servicio = "corte"
        if cepillado > corte and corte >= tintura:
            max_servicio = "cepillado"
        if tintura > cepillado and cepillado >= corte:
            max_servicio = "tintura"

        print(f"Total dia: {total_dia}")    
        print("Numero de clientes por servicio: ")
        print(f"Corte: {corte}")
        print(f"Cepillado: {cepillado}")
        print(f"Tintura: {tintura}")
        print(f"Servicio mas solicitado: {max_servicio}")

    if num_ejercicio == 18:
        print("### 18. Centro de idiomas: evaluación de estudiantes ###")

        general_prom = 0

        mejor_estudiante = ["", 0]

        nivel_bajo = 0
        nivel_medio = 0
        nivel_alto = 0

        num_estudiante = 0
        salir = False

        while not salir:
            num_estudiante +=1
            print(f"Estudiante # {num_estudiante}")
            nombre = input("Ingrese nombre: ")
            nota_speaking = int(input("Ingrese nota speaking: "))
            nota_lisening = int(input("Ingrese nota lisening: "))
            nota_reading = int(input("Ingrese nota reading: "))
            
            prom_estudiante = (nota_speaking + nota_lisening + nota_reading) / 3
            
            if prom_estudiante < 60:
                nivel_bajo += 1
            elif prom_estudiante >= 60 and prom_estudiante <=79:
                nivel_medio += 1
            elif prom_estudiante > 80:
                nivel_alto += 1
                
            if prom_estudiante > mejor_estudiante[1]:
                mejor_estudiante[0] = nombre
                mejor_estudiante[1] = prom_estudiante
            
            general_prom += prom_estudiante
            
            salir = input("Presione enter para agregar otro estudiante / ingrese (x) para salir ")
            salir = bool(salir.strip())
            
        general_prom = (general_prom / num_estudiante)

        print(f"\nPromedio general del grupo {general_prom}")
        print(f"Mejor estudiante {mejor_estudiante[0]}")
        print("Estudiantes en nivel: ")
        print(f"Bajo: {nivel_bajo}")
        print(f"Medio: {nivel_medio}")
        print(f"Alto: {nivel_alto}")

    if num_ejercicio == 19:
        print("### 19. Tienda de ropa deportiva: inventario crítico ###")
        num_productos = 10

        agotados = 0
        stock_bajo = 0
        stock_normal = 0


        for producto in range(num_productos):
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad disponible: "))
            if cantidad == 0:
                agotados += 1
            if cantidad >= 1 and cantidad <=5:
                stock_bajo += 1
            if cantidad >= 6:
                stock_normal += 1
                

        print(f"Agotados: {agotados}")
        print(f"Stock bajo: {stock_bajo}")
        print(f"Stock normal: {stock_normal}")

    if num_ejercicio == 20:
        print("### 20. Club recreativo: control de membresías ###")

        basic = 0
        premium = 0
        familiar = 0

        total = 0

        plan_max = ""

        add_persona = True

        while add_persona:
            nombre = input("Ingrese nombre: ")
            edad = int(input("Ingrese edad: "))
            plan = input("Planes:\nbasico\npremium\nfamiliar\nIngrese tipo de plan: ")
            
            if edad < 18:
                print("Registro juvenil")
            elif edad >= 60:
                print("beneficio senior")
                
            if plan == "basico":
                basic += 1
            elif plan == "premium":
                premium += 1
            elif plan == "familiar":
                familiar += 1
            
            agregar = input("Presione enter para agregar otro estudiante / ingrese (x) para salir: ")
            
            if agregar.strip() != "":
                add_persona = False

        total_basic = 50000 * basic
        total_premium = 90000 * premium
        total_familiar = 130000 * familiar

        total = total_basic + total_premium + total_familiar

        if total_basic > total_premium and total_premium >= total_familiar:
            plan_max = "basico"
        if total_premium > total_basic and total_basic >= total_familiar:
            plan_max = "premium"
        if total_familiar > total_premium and total_premium >= total_basic:
            plan_max = "familiar"

        print(f"Total recaudado: {total}")
        print("Personas por plan:")
        print(f"basico: {basic}")
        print(f"premium: {premium}")
        print(f"familiar: {familiar}")
        print(f"Plan mas vendido: {plan_max}")