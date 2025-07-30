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
                print()
            case 5:
                print()
            case 6:
                print("Vuelva Pronto")
                break
            case _:
                print("Opcion invalida, intente de nuevo")
    except ValueError:
        print("Por favor ingrese un numero que sea de 1 a 6")