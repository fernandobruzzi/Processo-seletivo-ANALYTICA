#ajeitar ordem dos numeros

freq_list = list()
freq_set = set()
while True:
    inp = eval(input())
    if inp == 'f':
        freq_list.sort()
        for i in freq_set:
            if freq_list.count(i) > 1:
                print(f'O número {i} apareceu {freq_list.count(i)} vezes')
            else:
                print(f'O número {i} apareceu {freq_list.count(i)} vez')
        print("Fim...")
        break
    if not isinstance(inp, int):
        continue
    freq_list += [inp]
    freq_set.add(inp)


