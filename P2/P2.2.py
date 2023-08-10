conversor_letra_numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
while True:
    inp = input()
    if inp == "f":
        break
    if len(inp) > 5 or " " not in inp:
        print("Input inválido")
    else:
        pi = (conversor_letra_numero[inp[0]], int(inp[1]))
        pf = (conversor_letra_numero[inp[3]], int(inp[4]))
        posicoes_possiveis = [(pi[0]+1,pi[1]+2), (pi[0]+1,pi[1]-2), (pi[0]+2, pi[1]+1), (pi[0]+2, pi[1]-1), (pi[0]-1,pi[1]+2), (pi[0]-1,pi[1]-2), (pi[0]-2, pi[1]+1), (pi[0]-2, pi[1]-1)]
        if pf not in posicoes_possiveis:
            print("INVÁLIDO")
        if pf in posicoes_possiveis:
            print("VÁLIDO")
