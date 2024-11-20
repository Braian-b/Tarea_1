## Braian Betancourt
## Programa que cuenta las consonantes de una cadena

cadena = input("Introduce una Cadena ") ## Pedir la cadena al usuario

## Busco la primera aparicion de cada consonante de la cadena y guardo su posicion en buscar_letra
buscar_letraB = cadena.find("b")
buscar_letraC = cadena.find("c")
buscar_letraD = cadena.find("d")

buscar_letraF = cadena.find("f")
buscar_letraG = cadena.find("g")
buscar_letraH = cadena.find("h")

buscar_letraJ = cadena.find("j")
buscar_letraK = cadena.find("k")
buscar_letraL = cadena.find("l")
buscar_letraM = cadena.find("m")
buscar_letraN = cadena.find("n")

buscar_letraP = cadena.find("p")
buscar_letraQ = cadena.find("q")
buscar_letraR = cadena.find("r")
buscar_letraS = cadena.find("s")
buscar_letraT = cadena.find("t")

buscar_letraV = cadena.find("v")
buscar_letraW = cadena.find("w")
buscar_letraX = cadena.find("x")
buscar_letraY = cadena.find("y")
buscar_letraZ = cadena.find("z")

## Ahora toca revisar cuantas veces se repite la letra
## Poe ejemplo la A

if buscar_letraB != -1: ## Aqui revisamos si la consonate "b" fue encontrada por eso usamos el -1 porque si guardo una posicion va a ser diferente a -1
    cuenta_B = 1
    if cadena.find("b", buscar_letraB + 1) != -1: ## Aqui hacemos lo mismo buscar una "b" pero le decimos al indice que inicie desde donde encontro la primera b +1
        cuenta_B += 1
    if cadena.find("b", buscar_letraB + 2) != -1:
        cuenta_B += 1
    if cadena.find("b", buscar_letraB + 3) != -1:
        cuenta_B += 1
else:
    cuenta_B = 0 ## Y en caso de que no encontro nada pues el valor es 0

if buscar_letraC != -1:
    cuenta_C = 1
    if cadena.find("c", buscar_letraC + 1) != -1:
        cuenta_C += 1
    if cadena.find("c", buscar_letraC + 2) != -1:
        cuenta_C += 1
    if cadena.find("c", buscar_letraC + 3) != -1:
        cuenta_C += 1
else:
    cuenta_C = 0

if buscar_letraD != -1:
    cuenta_D = 1
    if cadena.find("d", buscar_letraD + 1) != -1:
        cuenta_D += 1
    if cadena.find("d", buscar_letraD + 2) != -1:
        cuenta_D += 1
    if cadena.find("d", buscar_letraD + 3) != -1:
        cuenta_D += 1
else:
    cuenta_D = 0

if buscar_letraF != -1:
    cuenta_F = 1
    if cadena.find("f", buscar_letraF + 1) != -1:
        cuenta_F += 1
    if cadena.find("f", buscar_letraF + 2) != -1:
        cuenta_F += 1
    if cadena.find("f", buscar_letraF + 3) != -1:
        cuenta_F += 1
else:
    cuenta_F = 0

if buscar_letraG != -1:
    cuenta_G = 1
    if cadena.find("g", buscar_letraG + 1) != -1:
        cuenta_G += 1
    if cadena.find("g", buscar_letraG + 2) != -1:
        cuenta_G += 1
    if cadena.find("g", buscar_letraG + 3) != -1:
        cuenta_G += 1
else:
    cuenta_G = 0

if buscar_letraH != -1:
    cuenta_H = 1
    if cadena.find("h", buscar_letraH + 1) != -1:
        cuenta_H += 1
    if cadena.find("h", buscar_letraH + 2) != -1:
        cuenta_H += 1
    if cadena.find("h", buscar_letraH + 3) != -1:
        cuenta_H += 1
else:
    cuenta_H = 0

if buscar_letraJ != -1:
    cuenta_J = 1
    if cadena.find("j", buscar_letraJ + 1) != -1:
        cuenta_J += 1
    if cadena.find("j", buscar_letraJ + 2) != -1:
        cuenta_J += 1
    if cadena.find("j", buscar_letraJ + 3) != -1:
        cuenta_J += 1
else:
    cuenta_J = 0

if buscar_letraK != -1:
    cuenta_K = 1
    if cadena.find("k", buscar_letraK + 1) != -1:
        cuenta_K += 1
    if cadena.find("k", buscar_letraK + 2) != -1:
        cuenta_K += 1
    if cadena.find("k", buscar_letraK + 3) != -1:
        cuenta_K += 1
else:
    cuenta_K = 0

if buscar_letraL != -1:
    cuenta_L = 1
    if cadena.find("l", buscar_letraL + 1) != -1:
        cuenta_L += 1
    if cadena.find("l", buscar_letraL + 2) != -1:
        cuenta_L += 1
    if cadena.find("l", buscar_letraL + 3) != -1:
        cuenta_L += 1
else:
    cuenta_L = 0

if buscar_letraM != -1:
    cuenta_M = 1
    if cadena.find("m", buscar_letraM + 1) != -1:
        cuenta_M += 1
    if cadena.find("m", buscar_letraM + 2) != -1:
        cuenta_M += 1
    if cadena.find("m", buscar_letraM + 3) != -1:
        cuenta_M += 1
else:
    cuenta_M = 0

if buscar_letraN != -1:
    cuenta_N = 1
    if cadena.find("n", buscar_letraN + 1) != -1:
        cuenta_N += 1
    if cadena.find("n", buscar_letraN + 2) != -1:
        cuenta_N += 1
    if cadena.find("n", buscar_letraN + 3) != -1:
        cuenta_N += 1
else:
    cuenta_N = 0

if buscar_letraP != -1:
    cuenta_P = 1
    if cadena.find("p", buscar_letraP + 1) != -1:
        cuenta_P += 1
    if cadena.find("p", buscar_letraP + 2) != -1:
        cuenta_P += 1
    if cadena.find("p", buscar_letraP + 3) != -1:
        cuenta_P += 1
else:
    cuenta_P = 0

if buscar_letraQ != -1:
    cuenta_Q = 1
    if cadena.find("q", buscar_letraQ + 1) != -1:
        cuenta_Q += 1
    if cadena.find("q", buscar_letraQ + 2) != -1:
        cuenta_Q += 1
    if cadena.find("q", buscar_letraQ + 3) != -1:
        cuenta_Q += 1
else:
    cuenta_Q = 0

if buscar_letraR != -1:
    cuenta_R = 1
    if cadena.find("r", buscar_letraR + 1) != -1:
        cuenta_R += 1
    if cadena.find("r", buscar_letraR + 2) != -1:
        cuenta_R += 1
    if cadena.find("r", buscar_letraR + 3) != -1:
        cuenta_R += 1
else:
    cuenta_R = 0

if buscar_letraS != -1:
    cuenta_S = 1
    if cadena.find("s", buscar_letraS + 1) != -1:
        cuenta_S += 1
    if cadena.find("s", buscar_letraS + 2) != -1:
        cuenta_S += 1
    if cadena.find("s", buscar_letraS + 3) != -1:
        cuenta_S += 1
else:
    cuenta_S = 0

if buscar_letraT != -1:
    cuenta_T = 1
    if cadena.find("t", buscar_letraT + 1) != -1:
        cuenta_T += 1
    if cadena.find("t", buscar_letraT + 2) != -1:
        cuenta_T += 1
    if cadena.find("t", buscar_letraT + 3) != -1:
        cuenta_T += 1
else:
    cuenta_T = 0

if buscar_letraV != -1:
    cuenta_V = 1
    if cadena.find("v", buscar_letraV + 1) != -1:
        cuenta_V += 1
    if cadena.find("v", buscar_letraV + 2) != -1:
        cuenta_V += 1
    if cadena.find("v", buscar_letraV + 3) != -1:
        cuenta_V += 1
else:
    cuenta_V = 0

if buscar_letraW != -1:
    cuenta_W = 1
    if cadena.find("w", buscar_letraW + 1) != -1:
        cuenta_W += 1
    if cadena.find("w", buscar_letraW + 2) != -1:
        cuenta_W += 1
    if cadena.find("w", buscar_letraW + 3) != -1:
        cuenta_W += 1
else:
    cuenta_W = 0

if buscar_letraX != -1:
    cuenta_X = 1
    if cadena.find("x", buscar_letraX + 1) != -1:
        cuenta_X += 1
    if cadena.find("x", buscar_letraX + 2) != -1:
        cuenta_X += 1
    if cadena.find("x", buscar_letraX + 3) != -1:
        cuenta_X += 1
else:
    cuenta_X = 0

if buscar_letraY != -1:
    cuenta_Y = 1
    if cadena.find("y", buscar_letraY + 1) != -1:
        cuenta_Y += 1
    if cadena.find("y", buscar_letraY + 2) != -1:
        cuenta_Y += 1
    if cadena.find("y", buscar_letraY + 3) != -1:
        cuenta_Y += 1
else:
    cuenta_Y = 0

if buscar_letraZ != -1:
    cuenta_Z = 1
    if cadena.find("z", buscar_letraZ + 1) != -1:
        cuenta_Z += 1
    if cadena.find("z", buscar_letraZ + 2) != -1:
        cuenta_Z += 1
    if cadena.find("z", buscar_letraZ + 3) != -1:
        cuenta_Z += 1
else:
    cuenta_Z = 0

print(f"b: {cuenta_B}")## Aqui mostramos todos los resultados para cada consonante
print(f"c: {cuenta_C}")
print(f"d: {cuenta_D}")
print(f"f: {cuenta_F}")
print(f"g: {cuenta_G}")
print(f"h: {cuenta_H}")
print(f"j: {cuenta_J}")
print(f"k: {cuenta_K}")
print(f"l: {cuenta_L}")
print(f"m: {cuenta_M}")
print(f"n: {cuenta_N}")
print(f"p: {cuenta_P}")
print(f"q: {cuenta_Q}")
print(f"r: {cuenta_R}")
print(f"s: {cuenta_S}")
print(f"t: {cuenta_T}")
print(f"v: {cuenta_V}")
print(f"w: {cuenta_W}")
print(f"x: {cuenta_X}")
print(f"y: {cuenta_Y}")
print(f"z: {cuenta_Z}")

Total_consonantes = cuenta_B + cuenta_C + cuenta_D + cuenta_F + cuenta_G + cuenta_H + cuenta_J + cuenta_K + cuenta_L + cuenta_M + cuenta_N + cuenta_P + cuenta_Q + cuenta_R + cuenta_S + cuenta_T + cuenta_V + cuenta_W + cuenta_X + cuenta_Y + cuenta_Z

print ("El numero total de consonantes son: ",Total_consonantes)
