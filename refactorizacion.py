def introducir_puntos_y_comentarios():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        if point.isdecimal() and 1 <= int(point) <= 5:
            comment = input('Introduzca sus comentarios: ')
            with open("data.txt", 'a') as file_pc:
                file_pc.write(f'punto: {point} comentario: {comment}\n')
            break
        else:
            print('Ingrese un valor de 1 a 5')

def comprobar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            data = [line.strip() for line in read_file]
            print('Resultados hasta la fecha:')
            for item in data:
                print(item)
    except FileNotFoundError:
        print('No hay resultados hasta ahora.')

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Introducir puntos de evaluación y comentarios')
    print('2: Comprobar los resultados hasta ahora')
    print('3: Terminar')
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            introducir_puntos_y_comentarios()
        elif num == 2:
            comprobar_resultados()
        elif num == 3:
            print('Terminación.')
            break
        else:
            print('Introduzca de 1 a 3')
    else:
        print('Introduzca de 1 a 3')