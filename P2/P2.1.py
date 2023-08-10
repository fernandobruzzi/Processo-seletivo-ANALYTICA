while True:
    inp = input()
    if inp == "f":
        break
    if len(inp) > 5 or ":" not in inp: #aqui checamos se o input é válido
        print("Input inválido")
    else:
        hora = int(inp[:2])
        min = int(inp[3:])
        if hora >= 12:
            hora -= 12
        a_hora = hora * 30 #aqui conseguimos o valor da hora em graus
        a_min = min * 6
        if a_hora > a_min:
            ang = a_hora - a_min
        else: ang = a_min - a_hora
        print(f'o menor ângulo é de {ang}°')

