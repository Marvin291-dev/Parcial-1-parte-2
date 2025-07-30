while True:
    print("\nBienvenido")
    print("1. Calcular el MCD de dos números")
    print("2. Cadena repetida")
    print("3. Contar cuantas veces aparece una letra en una cadena")
    print("4. Convertir un numero decimal a binario")
    print("5 Calcular cuantos dígitos tiene un número")
    print("6. Salir")
    try:
        opcion = int(input("Ingresa una opcion: "))
        match opcion:
            case 1:
                print()
            case 2:
                def Repetir_Palabra(palabra, veces):
                    if veces <= 0:
                        return 0
                    if veces == 1:
                        return palabra
                    return palabra + Repetir_Palabra(palabra, veces - 1)

                Frase = input("Ingresa una frase: ")
                Cantidad = int(input("Cuantas veces desea ingresar: "))

                Resultado = Repetir_Palabra(Frase, Cantidad)
                print(Resultado)
            case 3:
                def Contar_Palabra(Palabra, letra):
                    if not Palabra:
                        return 0
                    elif Palabra[0] == letra:
                        return 1 + Contar_Palabra(Palabra[1:], letra)
                    else:
                        return Contar_Palabra(Palabra[1:], letra)

                palabra = input("Ingresa una palabra: ")
                letra = input("Ingresa una letra que quieres contar: ").strip()

                if len(letra) != 1:
                    print("Por favor ingrese una letra")
                else:
                    Resultado = Contar_Palabra(palabra, letra)
                    print(f"la letra {letra} aparece {Resultado} vecen en la palabra: {palabra}")
            case 4:
                def Numerodecimal_Binario(n):
                    if n < 0:
                        return "-" + Numerodecimal_Binario(-n)
                    if n == 0:
                        return 0
                    if n == 1:
                        return 1
                    return Numerodecimal_Binario(n // 2) + str(n % 2)

                numero = input("Ingresa un numero: ")

                binario = Numerodecimal_Binario(numero)
                print(binario)
            case 5:
                def Cuantos_Digitos(n):

                    if n < 10:
                        return 1
                    return 1 + Cuantos_Digitos(n // 10)
                numero = input("Ingresa un numero: ")
                binario = Cuantos_Digitos(numero)
                print(f"Cuantos {numero} tiene {binario} es: ")
            case 6:
                print("Vuelva Pronto")
                break
            case _:
                print("Opcion invalida, intente de nuevo")
    except ValueError:
        print("Por favor ingrese un numero que sea de 1 a 6")