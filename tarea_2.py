## Braian Betancourt
## Programa que verifica si los simbolos de una cadena (Maximos 6 simbolos) son letras

cadena = input("Introduce una cadena de caracteres: ") ## Le pedimos al usuario que ingrese sus caracteres

if cadena == "": ## iniciamos un condicional para ver que el usuarion ingreso algo
    print("No ingreso una cadena")
else: ## si el usuario ingreso algo ejecutamos el resto del codigo

    caracter = cadena[0] ## Guardamos el primer caracter que haya ingresado el usuario

    if 65 <= ord(caracter) <= 90 or 97 <= ord(caracter) <= 122: ## usamos el "ord" para convertir el caracter a su valor en el codigo ascci
        if len(cadena) == 1: ## Usamos el "len" para saber cuantos caracteres hay en la cadena 
            print("Todos los símbolos son letras del abecedario.")
        else:
                ## Luego repetimos el bloque cambiando los nombres de las variables para el siguiente caracter
            caracter_2 = cadena[1]
            if 65 <= ord(caracter_2) <= 90 or 97 <= ord(caracter_2) <= 122:
                if len(cadena) == 2:  
                    print("Todos los símbolos son letras del abecedario.")
                else:
                    
                    caracter_3 = cadena[2]
                    if 65 <= ord(caracter_3) <= 90 or 97 <= ord(caracter_3) <= 122:
                        if len(cadena) == 3:  
                            print("Todos los símbolos son letras del abecedario.")
                        else:

                            caracter_4 = cadena[3]
                            if 65 <= ord(caracter_4) <= 90 or 97 <= ord(caracter_4) <= 122:
                                if len(cadena) == 4:  
                                    print("Todos los símbolos son letras del abecedario.")
                                else:

                                    caracter_5 = cadena[4]
                                    if 65 <= ord(caracter_5) <= 90 or 97 <= ord(caracter_5) <= 122:
                                        if len(cadena) == 5:  
                                            print("Todos los símbolos son letras del abecedario.")
                                        else:

                                            caracter_6 = cadena[5]
                                            if 65 <= ord(caracter_6) <= 90 or 97 <= ord(caracter_6) <= 122:
                                                if len(cadena) == 6:  
                                                    print("Todos los símbolos son letras del abecedario.")
                                                else:
                                                    print("llego al limite de caracteres que admite el programa") 
                                                    ## Llegamos al limite que seria 6 pero este limite se puede aumentar
                                            else:
                                                print("No todos los símbolos son letras del abecedario.") 
                                                ## Cuidosamente alineamos estos else con los if que revisan si el caracter es una letra
                                    else:
                                        print("No todos los símbolos son letras del abecedario.")
                            else:
                                print("No todos los símbolos son letras del abecedario.")
                    else:
                        print("No todos los símbolos son letras del abecedario.")
            else:
                print("No todos los símbolos son letras del abecedario.")
    else:
        print("No todos los símbolos son letras del abecedario.")