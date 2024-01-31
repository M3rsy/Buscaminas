import random

def crear_tablero(ancho, alto, num_minas):
    tablero = [[0 for _ in range(ancho)] for _ in range(alto)]
    minas_colocadas = 0

    while minas_colocadas < num_minas:
        x = random.randint(0, ancho - 1)
        y = random.randint(0, alto - 1)

        if tablero[y][x] != 'X':
            tablero[y][x] = 'X'
            minas_colocadas += 1

    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))

def contar_minas_adyacentes(tablero, x, y):
    minas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < len(tablero[0]) and 0 <= y + j < len(tablero):
                if tablero[y + j][x + i] == 'X':
                    minas += 1
    return minas

def revelar_celda(tablero, x, y):
    if tablero[y][x] == 'X':
        return "Has perdido!"
    else:
        minas = contar_minas_adyacentes(tablero, x, y)
        tablero[y][x] = minas
        return tablero

def juego_terminado(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                return False
    return True

def jugar():
    ancho, alto, num_minas = 10, 10, 10
    tablero = crear_tablero(ancho, alto, num_minas)

    while True:
        mostrar_tablero(tablero)
        try:
            x = int(input("Elige una columna: "))
            y = int(input("Elige una fila: "))

            resultado = revelar_celda(tablero, x, y)
            if isinstance(resultado, str):
                print(resultado)
                break
            else:
                tablero = resultado

            if juego_terminado(tablero):
                print("¡Has ganado!")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    jugar()
