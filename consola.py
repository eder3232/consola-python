def main():
    data = []

    while True:
        empleadoActual = {}
        print("INGRESA LOS DATOS DE ESTE EMPLEADO")
        print('o ingresa "0" para salir')

        legajo: int = inputLegajo()

        if legajo == 0:
            break

        sueldoBasico: float = inputSueldoBasico()

        antiguedad: int = inputAntiguedad()

        sexo: str = inputSexo()

        categoria: int = inputCategoria()

        empleadoActual["legajo"] = legajo
        empleadoActual["sueldoBasico"] = sueldoBasico
        empleadoActual["antiguedad"] = antiguedad
        empleadoActual["sexo"] = sexo
        empleadoActual["categoria"] = categoria

        data.append(empleadoActual)

    (
        newData,
        empleadosViejos,
        sueldoMaximo,
        legajoEmpleadoSueldoMaximo,
        numMujeres,
        numHombres,
    ) = calculadora(data)

    print(f"""el numero de hombres es: {numHombres}""")
    print(f"""el numero de mujeres es: {numMujeres}""")
    print(
        f"""el mayor sueldo es {sueldoMaximo} y corresponde a {legajoEmpleadoSueldoMaximo}"""
    )
    print(f"""hay {empleadosViejos} empleados con mas de 10 anios de antiguedad""")

    for key, value in newData.items():
        print(f"""el empleado {key} gana: {value}""")


def inputLegajo() -> int:
    inputString = input("Ingresa el legajo: ")
    print(inputString)
    if inputString == "0":
        return 0
    inputInt: int
    try:
        inputInt: int = int(inputString)
    except:
        print("porfavor ingresa un NUMERO ENTERO: ")
        inputLegajo()

    if inputInt < 1000 or inputInt > 5000:
        print("Por favor ingresa un valor entre 1000 y 5000")
        inputLegajo()
    return inputInt


def inputSueldoBasico() -> float:
    inputString: str = input("Ingresa el sueldo basico (float): ")
    inputFloat: float
    try:
        inputFloat = float(inputString)
    except:
        print("porfavor ingresa un NUMERO FLOTANTE: ")
        inputSueldoBasico()
    return inputFloat or 0


def inputAntiguedad() -> int:
    inputString: str = input("Ingresa la antiguedad (int): ")
    inputInt: int
    try:
        inputInt = int(inputString)
    except:
        print("porfavor ingresa un NUMERO ENTERO: ")
        inputSueldoBasico()

    if inputInt < 0:
        print("Porfavor ingresa un numero MAYOR A CERO")
        inputAntiguedad()
    return inputInt or 0


def inputSexo() -> str:
    inputString: str = input("Ingresa el sexo (M o F): ")

    if inputString == "M":
        return "M"
    elif inputString == "F":
        return "F"
    else:
        print("ingresa solo M o F")
        inputSexo()


def inputCategoria() -> int:
    inputString: str = input("Ingresa la categoria (int): ")
    inputInt: int
    try:
        inputInt = int(inputString)
    except:
        print("porfavor ingresa un NUMERO ENTERO: ")
        inputCategoria()
    if inputInt < 1 or inputInt > 5:
        print("ingresa un valor entre 1 y 5")
    return inputInt or 0


def calculadora(data):
    # sueldo de cada emplead
    # cantidad de empleados de  mas de 10 anios de antiguedad
    # el mayor sueldo y el legajo del empleado
    # cantidad de hombres y mujeres

    # ---------------------

    sueldos = {}

    numHombres = 0
    numMujeres = 0

    empleadosViejos = 0

    sueldoMaximo = 0
    legajoEmpleadoSueldoMaximo = 0

    for e in data:
        # print(e)
        bonificacionNumero = 0
        bonificacionPorcentaje = 0
        # calculo de la bonificacion basado en categoria
        categoria = e["categoria"]
        if categoria == 2 or categoria == 3:
            bonificacionNumero = 500
        if categoria == 4:
            bonificaionPorcentaje = 10
        if categoria == 5:
            bonificacionPorcentaje = 30

        # calculo de la bonificacion basado en la antiguedad

        antiguedad = e["antiguedad"]
        if antiguedad > 10:
            bonificacionPorcentaje += 10

        sueldoBasico = e["sueldoBasico"]

        sueldoTotal = (
            sueldoBasico
            + sueldoBasico * bonificacionPorcentaje / 100
            + bonificacionNumero
        )

        e["sueldoTotal"] = sueldoTotal

        # verificando si es el mayor sueldo hasta el momento

        if sueldoMaximo < sueldoTotal:
            sueldoMaximo = sueldoTotal
            legajoEmpleadoSueldoMaximo = e["legajo"]

        if antiguedad > 10:
            empleadosViejos += 1

        # verificar hombres y mujeres
        if e["sexo"] == "M":
            numHombres += 1
        if e["sexo"] == "F":
            numMujeres += 1

        sueldos[e["legajo"]] = sueldoTotal

    return (
        sueldos,
        empleadosViejos,
        sueldoMaximo,
        legajoEmpleadoSueldoMaximo,
        numMujeres,
        numHombres,
    )


main()

# print(inputLegajo())
# print(inputSueldoBasico())
